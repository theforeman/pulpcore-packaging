#!/usr/bin/env python3

from find_package import parse_package_list


def test_prefix_removals():
    """Test packages that have prefixes removed (python-)"""
    test_input = [
        "python-dateutil==2.9.0.post0",
        "python-debian==0.1.49",
        "python-gnupg==0.5.4",
        "python-socks==2.7.1"
    ]
    
    expected = [
        {'package_name': 'dateutil', 'new_version': '2.9.0.post0'},
        {'package_name': 'debian', 'new_version': '0.1.49'},
        {'package_name': 'gnupg', 'new_version': '0.5.4'},
        {'package_name': 'socks', 'new_version': '2.7.1'}
    ]
    
    result = list(parse_package_list(test_input))
    assert result == expected


def test_exact_package_mappings():
    """Test packages with exact name mappings"""
    test_input = [
        "typing_extensions==4.14.1",
        "galaxy_importer==0.4.31",
        "psycopg-c==3.2.9",
        "importlib_resources==6.4.5",
        "ruamel.yaml==0.18.14",
        "ruamel.yaml.clib==0.2.12",
        "jaraco.classes==3.4.0",
        "et_xmlfile==2.0.0",
        "aiohttp_socks==0.10.1",
        "pyasn1_modules==0.4.2",
        "pydantic_core==2.33.2",
        "flit_core==3.12.0",
        "poetry_core==1.9.0",
        "poetry_plugin_export==1.8.0"
    ]
    
    expected = [
        {'package_name': 'typing-extensions', 'new_version': '4.14.1'},
        {'package_name': 'galaxy-importer', 'new_version': '0.4.31'},
        {'package_name': 'psycopg_c', 'new_version': '3.2.9'},
        {'package_name': 'importlib-resources', 'new_version': '6.4.5'},
        {'package_name': 'ruamel-yaml', 'new_version': '0.18.14'},
        {'package_name': 'ruamel-yaml-clib', 'new_version': '0.2.12'},
        {'package_name': 'jaraco-classes', 'new_version': '3.4.0'},
        {'package_name': 'et-xmlfile', 'new_version': '2.0.0'},
        {'package_name': 'aiohttp-socks', 'new_version': '0.10.1'},
        {'package_name': 'pyasn1-modules', 'new_version': '0.4.2'},
        {'package_name': 'pydantic-core', 'new_version': '2.33.2'},
        {'package_name': 'flit-core', 'new_version': '3.12.0'},
        {'package_name': 'poetry-core', 'new_version': '1.9.0'},
        {'package_name': 'poetry-plugin-export', 'new_version': '1.8.0'}
    ]
    
    result = list(parse_package_list(test_input))
    assert result == expected


def test_lowercase_packages():
    """Test packages that need to be lowercased"""
    test_input = [
        "PyYAML==6.0.2",
        "GitPython==3.1.44",
        "Deprecated==1.2.18",
        "CacheControl==0.14.3",
        "Django==4.2.23",
        "Jinja2==3.1.6",
        "MarkupPy==1.18",
        "MarkupSafe==3.0.2",
        "Parsley==1.3",
        "PyGObject==3.50.1",
        "Pygments==2.19.2",
        "PyJWT==2.10.1",
        "RapidFuzz==3.13.0",
        "SecretStorage==3.3.3"
    ]
    
    expected = [
        {'package_name': 'pyyaml', 'new_version': '6.0.2'},
        {'package_name': 'gitpython', 'new_version': '3.1.44'},
        {'package_name': 'deprecated', 'new_version': '1.2.18'},
        {'package_name': 'cachecontrol', 'new_version': '0.14.3'},
        {'package_name': 'django', 'new_version': '4.2.23'},
        {'package_name': 'jinja2', 'new_version': '3.1.6'},
        {'package_name': 'markuppy', 'new_version': '1.18'},
        {'package_name': 'markupsafe', 'new_version': '3.0.2'},
        {'package_name': 'parsley', 'new_version': '1.3'},
        {'package_name': 'pygobject', 'new_version': '3.50.1'},
        {'package_name': 'pygments', 'new_version': '2.19.2'},
        {'package_name': 'pyjwt', 'new_version': '2.10.1'},
        {'package_name': 'rapidfuzz', 'new_version': '3.13.0'},
        {'package_name': 'secretstorage', 'new_version': '3.3.3'}
    ]
    
    result = list(parse_package_list(test_input))
    assert result == expected


def test_pattern_based_transformations():
    """Test pattern-based transformations"""
    test_input = [
        "opentelemetry-api==1.30.0",
        "opentelemetry-exporter-otlp-proto-common==1.30.0",
        "opentelemetry-proto==1.30.0",
        "poetry==1.8.3",
        "flit==3.12.0",
        "etils==1.0.0",  # et prefix example
        "aiohttp==3.11.18",
        "pyasn1==0.6.1",
        "pydantic==2.11.7"
    ]
    
    expected = [
        {'package_name': 'opentelemetry_api', 'new_version': '1.30.0'},
        {'package_name': 'opentelemetry_exporter_otlp_proto_common', 'new_version': '1.30.0'},
        {'package_name': 'opentelemetry_proto', 'new_version': '1.30.0'},
        {'package_name': 'poetry', 'new_version': '1.8.3'},  # No transformation for single word
        {'package_name': 'flit', 'new_version': '3.12.0'},  # No transformation for single word
        {'package_name': 'etils', 'new_version': '1.0.0'},  # No transformation for single word
        {'package_name': 'aiohttp', 'new_version': '3.11.18'},  # No transformation for single word
        {'package_name': 'pyasn1', 'new_version': '0.6.1'},  # No transformation for single word
        {'package_name': 'pydantic', 'new_version': '2.11.7'}  # No transformation for single word
    ]
    
    result = list(parse_package_list(test_input))
    assert result == expected


def test_no_transformation_needed():
    """Test packages that don't need any transformation"""
    test_input = [
        "requests==2.32.4",
        "urllib3==2.5.0",
        "certifi==2025.6.15",
        "click==8.1.8",
        "attrs==22.2.0"
    ]
    
    expected = [
        {'package_name': 'requests', 'new_version': '2.32.4'},
        {'package_name': 'urllib3', 'new_version': '2.5.0'},
        {'package_name': 'certifi', 'new_version': '2025.6.15'},
        {'package_name': 'click', 'new_version': '8.1.8'},
        {'package_name': 'attrs', 'new_version': '22.2.0'}
    ]
    
    result = list(parse_package_list(test_input))
    assert result == expected


def test_mixed_transformations():
    """Test a mix of different transformation types"""
    test_input = [
        "PyYAML==6.0.2",  # lowercase
        "python-dateutil==2.9.0.post0",  # prefix removal
        "typing_extensions==4.14.1",  # exact mapping
        "opentelemetry-api==1.30.0",  # pattern transformation
        "requests==2.32.4"  # no transformation
    ]
    
    expected = [
        {'package_name': 'pyyaml', 'new_version': '6.0.2'},
        {'package_name': 'dateutil', 'new_version': '2.9.0.post0'},
        {'package_name': 'typing-extensions', 'new_version': '4.14.1'},
        {'package_name': 'opentelemetry_api', 'new_version': '1.30.0'},
        {'package_name': 'requests', 'new_version': '2.32.4'}
    ]
    
    result = list(parse_package_list(test_input))
    assert result == expected


def test_empty_input():
    """Test empty input"""
    test_input = []
    expected = []
    
    result = list(parse_package_list(test_input))
    assert result == expected


def test_whitespace_handling():
    """Test handling of whitespace in input"""
    test_input = [
        "  PyYAML==6.0.2  ",
        "\trequests==2.32.4\n",
        "   ",  # Empty line with whitespace
        "click==8.1.8"
    ]
    
    expected = [
        {'package_name': 'pyyaml', 'new_version': '6.0.2'},
        {'package_name': 'requests', 'new_version': '2.32.4'},
        {'package_name': 'click', 'new_version': '8.1.8'}
    ]
    
    result = list(parse_package_list(test_input))
    assert result == expected 