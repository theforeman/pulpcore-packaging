#!/usr/bin/env python3

import subprocess
import sys
import json
import os

def parse_package_list(lines):
    for line in lines:
        line = line.strip()
        if line:
            name, version = line.split('==')
            # Opentelemetry packages have _ on pypi
            if name.startswith('opentelemetry'):
                name = name.replace('-', '_')
            # debian, dateutil, gnugg and sockes starts with python-
            # and that breaks my wonky update_packages script
            elif name.startswith('python-'):
                name = name.replace('python-', '', 1)
            elif name.startswith('typing_extensions'):
                name = name.replace('_', '-')
            elif name.startswith('ruamel'):
                name = name.replace('.', '-')
            elif name.startswith('galaxy_importer'):
                name = name.replace('_', '-')
            #Lower Case all libs that needs to be lowercased(is this a verb?)
            elif name.startswith('PyYAML'):
                name = name.lower()
            elif name.startswith('GitPython'):
                name = name.lower()
            elif name.startswith('Deprecated'):
                name = name.lower()
            elif name.startswith('Django'):
                name = name.lower()
            elif name.startswith('Jinja2'):
                name = name.lower()
            elif name.startswith('Mark'):
                name = name.lower()
            elif name.startswith('Parsley'):
                name = name.lower()
            elif name.startswith('PyGObject'):
                name = name.lower()
            elif name.startswith('Pygments'):
                name = name.lower()
            elif name.startswith('PyJWT'):
                name = name.lower()
            yield {'package_name': name, 'new_version': version}

def find_packages(pkg, new_version):
    # Set paths and file names
    spec_file = f"packages/python-{pkg}/python-{pkg}.spec"

    # Retrieve the current RPM version from the spec file
    try:
        rpm_version_cmd = ["rpmspec", "-q", "--queryformat=%{version}", spec_file, "--srpm"]
        rpm_version = subprocess.check_output(rpm_version_cmd).decode().strip()
    except subprocess.CalledProcessError:
        print(f"Spec file not found for package {pkg}")
        return

    # Compare versions using rpmdev-vercmp
    vercmp_cmd = ["rpmdev-vercmp", rpm_version, new_version]
    exit_code = subprocess.run(vercmp_cmd).returncode

    if exit_code == 12:
        print(f"RPM for Package {pkg} needs to be updated from {rpm_version} to {new_version}")
        with open("packages-to-update.txt", "a") as file:
            file.write(f"{pkg} {new_version}\n")
    elif exit_code == 0:
        print(f"Package {pkg} version is the same as the packaged RPM")
    elif exit_code == 11:
        print(f"Packaged {pkg} RPM is newer than the version in requirements")

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
        find_packages(package['package_name'], package['new_version'])
        

if __name__ == '__main__':
    main()
