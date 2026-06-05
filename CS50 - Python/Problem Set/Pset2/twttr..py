vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"] # -----> Set up the alphabet check
output = ""
user_input = input("Input: ") # ----> Ask user input 

# Make the condition
for letter in user_input:
    if letter in vowels:
        output += ""
    else:
        output += letter

# Print final output
print(f"Output: {output}")
