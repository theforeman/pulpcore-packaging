#!/usr/bin/env python3

import unittest
from unittest.mock import patch, mock_open, MagicMock
import subprocess
from find_package import find_packages


class TestFindPackages(unittest.TestCase):
    """Test the find_packages function with reverse mapping functionality"""

    def setUp(self):
        """Set up test fixtures"""
        # Clear any existing packages-to-update.txt content for each test
        self.packages_to_update_content = []

    def mock_file_write(self, content):
        """Mock file write to capture what would be written to packages-to-update.txt"""
        self.packages_to_update_content.append(content)

    @patch('subprocess.check_output')
    @patch('subprocess.run')
    @patch('builtins.open', new_callable=mock_open)
    def test_poetry_core_reverse_mapping(self, mock_file, mock_subprocess_run, mock_subprocess_check_output):
        """Test that poetry-core correctly maps to poetry_core directory"""
        # Mock the rpmspec command to return a version
        mock_subprocess_check_output.return_value = b'1.8.0'
        
        # Mock rpmdev-vercmp to return 12 (first version is older)
        mock_subprocess_run.return_value = MagicMock(returncode=12)
        
        # Mock file write
        mock_file.return_value.write = self.mock_file_write
        
        # Test the function
        find_packages('poetry-core', '1.9.0')
        
        # Verify the correct spec file path was used
        mock_subprocess_check_output.assert_called_with(
            ["rpmspec", "-q", "--queryformat=%{version}", "packages/python-poetry_core/python-poetry_core.spec", "--srpm"]
        )
        
        # Verify version comparison was called
        mock_subprocess_run.assert_called_with(["rpmdev-vercmp", "1.8.0", "1.9.0"])
        
        # Verify file was opened for append
        mock_file.assert_called_with("packages-to-update.txt", "a")

    @patch('subprocess.check_output')
    @patch('subprocess.run')
    @patch('builtins.open', new_callable=mock_open)
    def test_typing_extensions_no_reverse_mapping_needed(self, mock_file, mock_subprocess_run, mock_subprocess_check_output):
        """Test that typing-extensions doesn't need reverse mapping (directory exists as-is)"""
        # Mock the rpmspec command to return a version
        mock_subprocess_check_output.return_value = b'4.8.0'
        
        # Mock rpmdev-vercmp to return 0 (versions are the same)
        mock_subprocess_run.return_value = MagicMock(returncode=0)
        
        # Test the function
        find_packages('typing-extensions', '4.8.0')
        
        # Verify the correct spec file path was used (no reverse mapping)
        mock_subprocess_check_output.assert_called_with(
            ["rpmspec", "-q", "--queryformat=%{version}", "packages/python-typing-extensions/python-typing-extensions.spec", "--srpm"]
        )

    @patch('subprocess.check_output')
    @patch('subprocess.run')
    @patch('builtins.open', new_callable=mock_open)
    def test_flit_core_no_reverse_mapping_needed(self, mock_file, mock_subprocess_run, mock_subprocess_check_output):
        """Test that flit-core doesn't need reverse mapping (directory exists as-is)"""
        # Mock the rpmspec command to return a version
        mock_subprocess_check_output.return_value = b'3.9.0'
        
        # Mock rpmdev-vercmp to return 11 (first version is newer)
        mock_subprocess_run.return_value = MagicMock(returncode=11)
        
        # Test the function
        find_packages('flit-core', '3.8.0')
        
        # Verify the correct spec file path was used (no reverse mapping)
        mock_subprocess_check_output.assert_called_with(
            ["rpmspec", "-q", "--queryformat=%{version}", "packages/python-flit-core/python-flit-core.spec", "--srpm"]
        )

    @patch('subprocess.check_output')
    def test_spec_file_not_found_error_handling(self, mock_subprocess_check_output):
        """Test error handling when spec file is not found"""
        # Mock subprocess to raise CalledProcessError
        mock_subprocess_check_output.side_effect = subprocess.CalledProcessError(1, 'rpmspec')
        
        # Capture print output
        with patch('builtins.print') as mock_print:
            find_packages('nonexistent-package', '1.0.0')
            
            # Verify error message was printed
            mock_print.assert_called_with(
                "Spec file not found for package nonexistent-package (looked for packages/python-nonexistent-package/python-nonexistent-package.spec)"
            )

    @patch('subprocess.check_output')
    def test_reverse_mapping_with_spec_file_not_found(self, mock_subprocess_check_output):
        """Test error handling when spec file is not found even with reverse mapping"""
        # Mock subprocess to raise CalledProcessError
        mock_subprocess_check_output.side_effect = subprocess.CalledProcessError(1, 'rpmspec')
        
        # Capture print output
        with patch('builtins.print') as mock_print:
            find_packages('poetry-core', '1.0.0')
            
            # Verify error message shows the actual path that was looked for
            mock_print.assert_called_with(
                "Spec file not found for package poetry-core (looked for packages/python-poetry_core/python-poetry_core.spec)"
            )

    @patch('subprocess.check_output')
    @patch('subprocess.run')
    @patch('builtins.open', new_callable=mock_open)
    def test_all_reverse_mappings(self, mock_file, mock_subprocess_run, mock_subprocess_check_output):
        """Test all packages in the reverse mapping dictionary"""
        reverse_mappings = {
            'poetry-core': 'poetry_core',
            'poetry-plugin-export': 'poetry_plugin_export',
            'galaxy-importer': 'galaxy_importer',
            'psycopg_c': 'psycopg-c',
            'importlib-resources': 'importlib_resources',
            'ruamel-yaml': 'ruamel.yaml',
            'ruamel-yaml-clib': 'ruamel.yaml.clib',
            'jaraco-classes': 'jaraco.classes',
            'et-xmlfile': 'et_xmlfile',
            'aiohttp-socks': 'aiohttp_socks',
            'pyasn1-modules': 'pyasn1_modules',
            'pydantic-core': 'pydantic_core',
        }
        
        # Mock the rpmspec command to return a version
        mock_subprocess_check_output.return_value = b'1.0.0'
        
        # Mock rpmdev-vercmp to return 0 (versions are the same)
        mock_subprocess_run.return_value = MagicMock(returncode=0)
        
        for transformed_name, original_name in reverse_mappings.items():
            with self.subTest(package=transformed_name):
                # Reset mocks for each iteration
                mock_subprocess_check_output.reset_mock()
                
                # Test the function
                find_packages(transformed_name, '1.0.0')
                
                # Verify the correct spec file path was used
                expected_path = f"packages/python-{original_name}/python-{original_name}.spec"
                mock_subprocess_check_output.assert_called_with(
                    ["rpmspec", "-q", "--queryformat=%{version}", expected_path, "--srpm"]
                )

    @patch('subprocess.check_output')
    @patch('subprocess.run')
    @patch('builtins.open', new_callable=mock_open)
    def test_package_update_needed(self, mock_file, mock_subprocess_run, mock_subprocess_check_output):
        """Test that packages needing updates are written to the file"""
        # Mock the rpmspec command to return an older version
        mock_subprocess_check_output.return_value = b'1.8.0'
        
        # Mock rpmdev-vercmp to return 12 (first version is older, update needed)
        mock_subprocess_run.return_value = MagicMock(returncode=12)
        
        # Mock file write to capture content
        written_content = []
        def mock_write(content):
            written_content.append(content)
        
        mock_file.return_value.write = mock_write
        
        # Test the function
        find_packages('poetry-core', '1.9.0')
        
        # Verify the package was written to the update file
        self.assertEqual(written_content, ['poetry-core 1.9.0\n'])

    @patch('subprocess.check_output')
    @patch('subprocess.run')
    def test_version_comparison_outcomes(self, mock_subprocess_run, mock_subprocess_check_output):
        """Test all possible version comparison outcomes"""
        # Mock the rpmspec command to return a version
        mock_subprocess_check_output.return_value = b'1.0.0'
        
        test_cases = [
            (0, "Package poetry-core version is the same as the packaged RPM"),
            (11, "Packaged poetry-core RPM is newer than the version in requirements"),
            (12, "RPM for Package poetry-core needs to be updated from 1.0.0 to 2.0.0")
        ]
        
        for return_code, expected_message in test_cases:
            with self.subTest(return_code=return_code):
                mock_subprocess_run.return_value = MagicMock(returncode=return_code)
                
                with patch('builtins.print') as mock_print:
                    with patch('builtins.open', mock_open()):
                        find_packages('poetry-core', '2.0.0')
                        
                        # Check that the expected message was printed
                        mock_print.assert_called_with(expected_message)


if __name__ == '__main__':
    unittest.main()
