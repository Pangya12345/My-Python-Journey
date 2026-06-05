greet = input("Greeting: ").strip() # --------> Ask for the user input
test = ""
for k in range(5):
  test += greet[k] # ---------> Create the string comparison

# Check the condition
if test == "Hello" or test == "hello":
  print("$0")

elif test[0] == "h" or test[0] == "H":
  print("$20")

<<<<<<< HEAD
# What to do if the condition does not match 
=======
# What to do if the condition does not match
>>>>>>> 11d66b4cbf65015f8e250c86c7851b9bd4fdb5b2
else:
  print("$100")
