#!/usr/bin/env python3
"""Update the main package's runtime Requires from PyPI metadata.

This deliberately edits an existing spec instead of regenerating it. Specs in
this repository contain RHEL/CentOS-specific Sources, macros, patches and file
lists which a generic spec generator cannot reproduce safely.
"""

import json
import random
import re
import sys
import time
import urllib.request

from packaging.markers import default_environment
from packaging.requirements import InvalidRequirement, Requirement
from packaging.version import Version

PYTHON_VER = "3.12"
PYTHON_RPM_PREFIX = "python%{python3_pkgversion}"
_SEP_RE = re.compile(r"[-_.]+")
_RPM_MACRO_RE = re.compile(r"%\{python3_pkgversion\}|%\{python3_abi\}")


class MetadataError(RuntimeError):
    """PyPI metadata could not be fetched or parsed safely."""


class UnsafeSpecError(RuntimeError):
    """The Requires block needs packaging-policy-aware human handling."""


def canonicalize(name):
    return _SEP_RE.sub("-", name).lower()


def _marker_environment():
    environment = default_environment()
    environment.update({
        "python_version": PYTHON_VER,
        "python_full_version": f"{PYTHON_VER}.0",
        "implementation_name": "cpython",
        "implementation_version": f"{PYTHON_VER}.0",
        "os_name": "posix",
        "platform_machine": "x86_64",
        "platform_system": "Linux",
        "platform_python_implementation": "CPython",
        "sys_platform": "linux",
        "extra": "",
    })
    return environment


def _compatible_upper_bound(version):
    parsed = Version(version)
    release = list(parsed.release)
    prefix = release[:-1] if len(release) > 1 else release
    prefix[-1] += 1
    return ".".join(str(part) for part in prefix)


def _rpm_constraints(requirement):
    constraints = set()
    for specifier in requirement.specifier:
        operator, version = specifier.operator, specifier.version
        if operator == "~=":
            constraints.add((">=", version))
            constraints.add(("<", _compatible_upper_bound(version)))
        elif operator in {">=", ">", "<", "<=", "=="} and "*" not in version:
            constraints.add((operator, version))
        elif operator not in {"!="}:
            print(
                f"WARNING: unsupported PyPI constraint {specifier} for {requirement.name}; ignoring it",
                file=sys.stderr,
            )
    rank = {">=": 0, ">": 1, "==": 2, "<=": 3, "<": 4}
    return sorted(constraints, key=lambda item: (rank[item[0]], Version(item[1])))


def requirements_from_metadata(requires_dist):
    """Translate applicable Python 3.12/Linux requirements to RPM Requires."""
    dependencies = {}
    environment = _marker_environment()
    for value in requires_dist:
        try:
            requirement = Requirement(value)
        except InvalidRequirement as exc:
            raise MetadataError(f"invalid Requires-Dist entry {value!r}: {exc}") from exc
        if requirement.marker and not requirement.marker.evaluate(environment):
            continue

        name = canonicalize(requirement.name)
        if name.startswith("python-"):
            name = name[len("python-"):]
        dependencies.setdefault(name, set()).update(_rpm_constraints(requirement))

    result = []
    rank = {">=": 0, ">": 1, "==": 2, "<=": 3, "<": 4}
    for name in sorted(dependencies):
        rpm_name = f"{PYTHON_RPM_PREFIX}-{name}"
        constraints = sorted(
            dependencies[name], key=lambda item: (rank[item[0]], Version(item[1]))
        )
        result.extend(
            f"{rpm_name} {operator} {version}" for operator, version in constraints
        )
        if not constraints:
            result.append(rpm_name)
    return result


def pypi_mandatory_deps(pypi_name, version):
    """Fetch mandatory runtime requirements for Python 3.12/Linux."""
    url = f"https://pypi.org/pypi/{pypi_name}/{version}/json"
    time.sleep(random.uniform(0, 20))
    last_error = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=15) as response:
                data = json.load(response)
            try:
                requires_dist = data["info"].get("requires_dist") or []
            except (KeyError, AttributeError) as exc:
                raise MetadataError("PyPI response has no info.requires_dist field") from exc
            return requirements_from_metadata(requires_dist)
        except MetadataError:
            raise
        except Exception as exc:
            last_error = exc
            if attempt < 2:
                time.sleep(2 ** attempt + random.uniform(0, 3))
    raise MetadataError(
        f"PyPI API error for {pypi_name}=={version}: {last_error}"
    ) from last_error


def is_library_name(name):
    expanded = _RPM_MACRO_RE.sub(PYTHON_VER, name)
    return expanded.startswith(f"python{PYTHON_VER}-")


def rpm_dependency_name(name):
    """Return the canonical PyPI-like portion of an RPM Python dependency."""
    expanded = _RPM_MACRO_RE.sub(PYTHON_VER, name)
    prefix = f"python{PYTHON_VER}-"
    if not expanded.startswith(prefix):
        return None
    value = canonicalize(expanded[len(prefix):])
    return value[len("python-"):] if value.startswith("python-") else value


def parse_requires_entries(rest):
    """Parse an RPM Requires value into ``(name, constraint)`` tuples."""
    entries = []
    tokens = rest.split()
    index = 0
    while index < len(tokens):
        name = tokens[index]
        constraint = ""
        index += 1
        if index < len(tokens) and re.match(r"^[><=!~]", tokens[index]):
            operator = tokens[index]
            index += 1
            if index < len(tokens):
                constraint = f"{operator} {tokens[index]}"
                index += 1
            else:
                constraint = operator
        entries.append((name, constraint))
    return entries


def _with_preserved_names(new_requires, existing_names):
    result = []
    for requirement in new_requires:
        name, separator, constraint = requirement.partition(" ")
        replacement = existing_names.get(rpm_dependency_name(name), name)
        result.append(f"{replacement}{separator}{constraint}")
    return result


def _has_conditional_requires(lines):
    conditional_depth = 0
    for line in lines:
        stripped = line.strip()
        if re.match(r"^%(?:if|ifarch|ifnarch)\b", stripped):
            conditional_depth += 1
        elif stripped.startswith("%endif"):
            conditional_depth = max(0, conditional_depth - 1)
        elif conditional_depth and stripped.startswith("Requires:"):
            value = stripped[len("Requires:"):].strip()
            if value and is_library_name(value.split()[0]):
                return True
    return False


def _unconditional_dependency_indexes(lines):
    indexes = []
    conditional_depth = 0
    for index, line in enumerate(lines):
        stripped = line.strip()
        if re.match(r"^%(?:if|ifarch|ifnarch)\b", stripped):
            conditional_depth += 1
        elif stripped.startswith("%endif"):
            conditional_depth = max(0, conditional_depth - 1)
        elif not conditional_depth and line.startswith(("Requires:", "BuildRequires:")):
            indexes.append(index)
    return indexes


def rewrite_requires(spec_file, new_requires):
    """Replace only the main package's Python Requires block."""
    with open(spec_file) as handle:
        lines = handle.readlines()

    description_index = next(
        (index for index, line in enumerate(lines) if line.startswith("%description")),
        len(lines),
    )
    preamble = lines[:description_index]
    if _has_conditional_requires(preamble):
        raise UnsafeSpecError(
            "conditional Requires found before %description; refusing to flatten distro policy"
        )

    existing_names = {}
    library_indexes = []
    for index, line in enumerate(preamble):
        stripped = line.rstrip()
        if not stripped.startswith("Requires:"):
            continue
        entries = parse_requires_entries(stripped[len("Requires:"):].strip())
        library_entries = [name for name, _constraint in entries if is_library_name(name)]
        if library_entries and len(library_entries) != len(entries):
            raise UnsafeSpecError(
                "mixed Python and non-Python requirements found on one line; refusing a lossy rewrite"
            )
        for name, _constraint in entries:
            dependency_name = rpm_dependency_name(name)
            if dependency_name is not None:
                existing_names.setdefault(dependency_name, name)
                library_indexes.append(index)

    requires_prefix = "Requires:       "
    if library_indexes:
        match = re.match(r"^(Requires:\s*)", preamble[min(library_indexes)])
        if match:
            requires_prefix = match.group(1)
    rendered = [
        f"{requires_prefix}{value}\n"
        for value in _with_preserved_names(new_requires, existing_names)
    ]
    if library_indexes:
        first_index = min(library_indexes)
        library_index_set = set(library_indexes)
        new_preamble = []
        for index, line in enumerate(preamble):
            if index == first_index:
                new_preamble.extend(rendered)
            if index not in library_index_set:
                new_preamble.append(line)
    elif rendered:
        candidates = _unconditional_dependency_indexes(preamble)
        insert_at = (max(candidates) + 1) if candidates else len(preamble)
        new_preamble = preamble[:insert_at] + rendered + preamble[insert_at:]
    else:
        new_preamble = preamble

    with open(spec_file, "w") as handle:
        handle.writelines(new_preamble + lines[description_index:])


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <spec_file> <pypi_name> <version>", file=sys.stderr)
        return 2

    spec_file, pypi_name, version = sys.argv[1], sys.argv[2], sys.argv[3]
    try:
        new_requires = pypi_mandatory_deps(pypi_name, version)
        rewrite_requires(spec_file, new_requires)
    except (MetadataError, UnsafeSpecError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if new_requires:
        print(f"Updated Requires in {spec_file}: {', '.join(new_requires)}")
    else:
        print(f"Cleared main Python Requires in {spec_file}; PyPI declares none.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
