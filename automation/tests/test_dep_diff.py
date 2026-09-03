"""Unit tests for dependency-change reporting."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import dep_diff as dd


def test_parse_spec_requires_stops_at_main_description(tmp_path):
    spec = tmp_path / "example.spec"
    spec.write_text(
        "Requires: python%{python3_pkgversion}-foo >= 1\n"
        "%description\n"
        "Requires: python%{python3_pkgversion}-subpackage\n"
    )
    assert dd.parse_spec_requires(spec) == {"python3.12-foo >= 1"}


def test_conditional_dependencies_can_be_excluded_from_diff(tmp_path):
    spec = tmp_path / "example.spec"
    spec.write_text(
        "%if 0%{?rhel} == 9\n"
        "Requires: python%{python3_pkgversion}-foo < 2\n"
        "%else\n"
        "Requires: python%{python3_pkgversion}-foo < 3\n"
        "%endif\n"
        "Requires: python%{python3_pkgversion}-bar >= 1\n"
        "%description\n"
    )
    protected = dd.conditional_dependency_names(spec)
    assert protected == {"foo"}
    assert dd.parse_spec_requires(spec, protected) == {"python3.12-bar >= 1"}


def test_diff_table_reports_constraint_changes():
    table = dd.diff_table(
        {"python3.12-foo >= 1"},
        {"python3.12-foo >= 2", "python3.12-bar"},
    )
    assert ":green_circle: added" in table
    assert "python3.12-foo >= 2" in table
    assert "python3.12-bar" in table
    assert ":red_circle: removed" in table
    assert "python3.12-foo >= 1" in table


def test_diff_table_no_changes():
    dependencies = {"python3.12-foo >= 1"}
    assert "No mandatory dependency changes" in dd.diff_table(dependencies, dependencies)
