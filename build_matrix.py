#!/usr/bin/env python3

import json
import os
import sys


def parse_package_list(lines):
    for line in lines:
        line = line.strip()
        if line:
            name, version = line.split('==')
            yield {'package_name': name, 'new_version': version}


def main():
    packages = list(parse_package_list(sys.stdin.readlines()))

    if 'GITHUB_OUTPUT' in os.environ:
        with open(os.environ['GITHUB_OUTPUT'], 'a') as github_output:
            print(f'matrix={json.dumps(packages)}', file=github_output)

    for package in packages:
        print(package['package_name'], package['new_version'])

if __name__ == '__main__':
    main()
