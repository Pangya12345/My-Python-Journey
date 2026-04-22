from art import logo
print(logo)
print("Welcome to 'Energy Allocation Challenge game!")
teams = {}
stop = False
while not stop:
    team_name = input("What is the name of your team?")
    power = int(input("What is the power? "))
    efficiency = int(input("What is the efficiency? "))
    any_team = input("Are there any team getting involved with this game? type 'yes' or 'no': ").lower()
    if any_team == "yes":
        print("\n" * 100)
    def calculate_final_score(real_power, real_efficiency):
        final_result = real_power * real_efficiency
        return final_result
    teams[team_name] = calculate_final_score(real_efficiency = efficiency, real_power = power)
    teams["efficiency"] = efficiency
    if any_team == "no":
        stop = True
top_score_team = ""
top_score = 0
for name in teams:
    if teams[name] > top_score:
        top_score = teams[name]
        top_score_team = name
        if top_score == teams[name]:
            top_efficiency = 0
            for i in teams:
                if i == "efficiency":
                    if teams[i] > top_efficiency:
                        top_efficiency = top_score_team
print(f"The winner team is {top_score_team} with the final score of {top_score}")

