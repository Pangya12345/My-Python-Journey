from fuel import convert, gauge

# Test that convert() properly raises a ZeroDivisionError when denominator is 0
def test_ZeroDivision():
    try:
        convert("1/0")
        assert False  # If no error is raised, force the test to fail
    except ZeroDivisionError:
        assert True   # The test passes if a ZeroDivisionError is successfully caught

# Test that convert() properly raises a ValueError for invalid fractions
def test_ValueError():
    try:
        convert("5/4")   # X > Y should trigger a ValueError
        convert("-1/3")  # X < 0 should trigger a ValueError
        assert False     # If no error is raised, force the test to fail
    except ValueError:
        assert True      # The test passes if a ValueError is successfully caught

# Test that gauge() correctly formats various percentage outputs
def test_Percent():
    # Verify the "Empty" threshold (<= 1%)
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    
    # Verify the "Full" threshold (>= 99%)
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    
    # Verify that standard percentages return formatted string values
    assert gauge(45) == "45%"
    assert gauge(87) == "87%"