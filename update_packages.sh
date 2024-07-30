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
    #Set the Spec path with the pkg name
    SPEC_FILE="packages/python-$pkg/python-$pkg.spec"
    # Store the packaged version of the lib
    rpm_version=$(rpmspec -q --queryformat='%{version}' packages/python-"$pkg"/python-"$pkg".spec --srpm)
    # Diff the new version and the packaged version
    rpmdev-vercmp "$rpm_version" "$NEW_VERSION"
    # Stores the exit_code from vercmp
    exit_code=$?
    if [ 12 -eq $exit_code ];
    then
        echo "RPM for Package $pkg needs to be updated from $rpm_version to $NEW_VERSION"
        TARBALL_TO_REMOVE=$(spectool --list-files "$SPEC_FILE" | cut -d' ' -f2 | grep http | xargs --no-run-if-empty -n 1 basename)
        git rm packages/python-"$pkg"/"$TARBALL_TO_REMOVE"
        rpmdev-bumpspec --comment "- Update to ${NEW_VERSION}" --new "${NEW_VR}" "$SPEC_FILE"
        git add "$SPEC_FILE"
        spectool --get-files "$SPEC_FILE" -C packages/python-"$pkg"
        TARBALL_ADDED=$(spectool --list-files "$SPEC_FILE" | cut -d' ' -f2 | grep http | xargs --no-run-if-empty -n 1 basename)
        git annex add packages/python-"$pkg"/"$TARBALL_ADDED"
    fi

    if [ 0 -eq $exit_code ];
    then
        echo "Package $pkg version is the same as the packaged RPM"
        exit 0
    fi

    if [ 11 -eq $exit_code ];
    then
        echo "Packaged $pkg RPM is newer than version in requirements"
        exit 0
    fi

}

bump_spec "$@"
