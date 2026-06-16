import sys
import random
import pyfiglet

fronts = pyfiglet.FigletFont.getFonts()
user_input = input("Input: ")


print(sys.argv)
print(len(sys.argv))

if len(sys.argv) == 1:
    print(pyfiglet.figlet_format(user_input, font = random.choice(fronts)))

elif len(sys.argv) == 2:
    sys.exit("Invalid usage")

elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" or sys.argv[1] != "--font":
        sys.exit("Invalid usage")

    elif sys.argv[2] not in fronts:
        sys.exit("Invalid usage")
    
    else:
        print(pyfiglet.figlet_format(user_input, font=sys.argv[2]))
    









