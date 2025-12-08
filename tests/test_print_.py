#!/usr/bin/env python3
"""
Tests for print_() function
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

def test_print_basic(capsys):
    """Test basic print functionality"""
    print_("Hello", "World")
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"

def test_print_sep(capsys):
    """Test separator parameter"""
    print_("Hello", "World", sep=", ")
    captured = capsys.readouterr()
    assert captured.out == "Hello, World\n"

def test_print_end(capsys):
    """Test end parameter"""
    print_("Hello", end="")
    captured = capsys.readouterr()
    assert captured.out == "Hello"

def test_print_timestamp(capsys):
    """Test timestamp parameter"""
    print_("Test", timestamp=True)
    captured = capsys.readouterr()
    assert "[" in captured.out
    assert "]" in captured.out
    assert "Test" in captured.out

def test_print_silent(capsys):
    """Test silent mode"""
    print_("Hello", silent=True)
    captured = capsys.readouterr()
    assert captured.out == ""

def test_print_return_string():
    """Test return_string parameter"""
    result = print_("Hello", "World", return_string=True, silent=True)
    assert isinstance(result, str)
    assert result == "Hello World\n"

def test_print_bytes():
    """Test _bytes_ parameter"""
    # بدون return_string، يجب أن يرجع bytes
    result = print_("Hello", _bytes_=True, silent=True)
    assert isinstance(result, bytes)
    assert result == b"Hello\n"
    
    # مع return_string، يجب أن يرجع str (الأولوية لـ return_string)
    result = print_("Hello", _bytes_=True, return_string=True, silent=True)
    assert isinstance(result, str)
    assert result == "Hello\n"

def test_print_to_file_write():
    """Test writing to file"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        filename = f.name
    try:
        print_("Line 1", file=filename, mode="w")
        print_("Line 2", file=filename, mode="a")
        with open(filename, 'r') as f:
            content = f.read()
        assert content == "Line 1\nLine 2\n"
    finally:
        os.unlink(filename)

def test_print_to_file_read():
    """Test reading from file"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write("Existing content\n")
        filename = f.name
    try:
        result = print_("", file=filename, mode="r", return_string=True)
        assert isinstance(result, str)
        assert result == "Existing content\n"
    finally:
        os.unlink(filename)

def test_print_error_handling(capsys):
    """Test error handling"""
    result = print_("", file="nonexistent.txt", mode="r", return_string=True)
    assert isinstance(result, str)
    assert "Error:" in result
