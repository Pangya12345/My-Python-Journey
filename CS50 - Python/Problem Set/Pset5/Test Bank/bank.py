def value(greet):
    # Initialize an empty string to store the first 5 characters
    test = ""
    
    # Loop through the first 5 indices to extract the beginning of the greeting
    for k in range(5):
        test += greet[k]

    # Check if the extracted 5-character string matches "Hello" (case-insensitive for 'h')
    if test == "Hello" or test == "hello":
        return 0

    # If it's not "Hello", check if the very first character starts with an 'h' or 'H'
    elif test[0] == "h" or test[0] == "H":
        return 20

    # If it doesn't start with 'h' or 'H' at all, return 100
    else:
        return 100