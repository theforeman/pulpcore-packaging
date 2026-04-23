#!/bin/bash

echo "django-storages[boto3,google,s3,azure]" >> automation/requirements.txt
# psycopg 3.3.x dropped setup.py and requires setuptools >= 80.3.1 to build the C extension.
# RHEL 9 only ships setuptools 68.x. Pin to 3.2.x until a build fix is available.
echo "psycopg[c]~=3.2.0" >> automation/requirements.txt
# Foreman only supports PostgreSQL 13, which Django 5.x dropped. Pin to 4.2 LTS.
# Switch only if Foreman supports a newer PostgreSQL version.
echo "Django~=4.2.0" >> automation/requirements.txt
