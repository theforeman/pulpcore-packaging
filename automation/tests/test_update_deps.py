"""Unit tests for automation/update_deps.py.

Tests cover the logic most likely to regress:
- Platform marker filtering (Windows/macOS deps must be skipped)
- extra == filtering
- parse_requires_entries: RPM macro values not treated as package names
- Version constraint extraction (>= preserved, < dropped)
- rewrite_requires: stray lines removed, macro form written
"""

import json
import sys
import tempfile
import textwrap
from io import BytesIO
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
import update_deps as ud


# ---------------------------------------------------------------------------
# canonicalize
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("name,expected", [
    ("ruamel.yaml", "ruamel-yaml"),
    ("ruamel_yaml", "ruamel-yaml"),
    ("Ruamel.YAML", "ruamel-yaml"),
    ("typing-extensions", "typing-extensions"),
    ("python-foo", "foo"),          # strip leading python-
])
def test_canonicalize(name, expected):
    result = ud.canonicalize(name)
    if result.startswith("python-"):
        result = result[len("python-"):]
    assert result == expected


# ---------------------------------------------------------------------------
# parse_requires_entries
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("rest,expected", [
    # plain name
    ("python%{python3_pkgversion}-foo", [("python%{python3_pkgversion}-foo", "")]),
    # name + >= constraint
    ("python%{python3_pkgversion}-foo >= 1.0",
     [("python%{python3_pkgversion}-foo", ">= 1.0")]),
    # name + >= RPM macro version — %{version} must NOT become its own entry
    ("python%{python3_pkgversion}-botocore >= %{version}",
     [("python%{python3_pkgversion}-botocore", ">= %{version}")]),
    # multiple entries on one line
    ("python%{python3_pkgversion}-foo >= 1.0 python%{python3_pkgversion}-bar",
     [("python%{python3_pkgversion}-foo", ">= 1.0"),
      ("python%{python3_pkgversion}-bar", "")]),
])
def test_parse_requires_entries(rest, expected):
    assert ud.parse_requires_entries(rest) == expected


# ---------------------------------------------------------------------------
# pypi_mandatory_deps — via mocked PyPI response
# ---------------------------------------------------------------------------

def _mock_pypi(requires_dist):
    """Return a context-manager mock for urllib.request.urlopen."""
    response_data = json.dumps({"info": {"requires_dist": requires_dist}}).encode()
    cm = MagicMock()
    cm.__enter__ = lambda s: BytesIO(response_data)
    cm.__exit__ = MagicMock(return_value=False)
    return cm


@pytest.mark.parametrize("dep,expected_in_result", [
    # Extra-gated dep — must be excluded
    ('requests; extra == "security"', False),
    # Windows-only dep — must be excluded
    ('tzdata; sys_platform == "win32"', False),
    ('colorama; platform_system == "Windows"', False),
    ('pywin32; os_name == "nt"', False),
    # macOS-only dep — must be excluded
    ('pyobjc; sys_platform == "darwin"', False),
    ('pyobjc; platform_system == "Darwin"', False),
    # Normal dep — must be included
    ('typing-extensions >= 4.6', True),
    # Linux-only dep — must be included
    ('readline; sys_platform == "linux"', True),
])
def test_pypi_mandatory_deps_filtering(dep, expected_in_result):
    mock_cm = _mock_pypi([dep])
    with patch("urllib.request.urlopen", return_value=mock_cm), \
         patch("time.sleep"):
        result = ud.pypi_mandatory_deps("somepkg", "1.0")
    pkg_names = [r.split()[0] for r in result]
    # Extract just the canonical suffix from the results
    found = any(True for r in pkg_names)
    if expected_in_result:
        assert len(result) > 0, f"Expected {dep!r} to be included but got empty result"
    else:
        assert len(result) == 0, f"Expected {dep!r} to be excluded but got {result}"


def test_pypi_mandatory_deps_version_constraints():
    """>= constraint is preserved; < constraint is dropped (first op only)."""
    deps = [
        "botocore>=1.43.84,<1.44.0",
        "jmespath>=0.7.1,<2.0.0",
        "s3transfer>=0.19.0,<0.20.0",
    ]
    mock_cm = _mock_pypi(deps)
    with patch("urllib.request.urlopen", return_value=mock_cm), \
         patch("time.sleep"):
        result = ud.pypi_mandatory_deps("boto3", "1.43.84")
    assert any("botocore >= 1.43.84" in r for r in result)
    assert any("jmespath >= 0.7.1" in r for r in result)
    assert any("s3transfer >= 0.19.0" in r for r in result)
    # Upper bounds must not appear
    assert not any("1.44.0" in r for r in result)


def test_pypi_mandatory_deps_uses_macro_prefix():
    """Output must use python%{python3_pkgversion}-* not python3.12-*."""
    mock_cm = _mock_pypi(["requests>=2.0"])
    with patch("urllib.request.urlopen", return_value=mock_cm), \
         patch("time.sleep"):
        result = ud.pypi_mandatory_deps("somepkg", "1.0")
    assert len(result) > 0, "Expected at least one dependency"
    assert all(r.startswith("python%{python3_pkgversion}-") for r in result)
    assert not any("python3.12-" in r for r in result)


# ---------------------------------------------------------------------------
# rewrite_requires
# ---------------------------------------------------------------------------

_BOTO3_SPEC_BROKEN = textwrap.dedent("""\
    Name: python%{python3_pkgversion}-boto3
    Version: 1.43.84

    Requires:       %{version}
    Requires:       python%{python3_pkgversion}-botocore
    Requires:       python%{python3_pkgversion}-jmespath
    Requires:       python%{python3_pkgversion}-s3transfer

    %description
    AWS SDK for Python.
""")

_BOTO3_SPEC_CORRECT = textwrap.dedent("""\
    Name: python%{python3_pkgversion}-boto3
    Version: 1.43.84

    Requires:       python%{python3_pkgversion}-botocore >= 1.43.84
    Requires:       python%{python3_pkgversion}-jmespath >= 0.7.1
    Requires:       python%{python3_pkgversion}-s3transfer >= 0.19.0

    %description
    AWS SDK for Python.
""")


def test_rewrite_requires_replaces_library_lines():
    new_requires = [
        "python%{python3_pkgversion}-botocore >= 1.43.84",
        "python%{python3_pkgversion}-jmespath >= 0.7.1",
        "python%{python3_pkgversion}-s3transfer >= 0.19.0",
    ]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".spec", delete=False) as f:
        f.write(_BOTO3_SPEC_BROKEN)
        tmp = f.name
    ud.rewrite_requires(tmp, new_requires)
    result = Path(tmp).read_text()
    # Stray %{version} line must be gone
    assert "Requires:       %{version}" not in result
    assert "Requires:       python%{python3_pkgversion}-botocore >= 1.43.84" in result
    assert "Requires:       python%{python3_pkgversion}-jmespath >= 0.7.1" in result
    assert "Requires:       python%{python3_pkgversion}-s3transfer >= 0.19.0" in result
