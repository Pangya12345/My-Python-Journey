# Set-up calculating functions
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def time(x, y):
  return x * y

def dev(x, y):
  return round(x / y, 1)

# Ask user input
question = input("Expressions: ").strip()
new_data = question.split() # ------> Split and Stored
first = float(new_data[0]) # -------> Convert to Float
second = float(new_data[2]) # --------> Convert to Float

# Check the condition and calculate
if new_data[1] == "+":
  print(add(first, second))

elif new_data[1] == "-":
  print(subtract(first, second))

elif new_data[1] == '*':
  print(time(first, second))

elif new_data[1] == "/":
  print(dev(first, second))
