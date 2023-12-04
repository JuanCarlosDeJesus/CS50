# Test fuel
import pytest
from fuel import convert,gauge


def test_convert():
    assert convert("1/4") == 25
    assert convert("100/100") == 100
    assert convert("0/100") == 0
    assert convert("99/100") == 99


def test_yequals_0():
    with pytest.raises(ZeroDivisionError):
        assert convert("2/0")


def test_xandy_notdigit():
    with pytest.raises(ValueError):
        assert convert("cat/dog")
    with pytest.raises(ValueError):
        assert convert("3/2")


def test_xandy_value():
    assert gauge(25) == "25%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"