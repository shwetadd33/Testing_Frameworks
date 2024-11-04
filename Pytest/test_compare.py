"""
Possible ways to execute the tests:
1. To run all the tests files in a directory use commands:
pytest
OR
pytest -v

2. To execute the tests from a specific file, use the following syntax −
pytest <filename> -v
ex: pytest test_compare.py -v

3. To execute the tests containing a string in its name we can use the following syntax −
pytest -k <substring> -v
ex: pytest -k great -v

4. Pytest allows us to use markers on test functions. Markers are used to set various features/attributes to test functions,
such as xfail, skip and parametrize.Apart from that, users can create their own marker names
Markers are applied on the tests functions using the syntax  −
@pytest.mark.<markername>

To use markers, we have to import pytest module in the test file

To run the marked tests, we can use the following syntax −
pytest -m <markername> -v

Now to run the tests marked as great, run the following command −
pytest -m great -v

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
