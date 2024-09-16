#!/bin/bash

pip3.11 freeze | sed '/^gobject/d; /subprocess-tee/d; /rpds-py/d; /referencing/d; /scikit/d; /libcomps/d; /mailbits/d; /markdown-it-py/d; /psycopg-binary/d; /mypy-extensions/d; /black/d; /chardet/d; /mdurl/d; /solv/d; /createrepo/d; /distro/d; /^ansible/d; /^jsonschema/d; /^pulp/d; /^yamllint/d;'
