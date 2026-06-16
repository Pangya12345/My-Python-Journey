# A dictionary containing the menu items and their corresponding prices
foods_menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Initialize the running total cost of the order
total = 0
stop = False

# Keep prompting the user for items until they signal an end of input
while not stop:
    try:
        # Get user input and convert it to Title Case to match dictionary keys
        item = input("Item: ").title()
        
        # Look up the item's price, add it to the total, and display the new total
        total += foods_menu[item]
        print(f"Total: ${total:.2f}")
        
    except KeyError:
        # If the item is not found in the dictionary, ignore it and prompt again
        pass
        
    except EOFError:
        # If the user signals End-of-File (e.g., Ctrl+D or Ctrl+Z), exit the loop
        break