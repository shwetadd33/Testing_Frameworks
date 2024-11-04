import pytest


@pytest.mark.parametrize("test_input,expected",[("2+3",5),("3*4",12),pytest.param("2+1",5, marks=pytest.mark.xfail)])
def test_eval(test_input,expected):
    assert eval(test_input) == expected



