# Import the necessary information from other file such as "Random, logo art, vs art and the data"
import random
from art import logo
from art import vs
from game_data import data
score = 0
used = []
random_A = random.randint(0, 49)
random_B = random.randint(0, 49)
while random_B == random_A:
    random_B = random.randint(0, 49)
    random_A = random.randint(0, 49)
stop = False
# Define the function to repeat putting A at the top if A is more than B
while not stop:
    def repeat_A_top():
        print(f"Compare A: {data[random_A]["name"]}, a {data[random_A]["description"]}, from {data[random_A]['country']}")
        print(vs)
        print(f"Against B: {data[random_B]["name"]}, a {data[random_B]["description"]}, from {data[random_B]['country']}")
# Define the function to repeat putting B at the top if B is more than A
    def repeat_B_top():
        print(f"Compare A: {data[random_B]["name"]}, a {data[random_B]["description"]}, from {data[random_A]['country']}")
        print(vs)
        print(f"Against B: {data[random_A]["name"]}, a {data[random_A]["description"]}, from {data[random_A]['country']}")
# Define the function to update score if player make the right guess
    def right_answer():
        global score
        print("\n" * 10)
        score = score + 1
        print(logo)
        print(f"You're right Current score: {score}")
# Define the function to stop if user make the wrong guess
    def stop_game():
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
# Define the function if the user guess correct by B > A and need to place B at the top
    def correct_continue_B_top():
        global random_A
        random_A = random.randint(0, 49)
        right_answer()
        repeat_B_top()
# Define the function if the user guess correct by A > B and need to place A at the top
    def correct_continue_A_top():
        global random_B
        random_B = random.randint(0, 49)
        right_answer()
        repeat_A_top()
# Implement those function above for the game logic
    print(logo)
    repeat_A_top()
    question_1 = input("Who has more followers? Type 'A' or 'B': ").upper()
# If user choose "A" and follower of A is < B or if user choose "B" and follower of is < A: then the game need to be stop and done
    if question_1 == "A" and data[random_A]["follower_count"] < data[random_B]["follower_count"] or question_1 == "B" and data[random_B]["follower_count"] < data[random_A]["follower_count"]:
        stop_game()
        stop = True
# If user choose "A" and follower of A is > B then it will replace the top with A and random the new B and we enter the while loop for the new condition
    elif question_1 == "A" and data[random_A]["follower_count"] > data[random_B]["follower_count"]:
        correct_continue_A_top()
        while True:
            question_2= input("Who has more followers? Type 'A' or 'B': ").upper()
# If user choose "A" and follower of A is < B or if user choose "B" and follower of is < A: then the game need to be stop and done
            if question_2 == "A" and data[random_A]["follower_count"] < data[random_B]["follower_count"] or question_2 == "B" and data[random_B]["follower_count"] < data[random_A]["follower_count"]:
                stop_game()
                stop = True
                break
# If the user choose "A" and A is > B then we put the same A at the top
            elif question_2 == "A" and data[random_A]["follower_count"] > data[random_B]["follower_count"]:
                correct_continue_A_top()
                continue
# If the user choose "B" and B is > A then we put B at the top (to become A) and define the new A to become B
            elif question_2 == "B" and data[random_A]["follower_count"] < data[random_B]["follower_count"]:
                correct_continue_B_top()
                while True:
                    question_4 = input("Who has more followers? Type 'A' or 'B': ").upper()
                    if question_4 == "A" and data[random_A]["follower_count"] > data[random_B]["follower_count"] or question_4 == "B" and data[random_A]["follower_count"] < data[random_B]["follower_count"]:
                        stop_game()
                        stop = True
                        break

                    elif question_4 == "A" and data[random_B]["follower_count"] < data[random_A]["follower_count"]:
                        correct_continue_B_top()
                        continue

                    elif question_4 == "B" and data[random_B]["follower_count"] > data[random_A]["follower_count"]:
                        correct_continue_A_top()
                        continue
# If A = B then the game automatically end
                    elif data[random_A]["follower_count"] == data[random_B]["follower_count"]:
                        stop_game()
                        stop = True
                        break
# # If user choose "B" and follower of B is > A then it will replace the top with previous B and random the new A to become the new B and we enter into the while loop for new condition
    elif question_1 == "B" and data[random_A]["follower_count"] < data[random_B]["follower_count"]:
        correct_continue_B_top()
        while True:
# If user choose "A" and follower of A is < B or if user choose "B" and follower of is < A: then the game need to be stop and done
            question_3 = input("Who has more followers? Type 'A' or 'B': ").upper()
# If user choose "A" and follower of A is > B then it will replace the top with A and random the new B and we enter the while loop for the new condition
            if question_3 == "A" and data[random_A]["follower_count"] > data[random_B]["follower_count"] or question_3 == "B" and data[random_B]["follower_count"] > data[random_A]["follower_count"]:
                stop_game()
                stop = True
                break
# If the user choose "A" and A is > B then we put the same A at the top
            elif question_3 == "A" and data[random_A]["follower_count"] < data[random_B]["follower_count"]:
                correct_continue_B_top()
                continue
# If the user choose "B" and B is > A then we put B at the top (to become A) and define the new A to become B
            elif question_3 == "B" and data[random_A]["follower_count"] > data[random_B]["follower_count"]:
                correct_continue_A_top()
                continue
# If the user A = B the game is automatically end and user need to restart the game
            elif data[random_A]["follower_count"] == data[random_B]["follower_count"]:
                stop_game()
                stop = True
                break
    elif data[random_A]["follower_count"] == data[random_B]["follower_count"]:
        stop_game()
        stop = True










