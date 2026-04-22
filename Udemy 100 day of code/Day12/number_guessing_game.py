import random
correct_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulity = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulity == "easy":
    attempt = 10
elif difficulity == "hard":
    attempt = 5
else:
    print("Invalid difficulty!")
def condition_game():
    stop = False
    global attempt
    global correct_number
    while not stop:
        print(f"You have {attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if 0 >= guess > 100:
            print("Invalid guess (you need to guess the number between 0-100")
        elif guess > correct_number and attempt == 1:
            stop = True
            print("you've run out of guesses. Refresh the page to run again.")
        elif guess < correct_number and attempt == 1:
            stop = True
            print("you've run out of guesses. Refresh the page to run again.")
        elif guess < correct_number:
            print("Too low")
            print("Guess again")
            attempt -= 1
        elif guess > correct_number:
            print("Too high")
            print("Guess again")
            attempt -= 1
        elif guess == correct_number:
            stop = True
            print(f"You got it! the answer is {correct_number}")
condition_game()

