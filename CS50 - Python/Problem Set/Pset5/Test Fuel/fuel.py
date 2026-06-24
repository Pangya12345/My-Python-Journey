def convert(user_input):
    # Split or extract the X and Y values from the input string (assumes format like "X/Y")
    X, Y = int(user_input[0]), int(user_input[2])

    # Prevent division by zero
    if Y == 0:
        raise ZeroDivisionError
    
    # Ensure X is not greater than Y (fraction cannot be greater than 100%)
    if X > Y:
        raise ValueError
        
    # Ensure X is a non-negative number
    if X < 0:
        raise ValueError

    # Calculate, round, and return the percentage if validation passes
    else:
        percentage = (X / Y) * 100
        real_percentage = round(percentage)
        return real_percentage


def gauge(percentage):
    # If the tank is 1% or less, indicate that it is Empty ("E")
    if percentage <= 1:
        return "E"

    # If the tank is 99% or more, indicate that it is Full ("F")
    elif percentage >= 99:
        return "F"

    # Otherwise, return the actual percentage as a formatted string
    else:
        return f"{percentage}%"