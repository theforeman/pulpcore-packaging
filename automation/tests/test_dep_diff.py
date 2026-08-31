"""Unit tests for automation/dep_diff.py."""

import json
import sys
import tempfile
import textwrap
from io import BytesIO
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
import dep_diff as dd


def _mock_pypi(requires_dist):
    response_data = json.dumps({"info": {"requires_dist": requires_dist}}).encode()
    cm = MagicMock()
    cm.__enter__ = lambda s: BytesIO(response_data)
    cm.__exit__ = MagicMock(return_value=False)
    return cm


@pytest.mark.parametrize("dep,expected_in_result", [
    ('requests; extra == "security"', False),
    ('tzdata; sys_platform == "win32"', False),
    ('colorama; platform_system == "Windows"', False),
    ('pywin32; os_name == "nt"', False),
    ('pyobjc; sys_platform == "darwin"', False),
    ('pyobjc; platform_system == "Darwin"', False),
    ('typing-extensions >= 4.6', True),
])
def test_pypi_mandatory_deps_filtering(dep, expected_in_result):
    mock_cm = _mock_pypi([dep])
    with patch("urllib.request.urlopen", return_value=mock_cm), \
         patch("time.sleep"):
        result = dd.pypi_mandatory_deps("somepkg", "1.0")
    if expected_in_result:
        assert len(result) > 0, f"Expected {dep!r} to be included but got empty"
    else:
        assert len(result) == 0, f"Expected {dep!r} to be excluded but got {result}"


_SAMPLE_SPEC = textwrap.dedent("""\
    Name: python3.12-psycopg
    Requires: python%{python3_pkgversion}-typing-extensions >= 4.6
    Requires: python%{python3_pkgversion}-tzdata
""")


def test_parse_spec_requires_expands_macros():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".spec", delete=False) as f:
        f.write(_SAMPLE_SPEC)
        tmp = f.name
    result = dd.parse_spec_requires(tmp)
    assert "python3.12-typing-extensions" in result
    assert "python3.12-tzdata" in result


def test_diff_table_added_removed():
    spec = {"python3.12-foo", "python3.12-bar"}
    pypi = {"python3.12-foo", "python3.12-baz"}
    table = dd.diff_table(spec, pypi)
    assert "added" in table
    assert "python3.12-baz" in table
    assert "removed" in table
    assert "python3.12-bar" in table


def test_diff_table_no_changes():
    deps = {"python3.12-foo"}
    result = dd.diff_table(deps, deps)
    assert "No mandatory dependency changes" in result
