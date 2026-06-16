# Initialize an empty dictionary to store grocery items and their quantities
grocery_list = {}
stop = False

# Loop to continuously take user input until an End-of-File (EOF) signal is received
while not stop:
    try:
        # Read input and convert it to uppercase to ensure case-insensitive matching
        item = input().upper()
        
        # If the item is already in the dictionary, increment its count
        if item in grocery_list:
            grocery_list[item] += 1
        # Otherwise, add the item to the dictionary with an initial count of 1
        else:
            grocery_list[item] = 1

    except EOFError:
        # Stop the loop when the user signals End-of-File (e.g., Ctrl+D or Ctrl+Z)
        stop = True

# Iterate through the dictionary and print the total quantity followed by the item name
for i in grocery_list:
    print(f"{grocery_list[i]} {i}")