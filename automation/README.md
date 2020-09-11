# pulpcore RPMs

This repository contains scripts and container files that can be used to add and update RPM packages for pulpcore to pulpcore-packaging.

The container is designed to be run against an empty directory, and produce a set of commits against `pulpcore-packaging` containing the generated packages.

## Dependencies

* podman, docker, or some other container runtime

## Configure

For the tools to work properly, you'll need to provide the container with your name and email address. The simplest way is to create a `packaging.env` file like this:
```
NAME=John Doe
EMAIL=john@example.org
```

The file can be later passed to the container runtime with `--env-file`. You can of course also use `--env` to specify the values of `NAME` and `EMAIL` directly.

## Execution

### Build

```
podman build --tag tfm-pulpcore-builder .
```

### Run

Execute `update_packaging.sh` which will do the following:

1. create an empty directory to host the resulting packages
2. check if there is an `packaging.env` file
3. pass the directory and optionally the `packaging.env` file to the container:
```
podman run --rm --volume $(pwd)/packaging/:/app/packaging/:Z  --env-file packaging.env tfm-pulpcore-builder
```
