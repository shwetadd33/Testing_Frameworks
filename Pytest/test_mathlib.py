import sys
import pytest
import mathlib

@pytest.mark.skip(reason="Shweta: Skipping this test at this moment")
def test_calc_total():
    total = mathlib.cal_total(4, 5)
    assert total == 9


def test_calc_multiply():
    mul = mathlib.cal_multiply(20, 5)
    assert mul == 100

@pytest.mark.skipif(sys.version_info > (3,5), reason="Shweta: Wrong Python version")
def test_calc_division():
    div = mathlib.cal_div(32, 6)
    assert div == 9
