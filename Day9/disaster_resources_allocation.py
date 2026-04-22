from art import logo
print(logo)
print("Welcome to the 'Disaster Resources Allocation' game!")
data = {}
stop = False
while not stop:
    team_name = input("What is the name of your team?\n")
    data[team_name] = {}
    water_amount = int(input("How many water amount your team have left?\n"))
    data[team_name]["water"] = water_amount
    food_amount = int(input("How many food do you have left?\n"))
    data[team_name]["food"] = food_amount
    medicine_amount = int(input("How many medicine amount that your team has left?\n"))
    data[team_name]["medicine"] = medicine_amount
    should_continue = input("Is there anymore team joining this game? type 'yes' or 'no'\n").lower()
    if should_continue == "no":
        stop = True
    elif should_continue == "yes":
        print("\n" * 100)

    def calculate_team_score(water, medicine, food):
        sum_of_everything = water + medicine + food
        return sum_of_everything
    data[team_name]["Total Score"] = calculate_team_score(food = food_amount, medicine = medicine_amount, water = water_amount)
print(data)
top_score = 0
top_score_team = ""
for key in data:
    if data[key]["Total Score"] > top_score:
        top_score = data[key]["Total Score"]
        top_score_team = key
print(f"The winner team is {top_score_team} with the final score of {top_score}")


