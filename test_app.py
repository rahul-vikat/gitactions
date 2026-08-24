"""
pytest unit tests for app.py functions.
Run via GitHub Actions CI workflow.
"""

from app import add, divide, multiply, subtract
import os
import requests

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 3) == -3
    assert multiply(0, 5) == 0


def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    try:
        divide(1, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass