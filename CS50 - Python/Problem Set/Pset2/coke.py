
coke_price = 50 # -------> Set up coke price 
total_input_amount = 0 # -------> Set up the total input amount 

while coke_price > 0: # Set up the loop (coke price > 0)
  print(f"Amount Due: {coke_price}")

# Ask for the user input and make a condition
  amount = int(input("Insert Coin: "))
  if amount == 10 or amount == 25 or amount == 5:
    total_input_amount += amount
    coke_price = coke_price - amount
  elif amount != 10 or amount != 25 or amount != 5:
    coke_price = coke_price

# Make a condition and calculate the change
if total_input_amount > 50:
  nume = total_input_amount - 50
  print(f"Change Owed: {nume}")

elif total_input_amount == 50:
  print("Change Owed: 0")