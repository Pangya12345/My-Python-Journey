print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You at a cross road. Where do you want to go? Type 'L' for left and type 'R' for right")
if direction == "R":
    print("You fell into a hole. Game over!")
elif direction == "L":
    decision = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim across ")
    if decision == "wait":
        house_door = input("You've arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Type R, Y or B ")
        if house_door == "Y":
            print("You found a treasure! you win!")
        elif house_door == "B":
            print("You get attack by the zombie! Game over!")
        elif house_door == "R":
            print("House full of fire! Game over!")
        else:
            print("You choose the door that does not exist! Game over!")
    elif decision == "swim":
        print("You got attack by shark! Game over!")
else:
    print("You have no where to go! Game over!")


