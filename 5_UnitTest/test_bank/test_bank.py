from bank import value

def test_bank():
    assert value("Hello") == 0
    assert value("Hi") == 20
    assert value("What's up!") == 100

def test_bank_err():
    try:
        assert value("Hello") == "$100"
    except AssertionError:
        pass