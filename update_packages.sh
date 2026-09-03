#!/bin/bash
set +e

ensure_program() {
	package=${2:-$1}
	if ! (program_exists "$1"); then
		echo "$1 is not installed - you can install it with"
		echo "sudo yum install $package"
		exit 1
	fi
}

program_exists() {
	which "$@" &> /dev/null
}

ensure_program rpmspec rpm-build

bump_spec() {

    pkg=$1
    NEW_VERSION=$2

    # Resolve PyPI name → on-disk directory (handles separator/prefix mismatches like ruamel.yaml)
    PKG_DIR=$(python3 find_package.py --resolve-dir "$pkg") || {
        echo "ERROR: cannot resolve '$pkg' to any packages/python-*/ directory" >&2
        exit 1
    }
    SPEC_FILE="packages/$PKG_DIR/$PKG_DIR.spec"
    # Store the packaged version of the lib; fail loudly if spec is missing or malformed
    rpm_version=$(rpmspec -q --queryformat='%{version}' "$SPEC_FILE" --srpm) || {
        echo "ERROR: rpmspec failed on $SPEC_FILE" >&2
        exit 1
    }
    [ -n "$rpm_version" ] || {
        echo "ERROR: rpmspec returned empty version for $SPEC_FILE" >&2
        exit 1
    }

    # Diff the new version and the packaged version
    rpmdev-vercmp "$rpm_version" "$NEW_VERSION"
    exit_code=$?

    if [ 12 -eq $exit_code ]; then
        echo "RPM for Package $PKG_DIR needs to be updated from $rpm_version to $NEW_VERSION"

        # Remove old tarball from git-annex
        TARBALL_TO_REMOVE=$(spectool --list-files "$SPEC_FILE" | cut -d' ' -f2 | grep http | xargs --no-run-if-empty -n 1 basename)
        git rm "packages/$PKG_DIR/$TARBALL_TO_REMOVE"

        # Existing specs are the source of truth for RHEL/CentOS packaging policy.
        # Never regenerate them with pyp2spec: it cannot preserve Sources, patches,
        # macros, conditional dependencies, vendored crates, or manual %files lists.
        _bump_in_place "$SPEC_FILE" "$NEW_VERSION" || exit 1
        if grep -qE 'rust-toolset|%cargo_prep' "$SPEC_FILE"; then
            echo "Rust package detected — vendor tarball must be regenerated manually" >&2
        fi

        # Fetch new tarball and track via git-annex
        spectool --get-files "$SPEC_FILE" -C "packages/$PKG_DIR"
        TARBALL_ADDED=$(spectool --list-files "$SPEC_FILE" | cut -d' ' -f2 | grep http | xargs --no-run-if-empty -n 1 basename)
        git annex add "packages/$PKG_DIR/$TARBALL_ADDED"
    fi

    if [ 0 -eq $exit_code ]; then
        echo "Package $PKG_DIR version is the same as the packaged RPM"
        exit 0
    fi

    if [ 11 -eq $exit_code ]; then
        echo "Packaged $PKG_DIR RPM is newer than version in requirements"
        exit 0
    fi
}

_bump_in_place() {
    local spec_file="$1"
    local new_version="$2"
    if ! rpmdev-bumpspec --comment "- Update to ${new_version}" --new "${new_version}" "$spec_file"; then
        echo "ERROR: rpmdev-bumpspec failed for $pkg $new_version" >&2
        return 1
    fi
    if python3 automation/update_deps.py "$spec_file" "$pkg" "$new_version"; then
        git add "$spec_file"
    else
        echo "ERROR: update_deps.py failed for $pkg $new_version" >&2
        return 1
    fi
}

bump_spec "$@"
