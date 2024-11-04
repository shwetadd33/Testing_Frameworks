"""
Creating custom markers for the test cases : windows and mac

to run tests of specific markers use commands:
pytest test_custom_markers.py -m windows -v
OR
pytest test_custom_markers.py -m mac -v
OR
pytest test_custom_markers.py -m "not windows" -v
"""
import pytest

@pytest.mark.windows
def test_windows_1():
    assert True

@pytest.mark.windows
def test_windows_2():
    assert True

@pytest.mark.mac
def test_mac_1():
    assert True

@pytest.mark.mac
def test_mac_2():
    assert True
