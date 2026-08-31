#!/bin/bash
# scaffold_package.sh <pypi_name> [<version>]
#
# Scaffold a new RPM spec for a PyPI package using pyp2spec's two-phase pipeline:
#   1. pyp2conf  — gathers PyPI metadata into a TOML config
#   2. conf2spec_theforeman.py — renders spec using our packaging conventions
#
# Creates packages/python-<normalized-name>/ with spec + source tarball.
# Review summary, %description, and %check before opening a PR.
set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Usage: $0 <pypi_name> [<version>]" >&2
    exit 1
fi

PYPI_NAME="$1"
VERSION="${2:-}"

# PEP-503 canonicalization: collapse runs of -_. into -
CANONICAL=$(python3 -c "import re,sys; print(re.sub(r'[-_.]+', '-', sys.argv[1]).lower())" "$PYPI_NAME")
PKG_DIR="packages/python-${CANONICAL}"
SPEC_FILE="${PKG_DIR}/python-${CANONICAL}.spec"
CONF_FILE="${PKG_DIR}/python-${CANONICAL}.conf"

if [ -d "$PKG_DIR" ]; then
    echo "ERROR: $PKG_DIR already exists. Use update_packages.sh to bump the version." >&2
    exit 1
fi

if ! command -v pyp2conf &> /dev/null; then
    echo "ERROR: pyp2spec is not installed. Install with: pip install pyp2spec" >&2
    exit 1
fi

echo "Gathering PyPI metadata for ${PYPI_NAME}${VERSION:+==${VERSION}} → ${CONF_FILE}"
mkdir -p "$PKG_DIR"

# Phase 1: pyp2conf — gather metadata into TOML
if [ -n "$VERSION" ]; then
    pyp2conf -a -v "$VERSION" "$PYPI_NAME" -c "$CONF_FILE"
else
    pyp2conf -a "$PYPI_NAME" -c "$CONF_FILE"
fi

if [ ! -f "$CONF_FILE" ]; then
    echo "ERROR: pyp2conf did not produce ${CONF_FILE}" >&2
    rm -rf "$PKG_DIR"
    exit 1
fi

# Phase 2: conf2spec_theforeman — render spec using our template
python3 "$(dirname "$0")/automation/conf2spec_theforeman.py" "$CONF_FILE" -o "$SPEC_FILE"

if [ ! -f "$SPEC_FILE" ]; then
    echo "ERROR: conf2spec_theforeman.py did not produce ${SPEC_FILE}" >&2
    rm -rf "$PKG_DIR"
    exit 1
fi

# Fetch source tarball and add via git-annex
spectool --get-files "$SPEC_FILE" -C "$PKG_DIR"
TARBALL=$(spectool --list-files "$SPEC_FILE" \
    | cut -d' ' -f2 | grep http | xargs --no-run-if-empty -n 1 basename)
if [ -n "$TARBALL" ] && [ -f "${PKG_DIR}/${TARBALL}" ]; then
    git annex add "${PKG_DIR}/${TARBALL}"
fi

git add "$SPEC_FILE" "$CONF_FILE"

echo ""
echo "Scaffolded: ${SPEC_FILE}"
echo ""
echo "TODO before opening a PR:"
echo "  - Review %description (uses PyPI summary, may need rewording)"
echo "  - Verify License: tag matches the actual SPDX expression"
echo "  - Add a %check section if the package ships a test suite"
echo "  - Run: obal scratch python-${CANONICAL}"
