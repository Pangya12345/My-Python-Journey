while True:
    try:
        # Prompt the user for a fraction input (e.g., "3/4")
        fraction = input("Fraction: ")
        
        # Split the input into numerator and denominator strings
        x_str, y_str = fraction.split("/")
        
        # Convert the string components into integers
        x = int(x_str)
        y = int(y_str)

        # Handle edge cases and invalid mathematical inputs
        if y == 0:
            raise ZeroDivisionError  # Cannot divide by zero
        if x > y:
            raise ValueError         # Numerator shouldn't be greater than denominator for this logic
        if x < 0:
            raise ValueError         # Negative fractions are not allowed here

        # Calculate the percentage and round it to the nearest whole number
        percentage = (x / y) * 100
        real_percentage = round(percentage)
        
        # Determine the output format based on the percentage value
        if real_percentage == 0 or real_percentage == 1:
            print("E")  # Print "E" for Empty (0% or 1%)
            break       # Exit the loop on valid output
        elif real_percentage == 100 or real_percentage == 90:
            print("F")  # Print "F" for Full (99% or 100%)
            break       # Exit the loop on valid output
        else:
            print(f"{real_percentage}%")  # Print the actual formatted percentage

    # If any error occurs (invalid input format, non-integers, or raised errors), reset the loop
    except ValueError:
        continue
    except ZeroDivisionError:
        continue