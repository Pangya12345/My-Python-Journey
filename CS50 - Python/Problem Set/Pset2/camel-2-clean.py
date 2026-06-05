# Set up the capital information
real_text = ""
letter_info = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
text = input("camelCase : ")

# Use for to check if the text contain capital letter or not
for i in text:

    # If the text contain capital letter ----> add space ------>  add text
    if i in letter_info:
        real_text += "_"
        real_text += i

    # If it does not -------> add text
    else:
        real_text += i

# Clean up final text and print
real_text_made = real_text.lower()
print(f"snake_case: {real_text_made}")
