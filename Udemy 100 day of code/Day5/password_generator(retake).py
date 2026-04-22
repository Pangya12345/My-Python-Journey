import random
elements = ["Fire", "Water", "Earth"]
user_choice = input("What element you would like to use?\n").title()
c_choice = random.choice(elements)

if user_choice == c_choice:
    print(f"You chose {user_choice}\n"
          f"Computer chose {c_choice}\n"
          f"tied!")
if user_choice == "Fire":
    if c_choice == "Water":
        print(f"You chose {user_choice}\n"
              f"Computer chose {c_choice}\n"
              f"You loss!")
    if c_choice == "Earth":
        print(f"You chose {user_choice}\n"
              f"Computer chose {c_choice}\n"
              f"You win!")
elif user_choice == "Water":
    if c_choice == "Fire":
        print(f"You chose {user_choice}\n"
          f"Computer chose {c_choice}\n"
          f"You win!")
    if c_choice == "Earth":
        print(f"You chose {user_choice}\n"
              f"Computer chose {c_choice}\n"
              f"You loss!")
elif user_choice == "Earth":
    if c_choice == "Fire":
        print(f"You chose {user_choice}\n"
              f"Computer chose {c_choice}\n"
              f"You loss!")
    if c_choice == "Water":
        print(f"You chose {user_choice}\n")
        print(f"Computer chose {c_choice}\n")
        print(f"You win!")

else:
    print("You put invalid element!")






