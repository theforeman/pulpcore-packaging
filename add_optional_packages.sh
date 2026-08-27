#!/bin/bash

echo "django-storages[boto3,google,s3,azure]" >> automation/requirements.txt
# pulpcore only requires plain "psycopg" (we strip its own [binary] extra in the
# spec), so request the [c] extra explicitly here to make psycopg-c discoverable
# by find_package.py too -- it's a separately packaged/versioned companion RPM.
echo "psycopg[c]" >> automation/requirements.txt
# Foreman only supports PostgreSQL 13, which Django 5.x dropped. Pin to 4.2 LTS.
# Switch only if Foreman supports a newer PostgreSQL version.
echo "Django~=4.2.0" >> automation/requirements.txt
