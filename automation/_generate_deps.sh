#!/bin/bash

set -e

PULPCORE_REQUIREMENTS="/app/requirements.txt"
PULPCORE_FULL_REQUIREMENTS="/app/pulpcore-requirements.txt"
PACKAGING_WORKDIR="/app/packaging"
FOREMAN_PACKAGING="${PACKAGING_WORKDIR}/foreman"
FOREMAN_PACKAGING_GIT="https://github.com/theforeman/foreman-packaging"
FOREMAN_PACKAGING_BRANCH="rpm/develop"
PULPCORE_PACKAGING="${PACKAGING_WORKDIR}/pulpcore"
PULPCORE_PACKAGING_GIT="https://github.com/theforeman/pulpcore-packaging"
PULPCORE_PACKAGING_BRANCH="rpm/3.16"
PULPCORE_TAG="katello-pulpcore-nightly-el7"

pip3 install scikit-build
pip3 install -r $PULPCORE_REQUIREMENTS
pip3 freeze |sed '/gobject/d; /scikit/d; /libcomps/d; /solv/d; /createrepo/d; /distro/d; /^ansible/d' > $PULPCORE_FULL_REQUIREMENTS

pip3 install git+https://github.com/evgeni/pyp2rpm.git@foreman#egg=pyp2rpm
pip3 install spec2scl

if [ -d $PACKAGING_WORKDIR ]; then

  git clone --branch $FOREMAN_PACKAGING_BRANCH $FOREMAN_PACKAGING_GIT $FOREMAN_PACKAGING
  git clone --branch $PULPCORE_PACKAGING_BRANCH $PULPCORE_PACKAGING_GIT $PULPCORE_PACKAGING

  pushd $PULPCORE_PACKAGING

  git config --local user.email "${EMAIL:-root@localhost}"
  git config --local user.name "${NAME:-root}"
  export RPM_PACKAGER="${NAME}"

  while read line; do
    pkg=${line%==*}
    version=${line#*==}
    REWRITE_ON_SAME_VERSION=false $FOREMAN_PACKAGING/add_pypi_package.sh ${pkg} ${version} $PULPCORE_TAG '/' $PULPCORE_PACKAGING/pyp2rpm/pulpcore.spec
    # don't hit pypi.org too hard, it sometimes decides to ratelimit us
    sleep 5
  done < $PULPCORE_FULL_REQUIREMENTS

  popd
fi
