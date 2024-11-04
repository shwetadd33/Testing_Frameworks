import pytest


@pytest.mark.parametrize("x", [1, 3])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    pass
