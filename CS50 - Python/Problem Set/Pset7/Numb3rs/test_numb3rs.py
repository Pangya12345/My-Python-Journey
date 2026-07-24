from numb3rs import validate

def test_digit():
    assert validate("2.6.5.8") == True
    assert validate("24.56.89.74") == True
    assert validate("123.164.190.205") == True

def test_digit_wrong():
    assert validate("-1.6.5.4") == False
    assert validate("34.-60.32.16") == False
    assert validate("234.134.187.567") == False

def test_digit_wrong_mix():
    assert validate("44.145.205.-1") == False
    assert validate("164.245.-34.1") == False
    assert validate("45.2.134.456") == False


def test_random_mix_correct():
    assert validate("45.1.245.43") == True
    assert validate("21.9.190.250") == True
    