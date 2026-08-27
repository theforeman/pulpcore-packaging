#!/usr/bin/env python3

from find_package import build_directory_index, resolve_package_dir


def test_real_world_sample_data():
    """Resolve a real-world pip-freeze-style sample against the actual packages/ tree.

    Unlike testing parse_package_list() in isolation, this exercises the full path a name
    takes in production: PyPI project name -> on-disk spec directory suffix. That's the
    thing that broke for aiohttp-socks, galaxy-importer and importlib-resources (their
    hardcoded reverse-mapping entries pointed at directories that don't exist), and it's
    what this test would have caught.
    """
    # A subset of a real requirements freeze, covering every separator-mismatch style
    # (hyphen/underscore/dot, mixed case, PyPI names that already start with "python-").
    test_input = [
        "aiohttp-xmlrpc==1.5.0",
        "aiohttp_socks==0.10.1",
        "CacheControl==0.14.3",
        "Deprecated==1.2.18",
        "Django==4.2.23",
        "et_xmlfile==2.0.0",
        "flit_core==3.12.0",
        "galaxy_importer==0.4.31",
        "GitPython==3.1.44",
        "importlib_resources==6.4.5",
        "jaraco.classes==3.4.0",
        "Jinja2==3.1.6",
        "MarkupPy==1.18",
        "MarkupSafe==3.0.2",
        "opentelemetry-api==1.30.0",
        "opentelemetry-exporter-otlp-proto-common==1.30.0",
        "Parsley==1.3",
        "poetry-core==1.9.0",
        "poetry-plugin-export==1.8.0",
        "psycopg-c==3.2.9",
        "pyasn1_modules==0.4.2",
        "pydantic_core==2.33.2",
        "Pygments==2.19.2",
        "PyGObject==3.50.1",
        "PyJWT==2.10.1",
        "python-dateutil==2.9.0.post0",
        "python-debian==0.1.49",
        "python-gnupg==0.5.4",
        "python-socks==2.7.1",
        "PyYAML==6.0.2",
        "RapidFuzz==3.13.0",
        "ruamel.yaml==0.18.14",
        "ruamel.yaml.clib==0.2.12",
        "SecretStorage==3.3.3",
        "typing_extensions==4.14.1",
        "requests==2.32.4",
        "urllib3==2.5.0",
        "certifi==2025.6.15",
        "click==8.1.8",
        "attrs==22.2.0",
    ]

    index = build_directory_index()

    # Expected on-disk directory suffix for each PyPI name, reflecting the actual current
    # state of packages/ (not a "pretty" canonical form) -- this is what update_packages.sh
    # and the generated PR title/branch actually key off downstream.
    expected = {
        "aiohttp-xmlrpc": "aiohttp-xmlrpc",
        "aiohttp_socks": "aiohttp-socks",
        "CacheControl": "cachecontrol",
        "Deprecated": "deprecated",
        "Django": "django",
        "et_xmlfile": "et-xmlfile",
        "flit_core": "flit-core",
        "galaxy_importer": "galaxy-importer",
        "GitPython": "gitpython",
        "importlib_resources": "importlib-resources",
        "jaraco.classes": "jaraco-classes",
        "Jinja2": "jinja2",
        "MarkupPy": "markuppy",
        "MarkupSafe": "markupsafe",
        "opentelemetry-api": "opentelemetry_api",
        "opentelemetry-exporter-otlp-proto-common": "opentelemetry_exporter_otlp_proto_common",
        "Parsley": "parsley",
        "poetry-core": "poetry_core",
        "poetry-plugin-export": "poetry_plugin_export",
        "psycopg-c": "psycopg_c",
        "pyasn1_modules": "pyasn1-modules",
        "pydantic_core": "pydantic-core",
        "Pygments": "pygments",
        "PyGObject": "pygobject",
        "PyJWT": "pyjwt",
        "python-dateutil": "dateutil",
        "python-debian": "debian",
        "python-gnupg": "gnupg",
        "python-socks": "socks",
        "PyYAML": "pyyaml",
        "RapidFuzz": "rapidfuzz",
        "ruamel.yaml": "ruamel-yaml",
        "ruamel.yaml.clib": "ruamel-yaml-clib",
        "SecretStorage": "secretstorage",
        "typing_extensions": "typing-extensions",
        "requests": "requests",
        "urllib3": "urllib3",
        "certifi": "certifi",
        "click": "click",
        "attrs": "attrs",
    }

    assert set(expected) == {line.split("==")[0] for line in test_input}

    failures = []
    for pypi_name, expected_suffix in expected.items():
        got = resolve_package_dir(pypi_name, index)
        if got != expected_suffix:
            failures.append((pypi_name, got, expected_suffix))

    assert not failures, f"Resolution mismatches (got, expected): {failures}"

    print(f"Successfully resolved {len(expected)} packages against the real packages/ tree")


def test_aiohttp_socks_regression():
    """aiohttp-socks previously reverse-mapped to a nonexistent 'aiohttp_socks' directory,
    silently dropping it from every automated update run (see PR that bumped python-socks
    to 3.0.0 without a matching aiohttp-socks bump, breaking repoclosure)."""
    index = build_directory_index()
    assert resolve_package_dir("aiohttp-socks", index) == "aiohttp-socks"
    assert resolve_package_dir("aiohttp_socks", index) == "aiohttp-socks"


def test_galaxy_importer_and_importlib_resources_regression():
    """These directories were renamed to hyphenated form at some point, but the old
    hardcoded reverse-mapping table still pointed at the stale underscored names."""
    index = build_directory_index()
    assert resolve_package_dir("galaxy-importer", index) == "galaxy-importer"
    assert resolve_package_dir("importlib-resources", index) == "importlib-resources"


if __name__ == "__main__":
    test_real_world_sample_data()
    test_aiohttp_socks_regression()
    test_galaxy_importer_and_importlib_resources_regression()
