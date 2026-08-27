#!/usr/bin/env python3

from find_package import parse_package_list


def test_parses_name_and_version_verbatim():
    """parse_package_list() is a pure passthrough: it splits 'name==version' pairs and
    does no name normalization. All PyPI-name -> on-disk-directory resolution (lowercasing,
    prefix handling, separator normalization) lives in resolve_package_dir() instead, since
    that's the only place that actually knows what's on disk -- see test_find_packages.py."""
    test_input = [
        "PyYAML==6.0.2",
        "python-dateutil==2.9.0.post0",
        "typing_extensions==4.14.1",
        "opentelemetry-api==1.30.0",
        "requests==2.32.4",
    ]

    expected = [
        {"package_name": "PyYAML", "new_version": "6.0.2"},
        {"package_name": "python-dateutil", "new_version": "2.9.0.post0"},
        {"package_name": "typing_extensions", "new_version": "4.14.1"},
        {"package_name": "opentelemetry-api", "new_version": "1.30.0"},
        {"package_name": "requests", "new_version": "2.32.4"},
    ]

    assert list(parse_package_list(test_input)) == expected


def test_skips_unparseable_lines_instead_of_crashing(capsys):
    # Requirements freezes can carry VCS/URL/editable deps ('name @ url', '-e git+...')
    # that don't have a '==' pin. One bad line shouldn't abort the whole run.
    test_input = [
        "requests==2.32.4",
        "some-vcs-dep @ git+https://example.com/some-vcs-dep.git",
        "-e git+https://example.com/editable-dep.git#egg=editable-dep",
        "click==8.1.8",
    ]

    expected = [
        {"package_name": "requests", "new_version": "2.32.4"},
        {"package_name": "click", "new_version": "8.1.8"},
    ]

    assert list(parse_package_list(test_input)) == expected
    assert "Skipping unparseable requirements line" in capsys.readouterr().out


def test_empty_input():
    assert list(parse_package_list([])) == []


def test_whitespace_handling():
    test_input = [
        "  PyYAML==6.0.2  ",
        "\trequests==2.32.4\n",
        "   ",  # blank line, skipped
        "click==8.1.8",
    ]

    expected = [
        {"package_name": "PyYAML", "new_version": "6.0.2"},
        {"package_name": "requests", "new_version": "2.32.4"},
        {"package_name": "click", "new_version": "8.1.8"},
    ]

    assert list(parse_package_list(test_input)) == expected
