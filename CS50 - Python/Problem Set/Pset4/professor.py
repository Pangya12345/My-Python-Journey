import random

# Global variables to track the math problems and valid difficulty levels
question_list = []
number_list = ["1", "2", "3"]

# ---- 1. GET THE DIFFICULTY LEVEL ----
while True:
    level = input("Level: ")
    # Ensure the user types 1, 2, or 3
    if level in number_list:
        real_level = int(level)
        break  # Exit loop if valid
    else:
        continue  # Ask again if invalid

# These string digits are used to build the minimum and maximum ranges for our math problems
number_1 = "0"
number_2 = "9"


# ---- 2. DETERMINE THE NUMBER RANGES BASED ON LEVEL ----
def compare(num_1, num_2, evel):
    # Level 1: Numbers range from 0 to 9 (1-digit numbers)
    if evel == 1:
        numb_1 = int(num_1)
    # Level 2: Numbers range from 10 to 99 (2-digit numbers)
    elif evel == 2:
        numb_1 = int("1" + num_1)
    # Level 3: Numbers range from 100 to 999 (3-digit numbers)
    else:
        numb_1 = int("1" + num_1 * 2)

    numb_2 = int(num_2 * evel)
    return numb_1, numb_2


# Run the range configuration function
zombie_1, zombie_2 = compare(number_1, number_2, real_level)


# ---- 3. GENERATE THE MATH QUESTIONS ----
def adjustment(n_1, n_2, q_list):
    # Generate exactly 10 random addition problems
    for t in range(10):
        x = str(random.randint(n_1, n_2))
        y = str(random.randint(n_1, n_2))
        # Store the equation as a nicely spaced string text format
        q_list.append(x + " " + "+" + " " + y + " " + "=" + " ")


# Generate the 10 questions using the calculated number boundaries
adjustment(zombie_1, zombie_2, question_list)

score = 0

# ---- 4. MAIN GAMEPLAY LOOP ----
while len(question_list) > 0:
    # Take the first question out of the list
    corn = question_list.pop(0)
    gun = input(corn)  # Display the math question and get user's answer

    # Inner helper function to manually extract numbers from the string text and solve it
    def get_answer(le):
        # Extract specific string characters by index depending on digits size
        if le == 1:
            mama_1 = int(corn[0])
            mama_2 = int(corn[4])
        elif le == 2:
            mama_1 = int(corn[0] + corn[1])
            mama_2 = int(corn[5] + corn[6])
        else:
            mama_1 = int(corn[0] + corn[1] + corn[2])
            mama_2 = int(corn[6] + corn[7] + corn[8])

        result = mama_1 + mama_2
        return result

    # ---- 5. CHECK WRONG ANSWERS AND RETRY MECHANISM ----
    if int(gun) != get_answer(real_level):
        print("EEE")  # Display error message for a wrong answer
        count = 1
        
        while True:
            gun = input(corn)  # Give them another try
            
            # If they fix it, exit the retry loop
            if int(gun) == get_answer(real_level):
                break
            else:
                print("EEE")
                count = count + 1
                
                # If they guess incorrectly 3 times total, show the answer and move on
                if count == 3:
                    print(corn + str(get_answer(real_level)))
                    break
    else:
        # If they got it right on the very first try, reward them 1 point
        score += 1

# ---- 6. FINAL GAME SCORE ----
print(f"Score: {score}")

