vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"] # -----> Set up the alphabet check
user_input = input("Input: ") # ----> Ask user input

def shorten(u_input):
    output = ""
    for letter in u_input:
        if letter in vowels:
            output += ""
        else:
            output += letter
    return output


# Print final output
print(f"Output: {shorten(user_input)}")
