print("Welcome to Calculator Game!")
operation = ["+","-","*","/"]
def calculator_for_fun():
    from art import logo
    print(logo)
    stop = False
    while not stop:
        num1 = float(input("What's the first number?: "))
        n2_loop = True
        while n2_loop:
            for sign in operation:
                print(sign)
            decision = input("Pick the operation: ")

            num2 = float(input("What's the second numbers: "))
            if decision == "+":
                output = num1 + num2
                print(f"{num1} + {num2} = {output}")
            elif decision == "-":
                output = num1 - num2
                print(f"{num1} - {num2} = {output}")
            elif decision == "*":
                output = num1 * num2
                print(f"{num1} * {num2} = {output}")
            elif decision == "/":
                output = num1 / num2
                print(f"{num1} / {num2} = {output}")
            continue_or_not = input(f"Type 'y' to continue calculating with {output}, or 'n' to start a new calculation: ").lower()
            if continue_or_not == "y":
                stop = True
                num1 = output
            elif continue_or_not == "n":
                n2_loop = False
calculator_for_fun()
