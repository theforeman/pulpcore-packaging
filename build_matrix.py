#!/usr/bin/env python3

import json
import os
import sys

from find_package import parse_package_list


def main():
    packages = list(parse_package_list(sys.stdin.readlines()))

    if 'GITHUB_OUTPUT' in os.environ:
        with open(os.environ['GITHUB_OUTPUT'], 'a') as github_output:
            print(f'matrix={json.dumps(packages)}', file=github_output)

    for package in packages:
        print(package['package_name'], package['new_version'])

if __name__ == '__main__':
    main()
