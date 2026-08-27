#!/usr/bin/env python3

import subprocess
import sys
import re
import glob

PACKAGES_DIR = "packages"


def canonicalize(name):
    """PEP 503 style canonicalization: lowercase, collapse runs of -_. into a single '-'.

    Used to match PyPI project names (which may use '-', '_' or '.' inconsistently,
    e.g. 'ruamel.yaml', 'poetry_core', 'opentelemetry-api') against the on-disk spec
    directory suffix for the same package, regardless of which separator style either
    side happens to use.
    """
    return re.sub(r"[-_.]+", "-", name).lower()


def strip_python_prefix(name):
    """Strip a single leading 'python-' from a PyPI project name.

    Some PyPI projects (python-socks, python-dateutil, python-debian, ...) already
    include this prefix in their own name, on top of the 'python-' prefix every spec
    directory in this repo uses. Stripping it here means both cases resolve the same
    way against the directory index below.
    """
    if name.lower().startswith("python-"):
        return name[len("python-"):]
    return name


def build_directory_index(packages_dir=PACKAGES_DIR):
    """Map canonical package name -> actual on-disk spec directory suffix.

    Every RPM-packaged python library lives at packages/python-<suffix>/python-<suffix>.spec.
    <suffix> doesn't always match the PyPI project name's separator style (e.g. the directory
    suffix is 'poetry_core' while the PyPI project is 'poetry-core', or 'et-xmlfile' while the
    PyPI project is 'et_xmlfile'). Building this index from the actual directories on disk means
    every current and future package resolves correctly without a hand-maintained mapping table.
    """
    index = {}
    for spec_path in glob.glob(f"{packages_dir}/python-*/python-*.spec"):
        dir_name = spec_path.split("/")[-2]
        suffix = dir_name[len("python-"):]
        index[canonicalize(suffix)] = suffix
    return index


def resolve_package_dir(pkg, directory_index=None):
    """Resolve a PyPI package name to its on-disk spec directory suffix, if packaged."""
    if directory_index is None:
        directory_index = build_directory_index()
    base = strip_python_prefix(pkg)
    return directory_index.get(canonicalize(base))


def parse_package_list(lines):
    for line in lines:
        line = line.strip()
        if line:
            name, version = line.split("==")
            yield {"package_name": name, "new_version": version}


def find_packages(pkg, new_version):
    dir_pkg_name = resolve_package_dir(pkg)

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


def build_package_list(file_handle):
    for line in file_handle:
        pkg_info = line.strip().split()
        if len(pkg_info) != 2:
            print(f"Invalid entry in list: {line.strip()}")
            continue

        pkg, new_version = pkg_info
        find_packages(pkg, new_version)


def main():
    packages = list(parse_package_list(sys.stdin.readlines()))

    for package in packages:
        find_packages(package["package_name"], package["new_version"])


if __name__ == "__main__":
    main()
