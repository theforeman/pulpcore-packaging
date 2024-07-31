#!/usr/bin/env python3


import json

def parse_package_list(file_path, output_path):
    packages = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                name, version = line.split('==')
                packages.append({'package_name': name, 'new_version': version})
    with open(output_path, 'w') as json_file:
        json.dump(packages, json_file, indent=4)

# Specify the path for package list file and output JSON file
file_path = 'package_list.txt'
output_path = 'packages.json'
parse_package_list(file_path, output_path)
