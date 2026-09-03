"""Regression tests for in-place dependency updates."""

import json
import sys
import textwrap
from io import BytesIO
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
import update_deps as ud


def _mock_pypi(requires_dist):
    response_data = json.dumps({"info": {"requires_dist": requires_dist}}).encode()
    context_manager = MagicMock()
    context_manager.__enter__ = lambda _self: BytesIO(response_data)
    context_manager.__exit__ = MagicMock(return_value=False)
    return context_manager


def test_python_312_linux_markers_and_all_constraints():
    dependencies = ud.requirements_from_metadata([
        "distlib<1,>=0.3.7",
        'filelock<4,>=3.24.2; python_version >= "3.10"',
        'filelock<=3.19.1,>=3.16.1; python_version < "3.10"',
        "platformdirs<5,>=3.9.1",
        "python-discovery>=1.6",
        'typing-extensions>=4.13.2; python_version < "3.11"',
        'tzdata; sys_platform == "win32"',
        'requests; extra == "test"',
    ])
    assert dependencies == [
        "python%{python3_pkgversion}-discovery >= 1.6",
        "python%{python3_pkgversion}-distlib >= 0.3.7",
        "python%{python3_pkgversion}-distlib < 1",
        "python%{python3_pkgversion}-filelock >= 3.24.2",
        "python%{python3_pkgversion}-filelock < 4",
        "python%{python3_pkgversion}-platformdirs >= 3.9.1",
        "python%{python3_pkgversion}-platformdirs < 5",
    ]


def test_compatible_release_is_translated_to_rpm_bounds():
    assert ud.requirements_from_metadata(["example~=1.4.5"]) == [
        "python%{python3_pkgversion}-example >= 1.4.5",
        "python%{python3_pkgversion}-example < 1.5",
    ]


def test_pypi_failure_raises_instead_of_clearing_dependencies():
    with patch("urllib.request.urlopen", side_effect=OSError("offline")), patch("time.sleep"):
        with pytest.raises(ud.MetadataError, match="offline"):
            ud.pypi_mandatory_deps("example", "1.0")


@pytest.mark.parametrize("rest, expected", [
    ("python%{python3_pkgversion}-foo", [("python%{python3_pkgversion}-foo", "")]),
    ("python%{python3_pkgversion}-foo >= 1.0", [("python%{python3_pkgversion}-foo", ">= 1.0")]),
    ("python%{python3_pkgversion}-foo >= %{version}", [("python%{python3_pkgversion}-foo", ">= %{version}")]),
])
def test_parse_requires_entries(rest, expected):
    assert ud.parse_requires_entries(rest) == expected


VIRTUALENV_SPEC = textwrap.dedent("""\
    %global python3_pkgversion 3.12
    %global pypi_name virtualenv

    Name:           python%{python3_pkgversion}-%{pypi_name}
    Source:         https://files.pythonhosted.org/packages/source/v/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
    BuildRequires:  python%{python3_pkgversion}-hatchling
    Requires:  python%{python3_pkgversion}-old-dependency
    Obsoletes:      python3.11-%{pypi_name} < %{version}-%{release}

    %description
    Existing description.

    %files -n python%{python3_pkgversion}-%{pypi_name}
    %{python3_sitelib}/%{pypi_name}
    %{_bindir}/%{pypi_name}
""")


def test_rewrite_preserves_spec_structure_and_updates_only_main_requires(tmp_path):
    spec = tmp_path / "python-virtualenv.spec"
    spec.write_text(VIRTUALENV_SPEC)
    before = spec.read_text()
    description_and_later = before[before.index("%description"):]

    ud.rewrite_requires(spec, [
        "python%{python3_pkgversion}-distlib >= 0.3.7",
        "python%{python3_pkgversion}-distlib < 1",
    ])
    result = spec.read_text()
    assert "Name:           python%{python3_pkgversion}-%{pypi_name}" in result
    assert "Source:         https://files.pythonhosted.org/" in result
    assert "BuildRequires:  python%{python3_pkgversion}-hatchling" in result
    assert "Obsoletes:      python3.11-%{pypi_name}" in result
    assert result[result.index("%description"):] == description_and_later
    assert "old-dependency" not in result
    assert "Requires:  python%{python3_pkgversion}-distlib >= 0.3.7" in result
    assert "Requires:  python%{python3_pkgversion}-distlib < 1" in result


def _without_main_python_requires(contents):
    preamble, description = contents.split("%description", 1)
    kept = []
    for line in preamble.splitlines(keepends=True):
        if line.startswith("Requires:"):
            value = line[len("Requires:"):].strip()
            if value and ud.is_library_name(value.split()[0]):
                continue
        kept.append(line)
    return "".join(kept) + "%description" + description


@pytest.mark.parametrize("package", ["python-virtualenv", "python-psycopg"])
def test_real_regression_specs_preserve_everything_except_main_requires(tmp_path, package):
    repository = Path(__file__).resolve().parents[2]
    original = (repository / "packages" / package / f"{package}.spec").read_text()
    spec = tmp_path / f"{package}.spec"
    spec.write_text(original)
    ud.rewrite_requires(spec, ["python%{python3_pkgversion}-replacement >= 1"])
    assert _without_main_python_requires(spec.read_text()) == _without_main_python_requires(original)


def test_all_existing_specs_are_byte_identical_for_unchanged_requirements(tmp_path):
    repository = Path(__file__).resolve().parents[2]
    for source_spec in repository.glob("packages/python-*/*.spec"):
        original = source_spec.read_text()
        requirements = []
        for line in original.splitlines():
            if line.startswith("%description"):
                break
            if not line.startswith("Requires:"):
                continue
            for name, constraint in ud.parse_requires_entries(
                line[len("Requires:"):].strip()
            ):
                if ud.is_library_name(name):
                    requirements.append(f"{name} {constraint}".rstrip())
        spec = tmp_path / source_spec.name
        spec.write_text(original)
        ud.rewrite_requires(spec, requirements)
        assert spec.read_text() == original, source_spec


def test_rewrite_preserves_existing_rpm_dependency_spelling(tmp_path):
    spec = tmp_path / "example.spec"
    spec.write_text("Requires:       python%{python3_pkgversion}-PyYAML\n\n%description\nx\n")
    ud.rewrite_requires(spec, ["python%{python3_pkgversion}-pyyaml >= 6"])
    assert "python%{python3_pkgversion}-PyYAML >= 6" in spec.read_text()


def test_semantically_unchanged_macro_constraint_is_byte_identical(tmp_path):
    spec = tmp_path / "example.spec"
    original = textwrap.dedent("""\
        Version: 1.43.88
        Requires:       python%{python3_pkgversion}-botocore >= %{version}
        Requires:       python%{python3_pkgversion}-botocore < 1.44.0
        %description
        Example.
    """)
    spec.write_text(original)
    ud.rewrite_requires(spec, [
        "python%{python3_pkgversion}-botocore >= 1.43.88",
        "python%{python3_pkgversion}-botocore < 1.44.0",
    ])
    assert spec.read_text() == original


def test_real_botocore_conditional_policy_is_byte_identical(tmp_path):
    repository = Path(__file__).resolve().parents[2]
    original = (
        repository / "packages/python-botocore/python-botocore.spec"
    ).read_text()
    spec = tmp_path / "python-botocore.spec"
    spec.write_text(original)
    ud.rewrite_requires(spec, ud.requirements_from_metadata([
        "jmespath<2.0.0,>=0.7.1",
        "python-dateutil<3.0.0,>=2.1",
        'urllib3!=2.2.0,<3,>=1.25.4; python_version >= "3.10"',
    ]))
    assert spec.read_text() == original


def test_rewrite_does_not_touch_subpackage_requires(tmp_path):
    spec = tmp_path / "example.spec"
    spec.write_text(textwrap.dedent("""\
        Requires:       python%{python3_pkgversion}-old
        %description
        Main package.
        %package extra
        Requires:       python%{python3_pkgversion}-self = %{version}-%{release}
        %description extra
        Extra package.
    """))
    ud.rewrite_requires(spec, ["python%{python3_pkgversion}-new"])
    result = spec.read_text()
    assert "python%{python3_pkgversion}-old" not in result
    assert "Requires:       python%{python3_pkgversion}-new" in result
    assert "Requires:       python%{python3_pkgversion}-self = %{version}-%{release}" in result


def test_conditional_main_requires_are_preserved_while_other_deps_update(tmp_path):
    spec = tmp_path / "example.spec"
    original = textwrap.dedent("""\
        %if 0%{?rhel} == 9
        Requires: python%{python3_pkgversion}-foo < 2
        %else
        Requires: python%{python3_pkgversion}-foo < 3
        %endif
        %description
        Example.
    """)
    spec.write_text(original)
    ud.rewrite_requires(spec, [
        "python%{python3_pkgversion}-foo < 4",
        "python%{python3_pkgversion}-bar >= 1",
    ])
    result = spec.read_text()
    assert "%if 0%{?rhel} == 9\nRequires: python%{python3_pkgversion}-foo < 2" in result
    assert "%else\nRequires: python%{python3_pkgversion}-foo < 3\n%endif" in result
    assert "python%{python3_pkgversion}-foo < 4" not in result
    assert "Requires:       python%{python3_pkgversion}-bar >= 1" in result


def test_mixed_requires_line_is_rejected_without_changes(tmp_path):
    spec = tmp_path / "example.spec"
    original = "Requires: python%{python3_pkgversion}-foo /etc/mime.types\n%description\nx\n"
    spec.write_text(original)
    with pytest.raises(ud.UnsafeSpecError, match="mixed Python and non-Python"):
        ud.rewrite_requires(spec, ["python%{python3_pkgversion}-bar"])
    assert spec.read_text() == original


def test_unrelated_conditional_does_not_block_requires_update(tmp_path):
    spec = tmp_path / "example.spec"
    spec.write_text(textwrap.dedent("""\
        Requires: python%{python3_pkgversion}-old
        %if 0%{?rhel} >= 10
        BuildRequires: cargo-rpm-macros
        %endif
        %description
        Example.
    """))
    ud.rewrite_requires(spec, ["python%{python3_pkgversion}-new"])
    assert "Requires: python%{python3_pkgversion}-new" in spec.read_text()


def test_empty_metadata_really_clears_main_python_requires(tmp_path):
    spec = tmp_path / "example.spec"
    spec.write_text("Requires: python%{python3_pkgversion}-old\nRequires: /etc/mime.types\n%description\nx\n")
    ud.rewrite_requires(spec, [])
    assert spec.read_text() == "Requires: /etc/mime.types\n%description\nx\n"


def test_fetch_parses_response():
    with patch("urllib.request.urlopen", return_value=_mock_pypi(["requests>=2,<3"])), patch("time.sleep"):
        assert ud.pypi_mandatory_deps("example", "1") == [
            "python%{python3_pkgversion}-requests >= 2",
            "python%{python3_pkgversion}-requests < 3",
        ]


def test_matching_pypi_source_macros_are_preserved(tmp_path):
    spec = tmp_path / "example.spec"
    original = textwrap.dedent("""\
        %global pypi_name example
        Version: 1.0
        Source: https://files.pythonhosted.org/packages/source/e/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
    """)
    spec.write_text(original)
    ud.update_pypi_source_filename(spec, {
        "urls": [{"packagetype": "sdist", "filename": "example-1.0.tar.gz"}],
    }, "1.0")
    assert spec.read_text() == original


def test_optional_source_suffix_macro_is_preserved_for_stable_release(tmp_path):
    spec = tmp_path / "example.spec"
    original = textwrap.dedent("""\
        %global src_name pulp_ostree
        Version: 2.6.1
        Source0: https://files.pythonhosted.org/packages/source/p/%{src_name}/%{src_name}-%{version}%{?prerelease}.tar.gz
    """)
    spec.write_text(original)
    ud.update_pypi_source_filename(spec, {
        "urls": [{"packagetype": "sdist", "filename": "pulp_ostree-2.6.1.tar.gz"}],
    }, "2.6.1")
    assert spec.read_text() == original


def test_pypi_source_uses_actual_normalized_sdist_filename(tmp_path):
    spec = tmp_path / "python-ruamel-yaml.spec"
    spec.write_text(textwrap.dedent("""\
        %global pypi_name ruamel.yaml
        Version: 0.19.1
        Source: https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
    """))
    ud.update_pypi_source_filename(spec, {
        "urls": [{"packagetype": "sdist", "filename": "ruamel_yaml-0.19.1.tar.gz"}],
    }, "0.19.1")
    assert spec.read_text().endswith(
        "https://files.pythonhosted.org/packages/source/r/%{pypi_name}/ruamel_yaml-%{version}.tar.gz\n"
    )


def test_new_unpackaged_dependency_is_detected(tmp_path):
    packages = tmp_path / "packages"
    package = packages / "python-example"
    package.mkdir(parents=True)
    spec = package / "python-example.spec"
    spec.write_text("Requires: python%{python3_pkgversion}-setuptools\n")
    assert ud.unpackaged_dependencies(spec, [
        "python%{python3_pkgversion}-setuptools",
        "python%{python3_pkgversion}-httpx2 >= 0.22",
    ]) == {"httpx2"}


def test_main_does_not_modify_spec_with_unpackageable_dependency(tmp_path, monkeypatch):
    packages = tmp_path / "packages"
    package = packages / "python-example"
    package.mkdir(parents=True)
    spec = package / "python-example.spec"
    original = textwrap.dedent("""\
        Version: 1.0
        Source: https://files.pythonhosted.org/packages/source/e/example/example-%{version}.tar.gz
        Requires: python%{python3_pkgversion}-known
        %description
        Example.
    """)
    spec.write_text(original)
    monkeypatch.setattr(ud, "pypi_release_data", lambda *_args: {
        "info": {"requires_dist": ["unknown-package>=1"]},
        "urls": [{"packagetype": "sdist", "filename": "example-2.0.tar.gz"}],
    })
    monkeypatch.setattr(sys, "argv", ["update_deps.py", str(spec), "example", "2.0"])
    assert ud.main() == 1
    assert spec.read_text() == original
