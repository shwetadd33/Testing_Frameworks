"""
Using fixture from conftest.py
"""
import pytest

def test_divide_by_9(input_value_1):
    assert input_value_1 % 9 == 0

def test_divide_by_5(input_value_1):
    assert input_value_1 % 5 == 0

