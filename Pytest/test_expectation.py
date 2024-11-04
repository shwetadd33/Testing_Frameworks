"""
Parameterizing of a test is done to run the test against multiple sets of inputs. We can do this by using the following marker −
@pytest.mark.parametrize
"""

import pytest


@pytest.mark.parametrize("test_input,expected", [("2+3", 5), ("4+8", 13), ("2*0", 2), ("12+3", 15)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("test_input,expected_text", [("Apple", "Apple"), ("Orange", "Banana"), ("MANGO", "mango")])
def test_compare_strings(test_input, expected_text):
    assert test_input.lower() == expected_text.lower()