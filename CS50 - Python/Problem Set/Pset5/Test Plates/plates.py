# Set up and import all of necessary tools
def is_valid(plate):
    # Lists of allowed valid characters (Note: missing 'U', 'V', 'T' from alphabet)
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "W", "X", "Y", "Z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    # Store everything from the third character onward
    rest = plate[2:]

    # Check plate length condition (must be between 2 and 6 characters inclusive)
    def lenght_check():
        if 2 <= len(plate) <= 6:
            return True
        else:
            return False

    # Check plate first and second letters (both must be valid uppercase letters)
    def characters_check():
        if plate[0] in letters and plate[1] in letters:
            return True
        else:
            return False

    # Filter out plates that have a length of 2 or 3 to change validation paths
    def lenght_cut():
        if 2 <= len(plate) <= 3:
            return False
        else:
            return True

    # Check for correct placement of numbers and zeros
    def number_check():
        # Check '0' in front condition: '0' cannot appear before any non-zero number
        for t in rest:
            if "0" in rest and t in numbers:
                if rest.index("0") < rest.index(t):
                    return False
                else:
                    continue

        # Check numbers in front condition for each type of length
        count = 3
        if count == 3:
            # If remaining characters are 2 (Total length of 4)
            if len(rest) == 2:
                # Invalid if a number is followed by a letter
                if rest[0] in numbers and rest[1] in letters:
                    return False
                else:
                    return True
            else:
                count = count - 1
                if count == 2:
                    # If remaining characters are 3 (Total length of 5)
                    if len(rest) == 3: 
                        # Invalid if a number precedes a letter at any position
                        if (rest[0] in numbers and rest[1] in letters) or (rest[1] in numbers or rest[2] in letters):
                            return False
                        else:
                            return True
                    else:
                        count = count - 1
                        if count == 1:
                            # If remaining characters are 4 (Total length of 6)
                            if len(rest) == 4: 
                                # Invalid if a number precedes a letter anywhere in the sequence
                                if (rest[0] in numbers and rest[1] in letters) or (rest[1] in numbers and rest[2] in letters) or (rest[2] in numbers and rest[3] in letters):
                                    return False
                                else:
                                    return True

    # Evaluate all conditions to determine if the vanity plate is valid
    # Note: 'lenght_check' without parentheses evaluates as a truthy function reference
    if lenght_check() and lenght_check and lenght_cut() and number_check():
        return True
    else:
        return False




