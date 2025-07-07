# Test Suite for find_package.py

This directory contains comprehensive tests for the `parse_package_list` function in `find_package.py`.

## Test Coverage

The test suite covers all transformation scenarios used by the `parse_package_list` function:

### 1. **Prefix Removals** (`test_prefix_removals`)
Tests packages that have prefixes removed (e.g., `python-` prefix):
- `python-dateutil` → `dateutil`
- `python-debian` → `debian`
- `python-gnupg` → `gnupg`
- `python-socks` → `socks`

### 2. **Exact Package Mappings** (`test_exact_package_mappings`)
Tests packages with specific name mappings:
- `typing_extensions` → `typing-extensions`
- `galaxy_importer` → `galaxy-importer`
- `psycopg-c` → `psycopg_c`
- `importlib_resources` → `importlib-resources`
- `ruamel.yaml` → `ruamel-yaml`
- And many more...

### 3. **Lowercase Packages** (`test_lowercase_packages`)
Tests packages that need to be converted to lowercase:
- `PyYAML` → `pyyaml`
- `GitPython` → `gitpython`
- `Django` → `django`
- `RapidFuzz` → `rapidfuzz`
- And others...

### 4. **Pattern-Based Transformations** (`test_pattern_based_transformations`)
Tests packages that follow specific patterns:
- OpenTelemetry packages: `opentelemetry-api` → `opentelemetry_api`
- Poetry packages: transformations for underscores/hyphens
- Flit packages: transformations for underscores/hyphens
- And more pattern-based rules...

### 5. **No Transformation** (`test_no_transformation_needed`)
Tests packages that don't need any transformation:
- `requests`, `urllib3`, `certifi`, `click`, `attrs`

### 6. **Mixed Transformations** (`test_mixed_transformations`)
Tests a combination of different transformation types in one test case.

### 7. **Edge Cases**
- **Empty Input** (`test_empty_input`): Tests handling of empty input
- **Whitespace Handling** (`test_whitespace_handling`): Tests proper trimming and handling of whitespace

## Running the Tests

### Install test dependencies:
```bash
pip install -r test/requirements-test.txt
```

### From the main directory:
```bash
python run_tests.py
```

### Using pytest directly:
```bash
# Run all tests
python -m pytest test/ -v

# Run specific test file
python -m pytest test/test_parse_package_list.py -v

# Run specific test function
python -m pytest test/test_parse_package_list.py::test_prefix_removals -v

# Run integration test
python -m pytest test/test_integration.py::test_real_world_sample_data -v
```

### Additional pytest options:
```bash
# Run tests with coverage report
python -m pytest test/ --cov=find_package --cov-report=html

# Run tests in parallel (if pytest-xdist is installed)
python -m pytest test/ -n auto
```

## Test Structure

- `test_parse_package_list.py`: Main test file with 8 unit tests
- `test_integration.py`: Integration test with real-world data (191 packages)
- `conftest.py`: Pytest configuration with shared fixtures for import path setup
- `requirements-test.txt`: Test dependencies (pytest and optional plugins)
- `__init__.py`: Makes the test directory a Python package
- `README.md`: This documentation file

## Adding New Tests

When adding new transformation rules to `find_package.py`, make sure to:

1. Add corresponding test functions to `test_parse_package_list.py`
2. Include both the input and expected output
3. Test edge cases and variations
4. Run the full test suite to ensure nothing is broken

## Test Results

All tests should pass with output similar to:
```
=============================== test session starts ================================
platform linux -- Python 3.11.x, pytest-7.x.x, py-1.x.x, pluggy-1.x.x
collected 9 items

test/test_integration.py::test_real_world_sample_data PASSED          [ 11%]
test/test_parse_package_list.py::test_prefix_removals PASSED          [ 22%]
test/test_parse_package_list.py::test_exact_package_mappings PASSED   [ 33%]
test/test_parse_package_list.py::test_lowercase_packages PASSED       [ 44%]
test/test_parse_package_list.py::test_pattern_based_transformations PASSED [ 55%]
test/test_parse_package_list.py::test_no_transformation_needed PASSED [ 66%]
test/test_parse_package_list.py::test_mixed_transformations PASSED    [ 77%]
test/test_parse_package_list.py::test_empty_input PASSED              [ 88%]
test/test_parse_package_list.py::test_whitespace_handling PASSED      [100%]

=============================== 9 passed in 0.05s ================================
```

## Continuous Integration

The repository includes a GitHub Actions workflow (`.github/workflows/test-find-package.yml`) that automatically runs the test suite when:
- `find_package.py` is modified
- Files in the `test/` directory are changed  
- The workflow file itself is modified

The workflow tests against Python 3.11 and 3.12 and uses pytest for test execution. 