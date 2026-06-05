# Set up the comapare list and final text
final_text = ""
compare = []

# Set up the list of capital letters
letter_info = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
text = input("camelCase ").strip().replace("", " ").lstrip().rstrip()

# Use for to create the mark for the space
for i in text:
    compare.append(i)
    for k in compare:
        if k in letter_info:
            compare[compare.index(k) - 1] = "*"

# Put all of the character in final_text
for r in compare:
    final_text += r

# Clean up the final text and print
time = final_text.replace("*", "_").replace(" ", "").lower()
print(f"snake_case: {time}")