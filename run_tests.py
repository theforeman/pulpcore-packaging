#!/usr/bin/env python3

import unittest
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def run_tests():
    """Run all tests in the test directory"""
    # Discover and run all tests in the test directory
    loader = unittest.TestLoader()
    start_dir = os.path.join(os.path.dirname(__file__), 'test')
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return exit code based on test results
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    sys.exit(run_tests()) 