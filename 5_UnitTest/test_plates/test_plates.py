from plates import is_valid




def test_first2alpha():
    assert is_valid("Hi") == True
    assert is_valid("50") == False
    try:
        assert is_valid("50") == False
    except AssertionError:
        pass


def test_lenght():
    assert is_valid("HELLO") == True
    assert is_valid("OUTATIME") == False
    try:
        assert is_valid("OUTATIME") == False
    except AssertionError:
        pass


def test_alpha_numeric_only():
    assert is_valid("NRVOUS") == True
    assert is_valid("Pi3.14") == False
    try:
        assert is_valid("Pi3.14") == False
    except AssertionError:
        pass


def test_lastnumeric_placement():
    assert is_valid("CS50")  == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    try:
        assert is_valid("CS05") == False
    except AssertionError:
        pass