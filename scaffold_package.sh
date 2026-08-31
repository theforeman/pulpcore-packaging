#!/bin/bash
# scaffold_package.sh <pypi_name> [<version>]
#
# Scaffold a new RPM spec for a PyPI package using pyp2spec.
# Creates packages/python-<normalized-name>/ with spec + source tarball.
# Review license, summary, %description, and %check before opening a PR.
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

if [ -d "$PKG_DIR" ]; then
    echo "ERROR: $PKG_DIR already exists. Use update_packages.sh to bump the version." >&2
    exit 1
fi

if ! command -v pyp2spec &> /dev/null; then
    echo "ERROR: pyp2spec is not installed. Install with: pip install pyp2spec" >&2
    exit 1
fi

# Build pyp2spec argument
if [ -n "$VERSION" ]; then
    PKG_SPEC="${PYPI_NAME}==${VERSION}"
else
    PKG_SPEC="${PYPI_NAME}"
fi

echo "Generating spec for ${PKG_SPEC} → ${PKG_DIR}/"
mkdir -p "$PKG_DIR"

# Run pyp2spec in automode; output spec file to the package directory
pyp2spec -a "$PKG_SPEC" -o "${PKG_DIR}/python-${CANONICAL}.spec"

if [ ! -f "${PKG_DIR}/python-${CANONICAL}.spec" ]; then
    echo "ERROR: pyp2spec did not produce ${PKG_DIR}/python-${CANONICAL}.spec" >&2
    rmdir "$PKG_DIR"
    exit 1
fi

# Fetch source tarball and add via git-annex
spectool --get-files "${PKG_DIR}/python-${CANONICAL}.spec" -C "$PKG_DIR"
TARBALL=$(spectool --list-files "${PKG_DIR}/python-${CANONICAL}.spec" \
    | cut -d' ' -f2 | grep http | xargs --no-run-if-empty -n 1 basename)
if [ -n "$TARBALL" ] && [ -f "${PKG_DIR}/${TARBALL}" ]; then
    git annex add "${PKG_DIR}/${TARBALL}"
fi

git add "${PKG_DIR}/python-${CANONICAL}.spec"

echo ""
echo "Scaffolded: ${PKG_DIR}/python-${CANONICAL}.spec"
echo ""
echo "TODO before opening a PR:"
echo "  - Review %description (pyp2spec uses the PyPI summary, may need rewording)"
echo "  - Verify License: tag matches the actual SPDX expression"
echo "  - Add a %check section if the package ships a test suite"
echo "  - Confirm Requires/BuildRequires are complete"
echo "  - Run: obal scratch python-${CANONICAL}"
