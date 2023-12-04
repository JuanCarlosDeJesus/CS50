"""
Implement one or more functions that collectively test your implementation of shorten thoroughly, each of whose names
should begin with test_ so that you can execute your tests with:

pytest test_twttr.py

"""

from twttr import shorten


def test_twttr():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
    assert shorten("cs5O") == "cs5"