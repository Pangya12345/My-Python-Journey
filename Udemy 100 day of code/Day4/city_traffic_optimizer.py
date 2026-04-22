low = "😊"
medium = "😐"
high = "🙁"

clear = "🧹"
rain = "🌧️"
fog = "🌫️"

normal_light = "🚦"
longer_green = "🟢"
emergency_mode = "🚨"

Traffic_level_image = [low, medium, high]
Traffic_level_word = ["low", "medium", "high"]
Weather_image = [clear, rain, fog]
Weather_word = ["clear", "rain", "fog"]
Light_type_image = [normal_light, longer_green, emergency_mode]
Light_type_word = ["normal_light", "longer_green", "emergency_mode"]

print("Welcome to the City traffic optimizer game!")
import random
c_traffic = random.randint(0,2)
print(f"Traffic is: {Traffic_level_word[c_traffic]}")
print(Traffic_level_image[c_traffic])
c_weather = random.randint(0, 2)
print(f"Weather is: {Weather_word[c_weather]}")
print(Weather_image[c_weather])

user_light_choice = int(input("choose the appropriate light type Type 0 for 'normal light', Type 1 for 'longer green', Type 2 for 'emergency mode'\n"))
print(f"user chose: {Light_type_word[user_light_choice]}")
print(Light_type_image[user_light_choice])

if 0 > user_light_choice > 2:
    print("You chose the invalid light type!")
elif c_traffic == 0 and c_weather == 0:
    if user_light_choice != 0:
        print("This not gonna work well!")
    else:
        print("This will work well")
elif c_traffic == 2 and c_weather == 0:
    if user_light_choice != 1:
        print("This not gonna work well!")
    else:
        print("This will work well!")
elif c_traffic == 2 and c_weather == 2:
    if user_light_choice != 2:
        print("This not gonna work well!")
    else:
        print("This will work well!")
elif c_traffic == 1 and c_weather == 0:
    if user_light_choice != 1:
        print("This not gonna work well!")
    else:
        print("This will work well!")
elif c_traffic == 1 and c_weather == 1 or c_weather == 2:
    if user_light_choice != 1:
        print("This not gonna work well!")
    else:
        print("This will work well!")

print("The game is end!")
