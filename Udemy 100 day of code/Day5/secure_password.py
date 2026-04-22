print("Welcome to the Secure password and validator!")
password = input("Enter the password: ")

letters = ""
Numbers = ""
Symbols = ""

for haha in password:
    if 'a' <= haha <= 'z' or 'A' <= haha <= 'Z':
        letters += haha
    elif haha == "0" or haha == "1" or haha == "2" or haha == "3" or haha == "4" or haha == "5" or haha == "6" or haha == "7" or haha == "8" or haha == "9":
        Numbers += haha
    elif haha == "!" or haha == "#" or haha == "$" or haha == "%" or haha == "$" or haha == "%" or haha == "&" or haha ==  "(', ')" or haha == ")" or haha == "*" or haha == "+":
        Symbols += haha

print(f"Letters: {len(letters)}")
print(f"Numbers: {len(Numbers)}")
print(f"Symbols: {len(Symbols)}")

score = 0

if len(letters) >= 1:
    score += 2
if len(Numbers) >= 1:
    score += 2
if len(Symbols) >= 1:
    score += 3
if len(password) >= 12:
    score += 3

print(f"Score: {score}")

if 0 <= score <= 3:
    strength = "Weak"
elif 4 <= score <= 7:
    strength = "Medium"
elif 8 <= score <= 10:
    strength = "Strong"

print("Password strength:", strength)








