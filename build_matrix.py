#!/usr/bin/env python3

import json
import os
import sys

from find_package import canonicalize, parse_package_list

# This script intentionally does NOT route through resolve_package_dir().
# update-pulp-packages.yml is scoped only to packages in automation/requirements.txt
# (pulpcore + official pulp plugins) — it must not trigger broad package discovery.
# update_packages.sh calls find_package.py --resolve-dir at runtime to resolve each
# raw PyPI name to its on-disk directory suffix, handling separator/prefix mismatches.


def main():
    packages = list(parse_package_list(sys.stdin.readlines()))

    # Normalize package names so separator mismatches (ruamel.yaml → ruamel-yaml) don't
    # produce malformed branch names or spec paths downstream.
    for p in packages:
        p["package_name"] = canonicalize(p["package_name"])

    if 'GITHUB_OUTPUT' in os.environ:
        with open(os.environ['GITHUB_OUTPUT'], 'a') as github_output:
            print(f'matrix={json.dumps(packages)}', file=github_output)

    for package in packages:
        print(package['package_name'], package['new_version'])

if __name__ == '__main__':
    main()
