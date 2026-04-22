#Computer Random element Choice:
fire = "🔥"
water = "💧"
earth = "🌏"
shadow = "⚫"
wind = "💨"

#User element choice:
inferno = "💥"
tidal_wave = "🌊"
storm_call = "🌪️"
stone_guard = "🗿"
light_seal = "💡"

#Assigning the lists (computer and user choices)
import random
print("Welcome to the circle of element game! ")
computer_elements_word = ["fire", "water", "earth", "shadow", "wind"]
computer_elements_image = [fire, water, earth, shadow, wind]
user_elements_word = ["inferno", "tidal_wave", "storm_call", "stone_guard", "light_seal"]
user_elements_image = [inferno, tidal_wave, storm_call, stone_guard, light_seal]
c_element = random.randint(0, 4)
print(f"Computer element are {computer_elements_word[c_element]}")
print(computer_elements_image[c_element])

u_element = int(input("Please choose the element power to compete with the computer element."
                      "Type 0 for Inferno(massive amount of fire), Type 1 for Tidal wave(Massive wave), Type 2 for Storm call(massive storm),"
                      "Type 3 for Stone guard(The strongest stone in the world!), Type 4 for light seal(The light that can heal anything)\n"))
print(f"User chose: {user_elements_word[u_element]}")
print(user_elements_image[u_element])

if 0 > u_element > 4:
    print("You chose an invalid element.")
elif c_element == 3 and u_element == 0 or u_element == 1 or u_element == 2 or u_element == 3:
    print("You lost!")
    print("Shadow consumes and overwhelms elemental power.")
elif c_element == 3 and u_element == 4:
    print("You win!")
    print("Light purifies and seals the shadow.")
elif c_element == 0:
    if u_element == 1:
        print("You win!")
        print("Water extinguishes the fire.")
    elif u_element == 2:
        print("You lost!")
        print("Fire burn and disturb the win.")
    elif u_element == 0 or u_element == 3 or u_element == 4:
        print("stalemate (No one lose, No one win.)")
        print("These 2 element are not active with each other.")
elif c_element == 1:
    if u_element == 0:
        print("You lost!")
        print("Water extinguishes the fire.")
    elif u_element == 3:
        print("You win!")
        print("Earth absorbs and contains the water.")
    elif u_element == 1 or u_element == 2 or u_element == 4:
        print("Stalemate (No one lose, No one win.)")
        print("These 2 element are not active with each other.")
elif c_element == 2:
    if u_element == 1:
        print("You lost!")
        print("Earth absorbs and contains the water.")
    elif u_element == 2:
        print("You win!")
        print("Wind erodes and wears down the earth.")
    elif u_element == 3 or u_element == 1 or u_element == 4:
        print("Stalemate (No one lose, No one win.)")
        print("These 2 element are not active with each other.")
elif c_element == 4:
    if u_element == 3:
        print("You lost!")
        print("Wind erodes and wears down the earth.")
    elif u_element == 0:
        print("You win!")
        print("Fire burn and disturb the win.")
    elif u_element == 2 or u_element == 1 or u_element == 4:
        print("stalemate (No one lose, No one win.")
        print("These 2 element are not active with each other.")












