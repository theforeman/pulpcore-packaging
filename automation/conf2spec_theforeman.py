#!/usr/bin/env python3
"""Render a pyp2spec TOML config using the theforeman packaging template.

Usage:
    python3 automation/conf2spec_theforeman.py <pkg.conf> [-o <output.spec>]

Calls pyp2spec's config loading and helper functions, but renders with
automation/template.spec instead of pyp2spec's Fedora-oriented template.
The result follows theforeman/pulpcore-packaging conventions:
  - python%{python3_pkgversion}-* naming
  - %pyproject_buildrequires (no explicit Requires needed)
  - %pyproject_wheel / %pyproject_install
  - Release: 1%{?dist}, standard %changelog entry
"""

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path

from jinja2 import Template
from pyp2spec.conf2spec import (
    ConfigFile,
    archive_basename,
    convert_version_to_rpm_scheme,
    create_compat_name,
    get_license_string,
    list_additional_build_requires,
    load_config_file,
    python_version_or_macro,
    source,
)

TEMPLATE_PATH = Path(__file__).parent / "template.spec"


def _packager_string() -> str:
    """Return 'Full Name <email>' from git config, falling back to env."""
    try:
        name = subprocess.check_output(
            ["git", "config", "user.name"], text=True
        ).strip()
        email = subprocess.check_output(
            ["git", "config", "user.email"], text=True
        ).strip()
        return f"{name} <{email}>"
    except subprocess.CalledProcessError:
        return "Foreman Packaging Automation <packaging@theforeman.org>"


def render(conf_path: str) -> str:
    config = ConfigFile(load_config_file(conf_path))
    template = Template(TEMPLATE_PATH.read_text(encoding="utf-8"))

    version = config.get_string("version")
    name = config.get_string("name")
    compat = config.get_string("compat")
    top_level_modules = config.get_list("top_level_modules")
    scripts = config.get_list("scripts")
    license_str, license_notice = get_license_string(config)

    return template.render(
        additional_build_requires=list_additional_build_requires(config),
        archful=config.get_bool("archful"),
        archive_name=archive_basename(config, version),
        automode=config.get_bool("automode"),
        compat=compat,
        compat_name=create_compat_name(name, compat),
        extras=",".join(config.get_list("extras")),
        top_level_modules=" ".join(top_level_modules) if top_level_modules else None,
        license=license_str,
        license_notice=license_notice,
        mandate_license=config.get_bool("license_files_present"),
        name=name,
        python_compat_name=create_compat_name(config.get_string("python_name"), compat),
        pypi_version=python_version_or_macro(version),
        scripts=scripts,
        source=source(config),
        summary=config.get_string("summary"),
        url=config.get_string("url"),
        version=convert_version_to_rpm_scheme(version),
        changelog_date=datetime.now().strftime("%a %b %d %Y"),
        changelog_packager=_packager_string(),
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("conf", help="pyp2spec TOML config file")
    parser.add_argument("-o", "--output", help="Output spec file path")
    args = parser.parse_args()

    spec_content = render(args.conf)

    if args.output:
        Path(args.output).write_text(spec_content, encoding="utf-8")
        print(f"Spec written to {args.output}")
    else:
        sys.stdout.write(spec_content)


if __name__ == "__main__":
    main()
