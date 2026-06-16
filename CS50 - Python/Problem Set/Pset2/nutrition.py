# Set up Fruit Dictionary
fruit_dict = {"Apple": 130, "Avocado": 50, "Banana": 110, "Cantaloupe": 50, "Grapefruit": 60, "Grapes": 90, "Honeydew Melon": 50, "Kiwifruit": 90, "Lemon": 15, "Lime": 20, "Nectarine": 60, "Orange": 80, "Peach": 60, "Pear": 100, "Pineapple": 50, "Plums": 70, "Strawberries": 50, "Sweet Cherries": 100, "Tangerine": 50, "Watermelon": 80}
fruit_name = input("Item: ").title() # ----------> Ask user for the name of the fruit

if fruit_name in fruit_dict:
  print(f"Calories: {fruit_dict[fruit_name]}") # -----> Print out the calories of the fruit
else:
  print("") # ---------> Print nothing if the input name does not contain

