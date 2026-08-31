#!/usr/bin/env python3
"""Regenerate Requires in an existing spec file using PyPI dependency metadata.

Usage:
    python3 automation/update_deps.py <spec_file> <pypi_name> <version>

Replaces mandatory (non-extra) Requires: python3.12-* entries in the spec
with the new version's declared runtime dependencies from the PyPI JSON API.
Toolchain BuildRequires (python3.12-devel, pyproject-rpm-macros, etc.) are untouched.
"""

import json
import re
import sys
import urllib.request

PYTHON_VER = "3.12"
_SEP_RE = re.compile(r"[-_.]+")
_RPM_MACRO_RE = re.compile(r"%\{python3_pkgversion\}|%\{python3_abi\}")

# Token patterns that are build toolchain, not Python library deps
_TOOLCHAIN_RE = re.compile(
    rf"python{re.escape(PYTHON_VER)}-(devel|wheel|pip|setuptools)|"
    r"pyproject-rpm-macros|gcc|make|cmake|perl|ruby"
)


def canonicalize(name):
    return _SEP_RE.sub("-", name).lower()


def pypi_mandatory_deps(pypi_name, version):
    """Return sorted list of python3.12-* RPM names for mandatory runtime deps."""
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
                return []
            time.sleep(2 ** attempt + random.uniform(0, 3))

    requires_dist = data["info"].get("requires_dist") or []
    rpm_names = set()
    for dep in requires_dist:
        if "extra ==" in dep or "extra==" in dep:
            continue
        name = re.split(r"[><=!;\s\(]", dep)[0].strip()
        if not name:
            continue
        canonical = canonicalize(name)
        if canonical.startswith("python-"):
            canonical = canonical[len("python-"):]
        rpm_names.add(f"python{PYTHON_VER}-{canonical}")
    return sorted(rpm_names)


def is_library_name(name):
    """Return True if name (after macro expansion) is a python3.12-* library dep."""
    expanded = _RPM_MACRO_RE.sub(PYTHON_VER, name)
    return (
        expanded.startswith(f"python{PYTHON_VER}-")
        and not _TOOLCHAIN_RE.search(expanded)
    )


def parse_requires_entries(rest):
    """Parse an RPM Requires value into list of (name, version_constraint) tuples.

    Handles: 'foo', 'foo >= 1.0', 'foo >= 1.0 bar baz >= 2.0'
    """
    entries = []
    tokens = rest.split()
    i = 0
    while i < len(tokens):
        name = tokens[i]
        constraint = ""
        # Consume optional version operator + value
        if i + 1 < len(tokens) and re.match(r"^[><=!]", tokens[i + 1]):
            op = tokens[i + 1]
            i += 2
            if i < len(tokens) and not re.match(r"^[><=!%a-z]", tokens[i]):
                constraint = f"{op} {tokens[i]}"
                i += 1
            else:
                constraint = op
        else:
            i += 1
        entries.append((name, constraint))
    return entries


def rewrite_requires(spec_file, new_requires):
    """Replace python3.12-* library Requires: lines in spec with new_requires."""
    with open(spec_file) as f:
        lines = f.readlines()

    out = []
    library_block_written = False

    for line in lines:
        stripped = line.rstrip()
        if not stripped.startswith("Requires:"):
            out.append(line)
            continue

        rest = stripped[len("Requires:"):].strip()
        entries = parse_requires_entries(rest)
        lib_entries = [(n, c) for n, c in entries if is_library_name(n)]
        preserved_entries = [(n, c) for n, c in entries if not is_library_name(n)]

        if not lib_entries:
            # No library entries on this line — keep it unchanged
            out.append(line)
            continue

        if library_block_written:
            # Additional library-only Requires lines are consolidated above
            continue

        indent = "Requires:       "
        # Write preserved non-library entries (with their version constraints)
        for name, constraint in preserved_entries:
            token = f"{name} {constraint}".strip()
            out.append(f"{indent}{token}\n")
        # Write the new library Requires
        for req in new_requires:
            out.append(f"{indent}{req}\n")
        library_block_written = True

    with open(spec_file, "w") as f:
        f.writelines(out)


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <spec_file> <pypi_name> <version>", file=sys.stderr)
        sys.exit(1)

    spec_file, pypi_name, version = sys.argv[1], sys.argv[2], sys.argv[3]
    new_requires = pypi_mandatory_deps(pypi_name, version)

    if not new_requires:
        print(f"INFO: no mandatory runtime deps for {pypi_name}=={version}; "
              "removing existing library Requires entries.")

    rewrite_requires(spec_file, new_requires)

    if new_requires:
        print(f"Updated Requires in {spec_file}: {', '.join(new_requires)}")
    else:
        print(f"Cleared library Requires in {spec_file} (no mandatory deps declared).")


if __name__ == "__main__":
    main()
