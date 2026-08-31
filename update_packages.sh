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

    #Set pkg with the 1st argument from cli
    pkg=$1
    #Set NEW_VERSION with the 2nd argument from cli
    NEW_VERSION=$2
    NEW_VR=$NEW_VERSION

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
    # Stores the exit_code from vercmp
    exit_code=$?
    if [ 12 -eq $exit_code ];
    then
        echo "RPM for Package $PKG_DIR needs to be updated from $rpm_version to $NEW_VERSION"
        TARBALL_TO_REMOVE=$(spectool --list-files "$SPEC_FILE" | cut -d' ' -f2 | grep http | xargs --no-run-if-empty -n 1 basename)
        git rm "packages/$PKG_DIR/$TARBALL_TO_REMOVE"
        rpmdev-bumpspec --comment "- Update to ${NEW_VERSION}" --new "${NEW_VR}" "$SPEC_FILE"
        git add "$SPEC_FILE"
        spectool --get-files "$SPEC_FILE" -C "packages/$PKG_DIR"
        TARBALL_ADDED=$(spectool --list-files "$SPEC_FILE" | cut -d' ' -f2 | grep http | xargs --no-run-if-empty -n 1 basename)
        git annex add "packages/$PKG_DIR/$TARBALL_ADDED"

        # Regenerate Requires from PyPI metadata (stdlib urllib only, no extra deps)
        python3 automation/update_deps.py "$SPEC_FILE" "$pkg" "$NEW_VERSION" && git add "$SPEC_FILE"
    fi

    if [ 0 -eq $exit_code ];
    then
        echo "Package $PKG_DIR version is the same as the packaged RPM"
        exit 0
    fi

    if [ 11 -eq $exit_code ];
    then
        echo "Packaged $PKG_DIR RPM is newer than version in requirements"
        exit 0
    fi

}

bump_spec "$@"
