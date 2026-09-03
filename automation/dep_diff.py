#!/usr/bin/env python3
"""Compare an existing spec's main runtime dependencies with PyPI metadata."""

import re
import sys

import update_deps


def parse_spec_requires(spec_file):
    """Return normalized main-package Python Requires, including constraints."""
    requires = set()
    with open(spec_file) as handle:
        for line in handle:
            if line.startswith("%description"):
                break
            stripped = line.strip()
            if not stripped.startswith("Requires:"):
                continue
            entries = update_deps.parse_requires_entries(
                stripped[len("Requires:"):].strip()
            )
            for name, constraint in entries:
                dependency_name = update_deps.rpm_dependency_name(name)
                if dependency_name is None:
                    continue
                value = f"python{update_deps.PYTHON_VER}-{dependency_name}"
                if constraint:
                    value = f"{value} {constraint}"
                requires.add(value)
    return requires


def pypi_mandatory_deps(pypi_name, version):
    return {
        re.sub(
            r"^python%\{python3_pkgversion\}-",
            f"python{update_deps.PYTHON_VER}-",
            value,
        )
        for value in update_deps.pypi_mandatory_deps(pypi_name, version)
    }


def diff_table(spec_requires, pypi_requires):
    added = sorted(pypi_requires - spec_requires)
    removed = sorted(spec_requires - pypi_requires)
    unchanged = sorted(spec_requires & pypi_requires)
    if not added and not removed:
        return "_No mandatory dependency changes detected._\n"

    lines = ["| Status | Requirement |", "|--------|-------------|"]
    lines.extend(f"| :green_circle: added | `{value}` |" for value in added)
    lines.extend(f"| :red_circle: removed | `{value}` |" for value in removed)
    lines.extend(f"| unchanged | `{value}` |" for value in unchanged)
    return "\n".join(lines) + "\n"


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <spec_file> <pypi_name> <version>", file=sys.stderr)
        return 2
    spec_file, pypi_name, version = sys.argv[1], sys.argv[2], sys.argv[3]
    try:
        pypi_requires = pypi_mandatory_deps(pypi_name, version)
    except update_deps.MetadataError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(diff_table(parse_spec_requires(spec_file), pypi_requires))
    return 0


if __name__ == "__main__":
    sys.exit(main())
