from art import logo
print(logo)
print("Welcome to the calculator game!")

# Define the addition function to use in the loop
def add(num1, num2):
    return num1 + num2
# Define the subtraction function to use in the loop
def subtract(num1, num2):
    return num1 - num2
# Define the multiplication function to use in the loop
def multiply(num1, num2):
    return num1 * num2
# Define the division function to use in the loop
def divide(num1, num2):
    return num1 / num2

sign_list = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator_for_fun():
    from art import logo
    print(logo)
    print("Welcome to the calculator game!")
    stop = False
    while not stop:
        n1 = float(input("What's the first numbers?: "))
        n2_loop = True
        while n2_loop:
            for operation in sign_list:
                print(operation)
            sign = input("Pick an operation: ")
            if sign not in sign_list:
                print("You put the invalid operation")
            n2 = float(input("What's second numbers: "))
            print(f"{n1} {sign} {n2} = {sign_list[sign](n1, n2)}")
            continue_or_not = input(f"Type 'y to continue calculating with {sign_list[sign](n1, n2)}, or type 'n' to start a new calculation: ").lower()
            if continue_or_not == "n":
                n2_loop = False
            elif continue_or_not == "y":
                n1 = sign_list[sign](n1, n2)
                stop = True
print("The game is finish!")
calculator_for_fun()
