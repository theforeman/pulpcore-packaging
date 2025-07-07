#!/usr/bin/env python3

import sys
import os
import pytest


@pytest.fixture(scope="session", autouse=True)
def setup_import_path():
    """Add the parent directory to sys.path so we can import find_package module."""
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir) 