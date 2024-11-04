"""
Fixtures:
Fixtures are functions, which will run before each test function to which it is applied. Fixtures are used to feed some
data to the tests such as database connections, URLs to test and some sort of input data. Therefore, instead of running
the same code for every test, we can attach fixture function to the tests and it will run and return the data to the
test before executing each test.

A function is marked as a fixture by −
@pytest.fixture
"""

import pytest

@pytest.fixture
def input_value():
    input = 39
    return input


def test_divisible_by_3(input_value):
    assert input_value % 3 == 0


def test_divisible_by_6(input_value):
    assert input_value % 6 == 0
