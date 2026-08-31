#!/usr/bin/env python3
"""Compare declared PyPI runtime deps against an existing spec file's Requires.

Usage:
    python3 automation/dep_diff.py <spec_file> <pypi_name> <version>

Outputs a markdown table of added/removed/unchanged mandatory Requires entries.
Uses the PyPI JSON API — no external tools required.
"""

import json
import re
import sys
import urllib.request

PYTHON_VER = "3.12"
_SEP_RE = re.compile(r"[-_.]+")

# RPM macro patterns to normalize before comparison
_RPM_MACRO_RE = re.compile(r"%\{python3_pkgversion\}|%\{python3_abi\}")


def canonicalize(name):
    return _SEP_RE.sub("-", name).lower()


def pypi_mandatory_deps(pypi_name, version):
    """Return set of python3.12-* RPM names for mandatory (non-extra) runtime deps."""
    import random, time
    url = f"https://pypi.org/pypi/{pypi_name}/{version}/json"
    # Jitter 0-20s so concurrent matrix jobs don't hit PyPI simultaneously
    time.sleep(random.uniform(0, 20))
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=15) as r:
                data = json.load(r)
            break
        except Exception as e:
            if attempt == 2:
                print(f"WARNING: PyPI API error for {pypi_name}=={version}: {e}", file=sys.stderr)
                return set()
            time.sleep(2 ** attempt + random.uniform(0, 3))

    requires_dist = data["info"].get("requires_dist") or []
    rpm_names = set()
    for dep in requires_dist:
        # Skip optional extras
        if "extra ==" in dep or "extra==" in dep:
            continue
        # Skip Windows/macOS-only deps; we build for Linux only
        marker_part = dep.split(";", 1)[1] if ";" in dep else ""
        if re.search(
            r'sys_platform\s*==\s*["\']win32["\']'
            r'|platform_system\s*==\s*["\']Windows["\']'
            r'|os_name\s*==\s*["\']nt["\']'
            r'|sys_platform\s*==\s*["\']darwin["\']'
            r'|platform_system\s*==\s*["\']Darwin["\']',
            marker_part,
        ):
            continue
        # Extract package name (before any version specifier or env marker)
        name = re.split(r"[><=!;\s\(]", dep)[0].strip()
        if not name:
            continue
        canonical = canonicalize(name)
        if canonical.startswith("python-"):
            canonical = canonical[len("python-"):]
        rpm_names.add(f"python{PYTHON_VER}-{canonical}")
    return rpm_names


def parse_spec_requires(spec_file):
    """Return set of python3.12-* Requires entries from spec (toolchain excluded)."""
    requires = set()
    with open(spec_file) as f:
        for line in f:
            stripped = line.strip()
            if not stripped.startswith("Requires:"):
                continue
            rest = stripped[len("Requires:"):].strip()
            # Expand RPM macros
            rest = _RPM_MACRO_RE.sub(PYTHON_VER, rest)
            for token in rest.split():
                # Skip version comparators and non-python tokens
                if re.match(r"^[><=!]", token):
                    continue
                if token.startswith(f"python{PYTHON_VER}-"):
                    requires.add(token)
    return requires


def diff_table(spec_requires, pypi_requires):
    added = sorted(pypi_requires - spec_requires)
    removed = sorted(spec_requires - pypi_requires)
    unchanged = sorted(spec_requires & pypi_requires)

    if not added and not removed:
        return "_No mandatory dependency changes detected._\n"

    lines = [
        "| Status | Package |",
        "|--------|---------|",
    ]
    for pkg in added:
        lines.append(f"| :green_circle: added | `{pkg}` |")
    for pkg in removed:
        lines.append(f"| :red_circle: removed | `{pkg}` |")
    for pkg in unchanged:
        lines.append(f"| unchanged | `{pkg}` |")
    return "\n".join(lines) + "\n"


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <spec_file> <pypi_name> <version>", file=sys.stderr)
        sys.exit(1)

    spec_file, pypi_name, version = sys.argv[1], sys.argv[2], sys.argv[3]
    spec_requires = parse_spec_requires(spec_file)
    pypi_requires = pypi_mandatory_deps(pypi_name, version)
    print(diff_table(spec_requires, pypi_requires))


if __name__ == "__main__":
    main()
