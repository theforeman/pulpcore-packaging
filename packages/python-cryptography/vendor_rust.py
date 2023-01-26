#!/usr/bin/python3
"""Vendor PyCA cryptography's Rust crates
"""
import argparse
import os
import re
import tarfile
import tempfile
import shutil
import subprocess
import sys

VENDOR_DIR = "vendor"
CARGO_TOML = "src/rust/Cargo.toml"
RE_VERSION = re.compile("Version:\s*(.*)")

parser = argparse.ArgumentParser(description="Vendor Rust packages")
parser.add_argument(
    "--spec", default="python-cryptography.spec", help="cryptography source tar bundle"
)


def cargo(cmd, manifest):
    args = ["cargo", cmd, f"--manifest-path={manifest}"]
    return subprocess.check_call(
        args, stdout=subprocess.DEVNULL, stderr=sys.stderr, env={}
    )


def tar_reset(tarinfo):
    """Reset user, group, mtime, and mode to create reproducible tar"""
    tarinfo.uid = 0
    tarinfo.gid = 0
    tarinfo.uname = "root"
    tarinfo.gname = "root"
    tarinfo.mtime = 0
    if tarinfo.type == tarfile.DIRTYPE:
        tarinfo.mode = 0o755
    else:
        tarinfo.mode = 0o644
    if tarinfo.pax_headers:
        raise ValueError(tarinfo.name, tarinfo.pax_headers)
    return tarinfo


def tar_reproducible(tar, basedir):
    """Create reproducible tar file"""

    content = [basedir]
    for root, dirs, files in os.walk(basedir):
        for directory in dirs:
            content.append(os.path.join(root, directory))
        for filename in files:
            content.append(os.path.join(root, filename))
    content.sort()

    for fn in content:
        tar.add(fn, filter=tar_reset, recursive=False, arcname=fn)


def main():
    args = parser.parse_args()
    spec = args.spec

    # change cwd to work in bundle directory
    here = os.path.dirname(os.path.abspath(spec))
    os.chdir(here)

    # extract version number from bundle name
    with open(spec) as f:
        for line in f:
            mo = RE_VERSION.search(line)
            if mo is not None:
                version = mo.group(1)
                break
        else:
            raise ValueError(f"Cannot find version in {spec}")

    bundle_file = f"cryptography-{version}.tar.gz"
    vendor_file = f"cryptography-{version}-vendor.tar.gz"

    # remove existing vendor directory and file
    if os.path.isdir(VENDOR_DIR):
        shutil.rmtree(VENDOR_DIR)
    try:
        os.unlink(vendor_file)
    except FileNotFoundError:
        pass

    print(f"Getting crates for {bundle_file}", file=sys.stderr)

    # extract tar file in tempdir
    # fetch and vendor Rust crates
    with tempfile.TemporaryDirectory(dir=here) as tmp:
        with tarfile.open(bundle_file) as tar:
            tar.extractall(path=tmp)
        manifest = os.path.join(tmp, f"cryptography-{version}", CARGO_TOML)
        cargo("fetch", manifest)
        cargo("vendor", manifest)

    print("\nCreating tar ball...", file=sys.stderr)
    with tarfile.open(vendor_file, "x:gz") as tar:
        tar_reproducible(tar, VENDOR_DIR)

    # remove vendor dir
    shutil.rmtree(VENDOR_DIR)

    parser.exit(0, f"Created {vendor_file}\n")


if __name__ == "__main__":
    main()
