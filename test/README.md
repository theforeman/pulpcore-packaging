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

### From the main directory:
```bash
python run_tests.py
```

### From the test directory:
```bash
cd test
python -m unittest test_parse_package_list.py -v
```

### Running specific test methods:
```bash
cd test
python -m unittest test_parse_package_list.TestParsePackageList.test_prefix_removals -v
```

## Test Structure

- `test_parse_package_list.py`: Main test file containing all test cases
- `__init__.py`: Makes the test directory a Python package
- `README.md`: This documentation file

## Adding New Tests

When adding new transformation rules to `find_package.py`, make sure to:

1. Add corresponding test cases to `test_parse_package_list.py`
2. Include both the input and expected output
3. Test edge cases and variations
4. Run the full test suite to ensure nothing is broken

## Test Results

All tests should pass with output similar to:
```
test_empty_input ... ok
test_exact_package_mappings ... ok
test_lowercase_packages ... ok
test_mixed_transformations ... ok
test_no_transformation_needed ... ok
test_pattern_based_transformations ... ok
test_prefix_removals ... ok
test_whitespace_handling ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.000s

OK 