letters = ""
Numbers = ""
Spaces = ""

print('Welcome to Messsege cleaner system!')
message = input("Enter messege: ")

for pan in message:
    if 'a' <= pan <= 'z' or 'A' <= pan <= 'Z':
        letters += pan
    elif '0' <= pan <= '9':
        Numbers += pan
    else:
        Spaces += pan
        real_spaces = len(Spaces)


print(f"Letters: {letters}")
print(f"Numbers: {Numbers}")
print(f"Spaces: {real_spaces}")


