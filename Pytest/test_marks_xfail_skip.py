"""
xfail :  Pytest will execute the xfailed test, but it will not be considered as part failed or passed tests.
Details of these tests will not be printed even if the test fails
@pytest.mark.xfail

Skipping a test means that the test will not be executed. We can skip tests using the following marker −
@pytest.mark.skip


Note -
The syntax to stop the execution of test suite soon after n number of test fails is as follows −
pytest --maxfail = <num>
ex - pytest test_failure.py -v --maxfail 1
"""

import pytest


@pytest.mark.xfail
def test_greater_than():
    num = 100
    assert num > 100


@pytest.mark.xfail
def test_greater_than_equal():
    num = 100
    assert num >= 100


@pytest.mark.skip
def test_less_than():
    num = 100
    assert num < 100
