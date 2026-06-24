def shorten(u_input):
    # Initialize an empty string to store the text without vowels
    output = ""
    
    # Loop through each individual character in the user's input
    for letter in u_input:
        # If the character is a vowel, skip it (append nothing)
        if letter in vowels:
            output += ""
        # If the character is a consonant, number, or symbol, keep it
        else:
            output += letter
            
    # Return the final string with all vowels removed
    return output
