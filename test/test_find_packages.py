#!/usr/bin/env python3

import unittest
from unittest.mock import patch, mock_open, MagicMock
import subprocess
from find_package import find_packages, resolve_package_dir, canonicalize, strip_python_prefix


class TestCanonicalize(unittest.TestCase):
    """Test the name-normalization helpers directly."""

    def test_lowercases_and_collapses_separators(self):
        self.assertEqual(canonicalize("PyYAML"), "pyyaml")
        self.assertEqual(canonicalize("ruamel.yaml.clib"), "ruamel-yaml-clib")
        self.assertEqual(canonicalize("poetry_core"), "poetry-core")
        self.assertEqual(canonicalize("opentelemetry-api"), "opentelemetry-api")
        self.assertEqual(canonicalize("jaraco.classes"), "jaraco-classes")

    def test_strip_python_prefix(self):
        self.assertEqual(strip_python_prefix("python-socks"), "socks")
        self.assertEqual(strip_python_prefix("python-dateutil"), "dateutil")
        self.assertEqual(strip_python_prefix("aiohttp-socks"), "aiohttp-socks")


class TestResolvePackageDir(unittest.TestCase):
    """Test resolving PyPI names to on-disk spec directory suffixes via a fake index,
    covering every separator-mismatch case that used to require a hand-maintained
    reverse-mapping table."""

    def setUp(self):
        # A representative slice of the real packages/ tree, including every case that
        # previously needed an entry in the old package_mappings/reverse_mappings tables.
        self.index = {
            canonicalize(suffix): suffix
            for suffix in [
                "socks",
                "aiohttp-socks",
                "poetry_core",
                "poetry_plugin_export",
                "galaxy_importer",
                "importlib-resources",
                "ruamel-yaml",
                "ruamel-yaml-clib",
                "jaraco-classes",
                "et-xmlfile",
                "pyasn1-modules",
                "psycopg_c",
                "pydantic-core",
                "opentelemetry_api",
                "typing-extensions",
                "flit-core",
                "pyyaml",
            ]
        }

    def test_hyphenated_pypi_name_resolves_to_underscored_directory(self):
        self.assertEqual(resolve_package_dir("poetry-core", self.index), "poetry_core")
        self.assertEqual(resolve_package_dir("poetry-plugin-export", self.index), "poetry_plugin_export")
        self.assertEqual(resolve_package_dir("galaxy-importer", self.index), "galaxy_importer")
        self.assertEqual(resolve_package_dir("psycopg-c", self.index), "psycopg_c")
        self.assertEqual(resolve_package_dir("opentelemetry-api", self.index), "opentelemetry_api")

    def test_dotted_pypi_name_resolves_to_hyphenated_directory(self):
        self.assertEqual(resolve_package_dir("ruamel.yaml", self.index), "ruamel-yaml")
        self.assertEqual(resolve_package_dir("ruamel.yaml.clib", self.index), "ruamel-yaml-clib")
        self.assertEqual(resolve_package_dir("jaraco.classes", self.index), "jaraco-classes")

    def test_underscored_pypi_name_resolves_to_hyphenated_directory(self):
        self.assertEqual(resolve_package_dir("et_xmlfile", self.index), "et-xmlfile")
        self.assertEqual(resolve_package_dir("pyasn1_modules", self.index), "pyasn1-modules")
        self.assertEqual(resolve_package_dir("importlib_resources", self.index), "importlib-resources")

    def test_hyphenated_pypi_name_matching_directory_exactly(self):
        self.assertEqual(resolve_package_dir("typing-extensions", self.index), "typing-extensions")
        self.assertEqual(resolve_package_dir("flit-core", self.index), "flit-core")
        self.assertEqual(resolve_package_dir("pydantic-core", self.index), "pydantic-core")

    def test_mixed_case_pypi_name(self):
        self.assertEqual(resolve_package_dir("PyYAML", self.index), "pyyaml")

    def test_pypi_name_with_own_python_prefix(self):
        # python-socks is the literal PyPI project name; the repo convention adds
        # another 'python-' on top for the RPM directory (packages/python-socks).
        self.assertEqual(resolve_package_dir("python-socks", self.index), "socks")

    def test_aiohttp_socks_bug_regression(self):
        # This is the exact case that used to break: aiohttp-socks (hyphen, matches
        # its own directory suffix exactly) was incorrectly reverse-mapped to a
        # nonexistent 'aiohttp_socks' (underscore) directory.
        self.assertEqual(resolve_package_dir("aiohttp-socks", self.index), "aiohttp-socks")

    def test_unpackaged_name_returns_none(self):
        self.assertIsNone(resolve_package_dir("nonexistent-package", self.index))


class TestFindPackages(unittest.TestCase):
    """Test find_packages() end to end, including that packages-to-update.txt and the
    printed messages use the resolved on-disk directory suffix -- since update_packages.sh
    and the PR title/branch downstream reuse that exact string to rebuild the spec path."""

    @patch("subprocess.check_output")
    @patch("subprocess.run")
    @patch("builtins.open", new_callable=mock_open)
    def test_update_needed_writes_resolved_directory_suffix(self, mock_file, mock_run, mock_check_output):
        mock_check_output.return_value = b"1.8.0"
        mock_run.return_value = MagicMock(returncode=12)

        written_content = []
        mock_file.return_value.write = lambda content: written_content.append(content)

        with patch("find_package.resolve_package_dir", return_value="poetry_core"):
            find_packages("poetry-core", "1.9.0")

        mock_check_output.assert_called_with(
            ["rpmspec", "-q", "--queryformat=%{version}", "packages/python-poetry_core/python-poetry_core.spec", "--srpm"]
        )
        mock_run.assert_called_with(["rpmdev-vercmp", "1.8.0", "1.9.0"])
        self.assertEqual(written_content, ["poetry_core 1.9.0\n"])

    @patch("subprocess.check_output")
    @patch("subprocess.run")
    @patch("builtins.open", new_callable=mock_open)
    def test_aiohttp_socks_resolves_to_its_own_hyphenated_directory(self, mock_file, mock_run, mock_check_output):
        mock_check_output.return_value = b"0.10.1"
        mock_run.return_value = MagicMock(returncode=12)

        with patch("find_package.resolve_package_dir", return_value="aiohttp-socks"):
            find_packages("aiohttp-socks", "0.12.0")

        mock_check_output.assert_called_with(
            ["rpmspec", "-q", "--queryformat=%{version}", "packages/python-aiohttp-socks/python-aiohttp-socks.spec", "--srpm"]
        )

    @patch("builtins.print")
    def test_unresolvable_package_prints_error_without_calling_rpmspec(self, mock_print):
        with patch("find_package.resolve_package_dir", return_value=None):
            find_packages("nonexistent-package", "1.0.0")

        mock_print.assert_called_with(
            "Spec file not found for package nonexistent-package (no packages/python-* directory matches)"
        )

    @patch("subprocess.check_output")
    def test_spec_file_missing_on_disk_despite_resolved_directory(self, mock_check_output):
        mock_check_output.side_effect = subprocess.CalledProcessError(1, "rpmspec")

        with patch("find_package.resolve_package_dir", return_value="poetry_core"):
            with patch("builtins.print") as mock_print:
                find_packages("poetry-core", "1.0.0")

        mock_print.assert_called_with(
            "Spec file not found for package poetry-core (looked for packages/python-poetry_core/python-poetry_core.spec)"
        )

    @patch("subprocess.check_output")
    @patch("subprocess.run")
    def test_version_comparison_outcomes_use_resolved_name(self, mock_run, mock_check_output):
        mock_check_output.return_value = b"1.0.0"

        test_cases = [
            (0, "Package poetry_core version is the same as the packaged RPM"),
            (11, "Packaged poetry_core RPM is newer than the version in requirements"),
            (12, "RPM for Package poetry_core needs to be updated from 1.0.0 to 2.0.0"),
        ]

        for return_code, expected_message in test_cases:
            with self.subTest(return_code=return_code):
                mock_run.return_value = MagicMock(returncode=return_code)

                with patch("find_package.resolve_package_dir", return_value="poetry_core"):
                    with patch("builtins.print") as mock_print:
                        with patch("builtins.open", mock_open()):
                            find_packages("poetry-core", "2.0.0")

                            mock_print.assert_called_with(expected_message)


if __name__ == "__main__":
    unittest.main()
