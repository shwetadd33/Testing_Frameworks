"""
This is first basic pytest test/program file
Run the test using the following command in cmd−
pytest

Observe that only the functions starting with word 'test' is executed and others are skipped while running the test file.

Note : use command: pytest -v
Now the result is more explanatory about the test that failed and the test that passed.

"""
import math
import pytest

@pytest.mark.square
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

@pytest.mark.square
def testsquare():
    num = 7
    assert 7*7 == 40

@pytest.mark.others
def tesequality():
    assert 10 == 11