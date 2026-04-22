# Import logo from art.py and print it out
from art import logo
print(logo)
print("Welcome to the 'Talent Auction game'")
# Set_up the dictionary tp stored the data inside
data = {}
stop = False
# Set up the 'while' loop to ask the user for information to put into the dictionary
while not stop:
# calculate the total score with the original referee
    total = 0
    name = input("What is the name of contest\n")
    referee = input("What is your name? (referee)\n")
    score = int(input("How much score you would like to give to this contest\n"))
    data[name] = {referee: score}
    total = total + score
# Ask the user is there anymore referee they want to add more to give the score to their contest
    continue_asking = input("Would you like to put in some more referee in this contest? type 'yes' or 'no'\n").lower()
    if continue_asking == "no":
        anymore_contest = input("Are there anymore contest joining this auction? type 'yes' or 'no'\n").lower()
        if anymore_contest == "yes":
            print("\n" * 100)
        elif anymore_contest == "no":
            stop = True
        data[name]["Total Score"] = total
    elif continue_asking == "yes":
        print("\n" * 100)
# if the user type 'yes' then ask the user for the new referee name
        direction = False
        while not direction:
# calculate the total_score for new referee combine with old referee (original_referee_score + new_referee_score)
            final_total = 0
            new_referee = input("What is your name? (new referee!)\n")
            new_score = int(input("How much score would you like to give to this contest?\n"))
            real_total = score + new_score
            if real_total > final_total:
                final_total = real_total
                data[name][new_referee] = new_score
                data[name]["Total Score"] = final_total
# asked the user is there anymore referee they want to put in the contest if 'yes' then do the following code
            anymore = input("You want to put anymore referee to give more score in this contest? type 'yes' or 'no'\n").lower()
            if anymore == "no":
                direction = True
# asked the user is there anymore contest joining this game
                anymore_contest = input("Are there any more contest joining this auction? type 'yes' or 'no'\n").lower()
                if anymore_contest == "yes":
                    print("\n" * 100)
                elif anymore_contest == "no":
                    stop = True
                    direction = True
            elif anymore  == "yes":
                print("\n" * 100)
print(data)

top_score = 0
top_contest = ""
for key in data:
    if data[key]["Total Score"] > top_score:
        top_score = data[key]["Total Score"]
        top_contest = key
print(f"The winner is {top_contest} with the total score of {top_score}")
