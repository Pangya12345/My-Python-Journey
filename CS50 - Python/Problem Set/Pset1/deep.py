text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip() # ----------> Ask user Question


forty = "forty two"
forty_next = "forty-two" # --------> set up the mutable answer

if text == "42":
  print("Yes") # ---------> Print "Yes" if user type "42"

# Print "Yes" or "No" if the user input met the condition
elif text == forty or text == forty.title():
  print("Yes")

elif text == forty_next or text == forty_next.title():
  print("yes")
elif text.lower == forty or text.lower == forty_next:
  print("Yes")

elif text.lower().title() == forty.title() or text.lower().title() == forty_next.title():
  print("Yes")

else:
  print("No")
