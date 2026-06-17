# Import all modules
import sys
import random
import pyfiglet

# Set up all the necessary compliment indicators
fonts = pyfiglet.FigletFont.getFonts() # -----> Create "font name" list
correct_list = ["-f", "--font"] # ----> Create fonts compare list
correct_length = [1, 3] # ------> Create input argument compare length

# If length of input argument == 1
if len(sys.argv) == 1:
    user_input = input("Input: ")
    print(pyfiglet.figlet_format(user_input, font = random.choice(fonts))) # ----> Print user input with random font

elif len(sys.argv) == 2:
    sys.exit("Invalid usage") # Exit if the length of the input argument == 2

# If the length of the input argument == 3
elif len(sys.argv) == 3:
    if sys.argv[1] not in correct_list:
        sys.exit("Invalid usage") # ----> If sys.argv[1] not in the correct_list ------> Exit

    elif sys.argv[2] not in fonts:
        sys.exit("Invalid usage") # If sys.argv[2] not in fonts ----> Exit
    
    else:
        user_input = input("Input: ")
        print(pyfiglet.figlet_format(user_input, font=sys.argv[2])) # Print user input if the argument does not meet the error condition with the given font in sys.argv[2]
        
# If the length of the input argument is not equal to 1 and 3
elif len(sys.argv) not in correct_length:
    sys.exit("Invalid usage") # Exit the program



    

    









