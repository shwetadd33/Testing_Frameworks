"""
We can generate the details of the test execution in an xml file.

pytest test_Results_in_XML.py -v --junitxml="result.xml"
"""

import pytest

@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100

@pytest.mark.great
def test_greate_equale():
    num = 100
    assert  num >= 100

@pytest.mark.others
def test_less():
    num = 100
    assert num < 200
