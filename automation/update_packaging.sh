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

if [[ -d /sys/fs/selinux ]]; then
  SELINUX_FLAG=":Z"
else
  SELINUX_FLAG=""
fi

podman run --rm --volume ${RESULT_DIR}:/app/packaging/${SELINUX_FLAG}  ${ENV_FILE_ARG} tfm-pulpcore-builder
