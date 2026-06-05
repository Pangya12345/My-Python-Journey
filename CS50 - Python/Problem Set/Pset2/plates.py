# Set up and import all of necessary tools
import sys  # -----> Import sys to control the stop condition
plate = input("Plate: ")
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
rest = plate[2:]

# Check plate lenght condition (2-6)
def lenght_check():
  if 2 <= len(plate) <= 6:
    return True

  else:
    print("Invalid")

# Check plate first and second letters (must be A-Z!)
def characters_check():
  if plate[0] in letters and plate[1] in letters:
    return True
  else:
    print("Invalid")

# Check if the plate lenght is 2 or 3
def lenght_cut():
  if 2 <= len(plate) <= 3:
    print("Valid")

  else:
    return True


# Check all of the numbers conditions
# 1. First number being use cannot be 0
# 2. Numbers cannot be in the middle of the plate
# 3. Numbers must come at the end of the plate not in the start of the plate

def number_check():

# Check 0 infront condition
  for t in rest:
    if "0" in rest and t in numbers:
      if rest.index("0") < rest.index(t):
        print("Invalid")
        sys.exit()
      else:
        continue

# Check numbers infront condition for each type of lenght
  count = 3
  if count == 3:
    if len(rest) == 2: # ------> If plate lenght = 4
      if rest[0] in numbers and rest[1] in letters:
          print("Invalid")
      else:
        return True
    else:
      count = count - 1
      if count == 2:
        if len(rest) == 3: # -------> If plate lenght = 5
          if (rest[0] in numbers and rest[1] in letters) or (rest[1] in numbers or rest[2] in letters):
            print("Invalid")
          else:
            return True
        else:
          count = count - 1
          if count == 1:
            if len(rest) == 4: # -------> If plate lenght = 6
              if (rest[0] in numbers and rest[1] in letters) or (rest[1] in numbers and  rest[2] in letters) or (rest[2] in numbers and rest[3] in letters):
                print("Invalid")
              else:
                return True





# Check all of the functions condition
if lenght_check():
    if characters_check():
        if lenght_cut():
            if number_check():
                print("Valid") # -------> If everything met the condition ----> print "Valid"