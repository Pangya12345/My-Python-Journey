from twttr import shorten

# List of vowels used by the main application for reference
vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

# Test cases for mixed-case words with missing vowels
def test_lower_check():
    # Verify that a word already missing standard vowels remains unchanged
    assert shorten("Twttr") == "Twttr"

# Test cases for numbers and uppercase non-vowel strings
def test_upper_check():
    # Verify that numbers and uppercase consonants are left untouched
    assert shorten("CS50") == "CS50"

# Test cases for full sentences, punctuation, and spaces
def test_odd_check():
    # Verify that punctuation, spaces, and vowels are handled correctly in a sentence
    assert shorten("What's your name?") == "Wht's yr nm?"

# Test cases for mixed-case vowel stripping
def test_capital_check():
    # Verify that both lowercase and uppercase vowels (like 'O') are successfully stripped
    assert shorten("PythOn") == "Pythn"
