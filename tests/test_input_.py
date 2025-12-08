#!/usr/bin/env python3
"""
Tests for input_() function
"""
from unittest.mock import patch
import pytest

import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from kipio import input_, print_
except ImportError:
    from core.kipio.kipio import print_, input_

def test_input_basic():
    """Test basic input functionality"""
    with patch('builtins.input', return_value='test'):
        result = input_("Enter: ")
        assert result == "test"

def test_input_strip():
    """Test strip parameter"""
    with patch('builtins.input', return_value='  test  '):
        result = input_("Enter: ", strip=True)
        assert result == "test"
        result = input_("Enter: ", strip=False)
        assert result == "  test  "

def test_input_lower():
    """Test lower parameter"""
    with patch('builtins.input', return_value='TEST'):
        result = input_("Enter: ", lower=True)
        assert result == "test"
        result = input_("Enter: ", lower=False)
        assert result == "TEST"

def test_input_choices():
    """Test choices validation"""
    with patch('builtins.input', return_value='yes'):
        result = input_("Continue? ", choices=['yes', 'no'], show_choices=False)
        assert result == "yes"

def test_input_choices_with_lower():
    """Test choices with lower=True"""
    with patch('builtins.input', return_value='YES'):
        result = input_("Test: ", choices=['yes', 'no'], lower=True)
        assert result == "yes"
    with patch('builtins.input', return_value='yes'):
        result = input_("Test: ", choices=['YES', 'NO'], lower=True)
        assert result == "yes"

def test_input_default():
    """Test default value"""
    with patch('builtins.input', return_value=''):
        result = input_("Enter: ", default='default_value')
        assert result == "default_value"
    with patch('builtins.input', return_value='custom'):
        result = input_("Enter: ", default='default_value')
        assert result == "custom"

def test_input_hidden():
    """Test hidden input (password)"""
    with patch('getpass.getpass', return_value='secret'):
        result = input_("Password: ", hidden=True)
        assert result == "secret"

def test_input_bytes():
    """Test _bytes_ parameter"""
    with patch('builtins.input', return_value='test'):
        result = input_("Enter: ", _bytes_=True)
        assert isinstance(result, bytes)
        assert result == b'test'

def test_input_error_handling():
    """Test error handling returns error message"""
    with patch('builtins.input', side_effect=ValueError("Test error")):
        result = input_("Enter: ")
        assert isinstance(result, str)
        assert "Error:" in result
        assert "Test error" in result

def test_input_show_choices():
    """Test show_choices parameter"""
    with patch('builtins.input', return_value='yes'):
        result = input_("Continue? ", choices=['yes', 'no'], show_choices=True)
        assert result == "yes"
