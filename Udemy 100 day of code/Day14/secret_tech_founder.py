# Define the list of Founder (nested list)
game_data = [
    {"name": "Elon Musk", "company": "Tesla", "field": "Automative", "nationality": "South Africa"},
    {"name": "Sam Altman", "company": "OpenAI", "field": "Generative", "nationality": "America"},
    {"name": "Mark Zuckerberg", "company": "Facebook", "field": "Social Media", "nationality": "America"},
    {"name": "Jack Ma", "company": "Alibaba", "field": "Technology", "nationality": "China"},
    {"name": "Komsan Lee", "company": "Flash", "field": "Delivery", "nationality": "Thailand"},
    {"name": "Liang Wenfeng", "company": "DeepSeek", "field": "Generative", "nationality": "China"},
    {"name": "Pangya Pholphirul", "company": "WinAll", "field": "SportTech", "nationality": "Thailand"},
    {"name": "Bryan Johnson", "company": "Kernal", "field": "Healthcare", "nationality": "America"},
    {"name": "Jirayut Subsrisopa", "company": "Bitkub", "field": "Bitcoin", "nationality": "Thailand"},
    {"name": "Robin Li", "company": "Baidu", "field": "Cloud Computing", "nationality": "China"}
]
# Set up the global variable
print("Welcome to the Secret Tech Founder!")
import random
# Find the founder name by using random in the choice
target = random.choice(game_data)
print(target)
option_left = len(game_data)
question_left = 5
print(f"You have {question_left} questions available")
print(f"Remaining options: {option_left}")
stop = False
# Set up the function that will update the option and question left everytime
def correct_list_update():
    global correct_list
    global question_left
    print(f"Remaining options: {len(correct_list)}")
    print(f"question left: {question_left}")
# Set up the function that will update the global variable (correct_list, question_left) everytime in the function
def global_update():
    global correct_list
    global question_left
# Set up the function that will show the result if the user guess the name of the founder correctly
def game_end_good():
    global stop
    print("Correct! ")
    print("You found the secret Founder!")
    print("Game Over.")
    stop = True
# Set up the function that will show the result if the user can't get the name of the founder correctly
def game_end_bad():
    global stop
    print("Wrong guess!")
    print(f"The correct answer was {target['name']}")
    print("Game Over.")
    stop = True

# Set up the game loop
while not stop:
    correct_list = []
    if question_left == 0:
        stop = True
        print("No Question left!")
        print("You must guess now.")
        final_guess = input("Enter name ").title()
        if final_guess == target["name"]:
            game_end_good()
            break
        elif final_guess != target["name"]:
            game_end_bad()
            break
    print("----------------------------------------")
    question = int(input("1. Ask nationality "
                         "2. Ask field "
                         "3. Ask company "
                         "4. Guess the founder "))
# if the user choose 1 to get the 'nationality' hint
    if question == 1:
        question_left = question_left - 1
# Define the function for this nationality hint
        def nationality_question():
            global_update()
            question_1_input = input("Enter nationality ").title()
# if user guess is equal to 'nationality' of the 'founder name' then the correct founder that have the same nationality including picked founder will append into the list and count it as the number of option left
            if question_1_input == target["nationality"]:
                print("Yes!")
                for i in game_data:
                    if i["nationality"] == question_1_input:
                        correct_list.append(i)
                correct_list_update()
# if user guess is not equal to 'nationality' of the 'founder name' then the correct founder that is not the same as the guess will be append in the correct_list
            elif question_1_input != target["nationality"]:
                print("No!")
                for w in game_data:
                    if w["nationality"] != question_1_input:
                        correct_list.append(w)
                correct_list_update()
        nationality_question()
# if user choose 2 to get the 'field' hint
    elif question == 2:
        question_left = question_left - 1
# define the function for field hint
        def field_question():
            global_update()
            question_2_input = input("Enter field ").title()
# if user guess is equal to 'field' of the 'founder name' then the correct founder that have the same nationality including picked founder will append into the list and count it as the number of option left
            if question_2_input == target["field"]:
                print("yes!")
                for k in game_data:
                    if k["field"] == question_2_input:
                        correct_list.append(k)
                correct_list_update()
# if user guess is not equal to 'field' of the 'founder name' then the correct founder that is not the same as the guess will be append in the correct_list
            elif question_2_input != target["field"]:
                print("No!")
                for r in game_data:
                    if r["field"] == question_2_input:
                        correct_list.append(r)
                correct_list_update()
        field_question()
# if user choose 3 to get company hint
    elif question == 3:
        question_left = question_left - 1
# define the function for company hint
        def company_question():
            global_update()
            global stop
# Ask the user if they really want to guess the company hint
            decide = input("Do you want to guess the company of this Secret founder? type 'Y' or 'N' ").upper()
            if decide == "Y":
# if the user type 'Y'(mean 'yes') the game will ask to guess for the founder company name
                question_2_input = input("Enter Company ").title()
# if the user make the right guess, the game will then ask if the user want to guess the name of the founder or not
                if question_2_input == target["company"]:
                    print("Yes! You guess the right company! you nearly there!")
                    next_step = input("Do you want to guess the name of the founder! type 'Y' or 'N' ").upper()
                    if next_step == 'Y':
                        founder_guess = input("What was the full name of the founder? ").title()
# if the user can guess the name of the founder, the game is end and the user win!
                        if founder_guess == target["name"]:
                            game_end_good()
                            stop = True
# if the user cannot guess the name of the founder, the game is end but the user is lost!
                        elif founder_guess != target["name"]:
                            game_end_bad()
# if the user type 'N'(mean 'No') the game will continue
                    elif next_step == "N":
                        correct_list_update()
# if the user did not guess the name of the 'founder company' then the correct founder that is not the same as the guess will be append in the correct_list
                elif question_2_input != target["company"]:
                    print("No!")
                    for t in game_data:
                        if t["company"] == question_2_input:
                            correct_list.append(t)
                    correct_list_update()
            elif decide == "N":
                print("That's Ok go for more!")

        company_question()
# if user choose 4 to guess the founder name straight away
    elif question == 4:
        question_left = question_left - 1
# define the function for founder guess
        def founder_question():
            global stop
            global_update()
            question_4_input = input("Enter your founder guess name ").title()
# if the user make the right guess, the game is end and the user win!
            if question_4_input == target["name"]:
                game_end_good()
# if the user did not make the right guess, the game is end and the user lost!
            elif question_4_input != target["name"]:
                game_end_bad()
        founder_question()

