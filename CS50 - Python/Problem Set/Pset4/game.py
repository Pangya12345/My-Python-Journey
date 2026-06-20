import random

# ---- Set up the Level Selection Loop ----
while True:
    level = input("Level: ")
    
    # Check if the input consists only of digits
    if level.isdigit():
        level_num = int(level)
        
        # Ensure the level is a positive integer greater than 0
        if level_num > 0:
            correct_number = random.randint(1, level_num)
            break  # Successfully set the level, exit the loop
            
    # If the input contains letters, symbols, or is <= 0, the loop automatically repeats

# ---- Set up the Guessing Loop ----
while True:
    guess = input("Guess: ")
    
    # Check if the guess consists only of digits
    if guess.isdigit():
        guess_num = int(guess)
        
        # Ignore numbers that are 0 or negative
        if guess_num <= 0:
            continue
            
        # Check the guess against the correct number
        if guess_num > correct_number:
            print("Too large!")
        elif guess_num < correct_number:
            print("Too small!")
        else:
            print("Just right!")
            break  # Correct guess, exit the game
            
    # If the input contains letters or symbols, the loop automatically repeats


  



