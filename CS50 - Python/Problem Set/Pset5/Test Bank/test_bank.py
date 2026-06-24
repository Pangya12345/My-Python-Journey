from bank import value

# Test cases for greetings that equal "Hello" or "hello"
def test_Hello():
    # Verify that an uppercase "Hello" returns 0
    assert value("Hello") == 0
    # Verify that a lowercase "hello" returns 0
    assert value("hello") == 0

# Test cases for greetings that start with 'H' or 'h' but are not "Hello"
def test_H_or_h():
    # Verify that a phrase starting with 'H' returns 20
    assert value("How are you doing?") == 20

# Test cases for greetings that do not start with 'H' or 'h'
def test_other():
    # Verify that a phrase starting with any other letter (like 'W') returns 100
    assert value("What's happening") == 100