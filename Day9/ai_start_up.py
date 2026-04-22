from art import logo
print(logo)
print("Welcome to 'AI Start Pitch Battle!")
Start_up = {}
stop = False
while not stop:
    team_name = input("What is the name of your start-up team?\n")
    Start_up[team_name] = []
    score_idea = int(input("How many idea score you get for your team?\n"))
    Start_up[team_name].append({"Score": score_idea})
    team_score = int(input("How many teams score you get for your team?\n"))
    Start_up[team_name].append({"Team Score": team_score})
    investment_amount = float(input("How many amount of money that you would like to offer to the investors?\n"))
    Start_up[team_name].append({"Investment amount": investment_amount})
    go_ahead = input("Is there any team joining this competition? type 'yes' or 'no'\n").lower()

    if go_ahead == "no":
        stop = True
    elif go_ahead == "yes":
        print("\n" * 100)

    def calculate_team_final_score(idea, team, investment):
        final_score = (idea * 2) + (team * 2) - (investment / 1000)
        return final_score
    real_final_score = calculate_team_final_score(investment = investment_amount, team = team_score, idea = score_idea)
    Start_up[team_name].append({"Final Score": real_final_score})
print(Start_up)
top_score = 0
top_score_team_name = ""
for key in Start_up:
    for i in Start_up[key][3]:
        if Start_up[key][3][i] > top_score:
            top_score = Start_up[key][3][i]
            top_score_team_name = key
print(f"The winner team is {top_score_team_name} with the final score of {top_score}")





