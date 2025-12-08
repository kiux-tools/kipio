#!/usr/bin/env python3
"""
Integration tests for Kipio
"""
import tempfile
from unittest.mock import patch
import pytest

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from kipio import input_, print_
except ImportError:
    from core.kipio.kipio import print_, input_

def test_integration_file_logging():
    """Test input + file logging"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        logfile = f.name
    try:
        with patch('builtins.input', return_value='test_user'):
            username = input_("Username: ", required=True)
        print_(f"User logged in: {username}", file=logfile, mode="a", timestamp=True)
        log_content = print_("", file=logfile, mode="r", return_string=True)
        assert "test_user" in log_content
    finally:
        os.unlink(logfile)

def test_integration_configuration():
    """Test configuration setup"""
    inputs = ["John Doe", "dark", "yes", "8080"]
    input_responses = iter(inputs)
    def mock_input(prompt):
        return next(input_responses)
    with patch('builtins.input', mock_input):
        config = {
            "name": input_("Full name: ", required=True),
            "theme": input_("Theme: ", choices=["light", "dark", "auto"], default="dark"),
            "notifications": input_("Notifications? ", choices=["yes", "no"], default="yes") == "yes",
            "port": input_("Port: ", default="8080")
        }
    assert config["name"] == "John Doe"
    assert config["theme"] == "dark"
    assert config["notifications"] == True
    assert config["port"] == "8080"

def test_integration_security():
    """Test password scenario"""
    with patch('getpass.getpass', side_effect=['secret123', 'secret123']):
        password1 = input_("Password: ", hidden=True, required=True)
        password2 = input_("Confirm: ", hidden=True, required=True)
        assert password1 == password2 == "secret123"
