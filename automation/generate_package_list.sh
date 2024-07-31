#!/bin/bash

PULPCORE_REQUIREMENTS="/app/requirements.txt"
PULPCORE_FULL_REQUIREMENTS="/app/pulpcore-requirements.txt"

pip3.11 install -r $PULPCORE_REQUIREMENTS

pip3.11 freeze | sed '/gobject/d; /scikit/d; /libcomps/d; /solv/d; /createrepo/d; /distro/d; /^ansible/d; /^jsonschema/d; /^pulp/d;' > $PULPCORE_FULL_REQUIREMENTS
