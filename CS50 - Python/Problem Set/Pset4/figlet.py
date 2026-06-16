import sys
import random
import pyfiglet

fronts = pyfiglet.FigletFont.getFonts()
correct_list = ["-f", "--font"]
correct_lenght = [1, 3]

if len(sys.argv) == 1:
    user_input = input("Input: ")
    print(pyfiglet.figlet_format(user_input, font = random.choice(fronts)))

elif len(sys.argv) == 2:
    sys.exit("Invalid usage")

elif len(sys.argv) == 3:
    if sys.argv[1] not in correct_list:
        sys.exit("Invalid usage")

    elif sys.argv[2] not in fronts:
        sys.exit("Invaid usage")
    
    else:
        user_input = input("Input ")
        print(pyfiglet.figlet_format(user_input, font=sys.argv[2]))
        

elif len(sys.argv) not in correct_lenght:
    sys.exit("Invalid usage")




    

    









