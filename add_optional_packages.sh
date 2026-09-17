#!/bin/bash

echo "django-storages[boto3,google,s3,azure]" >> automation/requirements.txt
# pulpcore only requires plain "psycopg" (we strip its own [binary] extra in the
# spec), so request the [c] extra explicitly here to make psycopg-c discoverable
# by find_package.py too -- it's a separately packaged/versioned companion RPM.
echo "psycopg[c]" >> automation/requirements.txt
