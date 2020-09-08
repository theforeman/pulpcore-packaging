#!/bin/bash

set -e

RESULT_DIR="$(pwd)/packaging"
ENV_FILE="packaging.env"

mkdir -p ${RESULT_DIR}

if [[ -f ${ENV_FILE} ]]; then
  ENV_FILE_ARG="--env-file ${ENV_FILE}"
else
  ENV_FILE_ARG=""
fi

podman run --rm --volume ${RESULT_DIR}:/app/packaging/:Z  ${ENV_FILE_ARG} tfm-pulpcore-builder
