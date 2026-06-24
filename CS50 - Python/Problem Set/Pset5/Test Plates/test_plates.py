from plates import is_valid

# Test cases for number placement and leading zero rules
def test_check():
    # A valid plate: starts with letters, ends with numbers
    assert is_valid("CS50") == True
    # Invalid: the first number used cannot be a '0'
    assert is_valid("CS05") == False

# Test cases for character types and number positioning
def test_letter():
    # Invalid: letters cannot come after numbers ("P" comes after "50")
    assert is_valid("CS50P") == False
    # Invalid: periods and other punctuation are not allowed
    assert is_valid("PI3.14") == False

# Test cases for length constraints (typically between 2 and 6 characters)
def test_Capital():
    # Invalid: plate is too short (less than 2 characters)
    assert is_valid("H") == False
    # Invalid: plate is too long (more than 6 characters)
    assert is_valid("OUTATIME") == False
