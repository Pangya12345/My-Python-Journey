Rainny = "🌧️"
Sunny = "☀️"
Snowy = "❄️"

walk = "🚶"
drive = "🚘"
stay = "🏠"

c_choices_image = [Rainny, Sunny, Snowy]
c_choices_word = ["Rainny", "Sunny", "Snowy"]
u_choices_image = [walk, drive, stay]
u_choices_word = ["Walk", "drive", "Stay"]
print("Welcome to the 'Weather decision game!'")
import random
computer_choice = random.randint(0, 2)
print(f"computer chose: {c_choices_word[computer_choice]}")
print(c_choices_image[computer_choice])
user_choice = int(input("What do you think you could do in this weather?\n"
                    "Type 0 for 'walk', Type 1 for 'drive', type 2 for stay at 'home'\n"))
print(f"User chose: {u_choices_word[user_choice]}")
print(u_choices_image[user_choice])

if user_choice >= 3 and user_choice < 0:
    print("You chose the invalid decision!")
elif computer_choice == 0 and user_choice != 1:
    print("This will not work well")
elif computer_choice == 1 and user_choice != 0:
    print("This will not work well")
elif computer_choice == 1 and user_choice > 0:
    print("This does not work well!")
elif computer_choice == 2 and user_choice < 2:
    print("This does not work well!")
elif computer_choice == 0 and user_choice == 1:
    print("This work well!")
elif computer_choice == 1 and user_choice == 0:
    print("This work well!")
elif computer_choice == 2 and user_choice == 2:
    print("This work well!")

print("The game is end")

