#!/usr/bin/env python3

import subprocess
import sys
import json
import os

def parse_package_list(lines):
    # Define transformation rules for better maintainability
    
    # Packages that need prefix removal
    prefix_removals = {
        'python-': ''
    }
    
    # Specific package name mappings (exact matches)
    package_mappings = {
        'typing_extensions': 'typing-extensions',
        'galaxy_importer': 'galaxy-importer',
        'psycopg-c': 'psycopg_c',
        'importlib_resources': 'importlib-resources',
        'ruamel.yaml': 'ruamel-yaml',
        'ruamel.yaml.clib': 'ruamel-yaml-clib',
        'jaraco.classes': 'jaraco-classes',
        'et_xmlfile': 'et-xmlfile',
        'aiohttp_socks': 'aiohttp-socks',
        'pyasn1_modules': 'pyasn1-modules',
        'pydantic_core': 'pydantic-core',
        'flit_core': 'flit-core',
        'poetry_core': 'poetry-core',
        'poetry_plugin_export': 'poetry-plugin-export',
    }
    
    # Packages that need to be lowercased
    lowercase_packages = {
        'PyYAML': 'pyyaml',
        'GitPython': 'gitpython', 
        'Deprecated': 'deprecated',
        'CacheControl': 'cachecontrol',
        'Django': 'django',
        'Jinja2': 'jinja2',
        'MarkupPy': 'markuppy',
        'MarkupSafe': 'markupsafe',
        'Parsley': 'parsley',
        'PyGObject': 'pygobject',
        'Pygments': 'pygments',
        'PyJWT': 'pyjwt',
        'RapidFuzz': 'rapidfuzz',
        'SecretStorage': 'secretstorage',
    }
    
    # Pattern-based transformations
    def apply_pattern_transformations(name):
        # OpenTelemetry packages: replace - with _
        if name.startswith('opentelemetry'):
            return name.replace('-', '_')
        # Poetry packages: only transform the main poetry package and core packages with underscores
        elif name == 'poetry' or (name.startswith('poetry') and '_' in name):
            return name.replace('-', '_')
        # Flit packages: replace _ with -
        elif name.startswith('flit') and '_' in name:
            return name.replace('_', '-')
        # ET packages: replace _ with -
        elif name.startswith('et') and '_' in name:
            return name.replace('_', '-')
        # AioHTTP packages: replace _ with -
        elif name.startswith('aiohttp') and '_' in name:
            return name.replace('_', '-')
        # PyASN1 packages: replace _ with -
        elif name.startswith('pyasn1') and '_' in name:
            return name.replace('_', '-')
        # Jaraco packages: replace . with -
        elif name.startswith('jaraco') and '.' in name:
            return name.replace('.', '-')
        # Pydantic packages: replace _ with -
        elif name.startswith('pydantic') and '_' in name:
            return name.replace('_', '-')
        # Ruamel packages: replace . with -
        elif name.startswith('ruamel') and '.' in name:
            return name.replace('.', '-')
        # Default: no transformation
        return name
    
    for line in lines:
        line = line.strip()
        if line:
            name, version = line.split('==')
            
            # Apply prefix removals first
            for prefix, replacement in prefix_removals.items():
                if name.startswith(prefix):
                    name = name.replace(prefix, replacement, 1)
                    break
            
            # Apply specific package mappings
            if name in package_mappings:
                name = package_mappings[name]
            # Apply lowercase mappings
            elif name in lowercase_packages:
                name = lowercase_packages[name]
            # Apply pattern-based transformations
            else:
                name = apply_pattern_transformations(name)
            
            yield {'package_name': name, 'new_version': version}

def find_packages(pkg, new_version):
    # Create reverse mapping to find the original package name for directory lookup
    reverse_mappings = {
        'poetry-core': 'poetry_core',
        'poetry-plugin-export': 'poetry_plugin_export',
        'galaxy-importer': 'galaxy_importer',
        'importlib-resources': 'importlib_resources',
        'ruamel-yaml': 'ruamel.yaml',
        'ruamel-yaml-clib': 'ruamel.yaml.clib',
        'jaraco-classes': 'jaraco.classes',
        'et-xmlfile': 'et_xmlfile',
        'aiohttp-socks': 'aiohttp_socks',
        'pyasn1-modules': 'pyasn1_modules',
    }
    
    # Use original package name for directory lookup if it exists in reverse mapping
    dir_pkg_name = reverse_mappings.get(pkg, pkg)
    
    # Set paths and file names
    spec_file = f"packages/python-{dir_pkg_name}/python-{dir_pkg_name}.spec"

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
