from art import logo
print(logo)
print("Welcome to the 'Resource Survival Simulator game!'")
teams = {}
stop = False
while not stop:
    team_name = input("What is the name of the team?\n")
    food = int(input("How many amount of food do you have left?\n"))
    water = int(input("How many water do you have?\n"))
    member = int(input("How many member in your team?\n"))
    teams["Team"] = team_name
    teams["Food"] = food
    teams["Water"] = water
    teams["Member"] = member
    should_continue = input("Are there any team that want to join in this game. type 'yes' or 'no' ").lower()
    def calculate_resource_per_person(food_amount, water_amount, member_number):
        resource_per_person = (food_amount + water_amount) / member_number
        return resource_per_person
    teams["Resources per person"] = calculate_resource_per_person(member_number = member, water_amount = water, food_amount = food)
    if should_continue == "yes":
        print("\n" * 100)
    elif should_continue == "no":
        stop = True
survived_team = []
for team in teams:
    if teams[team]["Resources per person"] >= 10:
        survived_team.append(team)
top_team_score = 0
top_team_name = ""
for i in survived_team:
    if teams[i]["member"] > top_team_score:
        top_team_score = teams[i]["member"]
        top_team_name = i
        if top_team_score == teams[i]["member"]:
            if teams[i]["Resources per person"] > top_team_score:
                top_team_score = teams["Resources per person"]
                top_team_name = i
    else:
        print("No team survived!")
print(f"The winner is {top_team_name}")
