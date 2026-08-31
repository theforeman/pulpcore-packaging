#!/usr/bin/env python3

import subprocess
import sys
import re
import glob

PACKAGES_DIR = "packages"
PYTHON_PREFIX = "python-"


def canonicalize(name):
    """PEP 503 style canonicalization: lowercase, collapse runs of -_. into a single '-'.

    Used to match PyPI project names (which may use '-', '_' or '.' inconsistently,
    e.g. 'ruamel.yaml', 'poetry_core', 'opentelemetry-api') against the on-disk spec
    directory suffix for the same package, regardless of which separator style either
    side happens to use. Applied before any prefix stripping, since pip freeze can emit
    either 'python-socks' or 'python_socks' for the same project.
    """
    return re.sub(r"[-_.]+", "-", name).lower()


def build_directory_index(packages_dir=PACKAGES_DIR):
    """Map canonical package name -> actual on-disk spec directory suffix.

    Every RPM-packaged python library lives at packages/python-<suffix>/python-<suffix>.spec.
    <suffix> doesn't always match the PyPI project name's separator style (e.g. the directory
    suffix is 'poetry_core' while the PyPI project is 'poetry-core', or 'et-xmlfile' while the
    PyPI project is 'et_xmlfile'). Building this index from the actual directories on disk means
    every current and future package resolves correctly without a hand-maintained mapping table.

    Raises if two directories canonicalize to the same key: that would make resolution
    filesystem-order-dependent, and this repo has renamed directories between separator
    styles before (galaxy_importer -> galaxy-importer, importlib_resources -> importlib-resources).
    """
    index = {}
    for spec_path in sorted(glob.glob(f"{packages_dir}/python-*/python-*.spec")):
        dir_name = spec_path.split("/")[-2]
        suffix = dir_name[len(PYTHON_PREFIX):]
        key = canonicalize(suffix)
        if key in index and index[key] != suffix:
            raise ValueError(
                f"Ambiguous package directory: '{index[key]}' and '{suffix}' both canonicalize to '{key}'"
            )
        index[key] = suffix
    return index


def resolve_package_dir(pkg, directory_index=None):
    """Resolve a PyPI package name to its on-disk spec directory suffix, if packaged.

    Tries an exact canonical match first, since a handful of PyPI projects (e.g. 'gnupg'
    and 'python-gnupg') are genuinely distinct packages that happen to differ only by a
    'python-' prefix -- stripping the prefix unconditionally would collapse them onto the
    same directory. Only if there's no exact match do we fall back to stripping a leading
    'python-' from the canonical form, for projects (python-socks, python-dateutil, ...)
    that bundle this repo's own directory-naming prefix into their PyPI name.
    """
    if directory_index is None:
        directory_index = build_directory_index()

    canonical_pkg = canonicalize(pkg)

    if canonical_pkg in directory_index:
        return directory_index[canonical_pkg]

    if canonical_pkg.startswith(PYTHON_PREFIX):
        stripped = canonical_pkg[len(PYTHON_PREFIX):]
        if stripped in directory_index:
            return directory_index[stripped]

    return None


def parse_package_list(lines):
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if "==" not in line:
            print(f"Skipping unparseable requirements line: {line}")
            continue
        name, version = line.split("==")
        yield {"package_name": name, "new_version": version}


def find_packages(pkg, new_version, directory_index=None):
    dir_pkg_name = resolve_package_dir(pkg, directory_index)

    if dir_pkg_name is None:
        print(f"Spec file not found for package {pkg} (no packages/python-* directory matches)")
        return

    spec_file = f"{PACKAGES_DIR}/python-{dir_pkg_name}/python-{dir_pkg_name}.spec"

    # Retrieve the current RPM version from the spec file
    try:
        rpm_version_cmd = ["rpmspec", "-q", "--queryformat=%{version}", spec_file, "--srpm"]
        rpm_version = subprocess.check_output(rpm_version_cmd).decode().strip()
    except subprocess.CalledProcessError:
        print(f"Spec file not found for package {pkg} (looked for {spec_file})")
        return

    # Compare versions using rpmdev-vercmp
    vercmp_cmd = ["rpmdev-vercmp", rpm_version, new_version]
    exit_code = subprocess.run(vercmp_cmd).returncode

    # The resolved directory suffix (not the raw PyPI name) is what downstream tooling
    # (update_packages.sh, PR title/branch name) expects, since it builds spec paths the
    # same naive "packages/python-$pkg/python-$pkg.spec" way without re-resolving names.
    if exit_code == 12:
        print(f"RPM for Package {dir_pkg_name} needs to be updated from {rpm_version} to {new_version}")
        with open("packages-to-update.txt", "a") as file:
            file.write(f"{dir_pkg_name} {new_version}\n")
    elif exit_code == 0:
        print(f"Package {dir_pkg_name} version is the same as the packaged RPM")
    elif exit_code == 11:
        print(f"Packaged {dir_pkg_name} RPM is newer than the version in requirements")


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "--resolve-dir":
        pkg = sys.argv[2]
        directory_index = build_directory_index()
        if not directory_index:
            sys.exit(
                f"No package directories found under '{PACKAGES_DIR}/python-*/'. "
                "Run this script from the repository root."
            )
        suffix = resolve_package_dir(pkg, directory_index)
        if suffix is None:
            print(
                f"ERROR: cannot resolve '{pkg}' to any packages/python-*/ directory",
                file=sys.stderr,
            )
            sys.exit(1)
        print(f"python-{suffix}")
        return

    packages = list(parse_package_list(sys.stdin.readlines()))
    directory_index = build_directory_index()

    if not directory_index:
        sys.exit(
            f"No package directories found under '{PACKAGES_DIR}/python-*/'. "
            "Run this script from the repository root."
        )

    for package in packages:
        find_packages(package["package_name"], package["new_version"], directory_index)


if __name__ == "__main__":
    main()
