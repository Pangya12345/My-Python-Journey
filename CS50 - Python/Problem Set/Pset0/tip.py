meal_cost = float(input("How much was the meal? ").replace("$", "")) # -----> receive meal cost from the user (replace "$" with "")
percentage = float(input("What percentage would you like to tip? ").replace("%", "")) # --------> percentage of tip (replace "%" with "")

def calculate_tip_amount(cost, tip_percentage):
    tip_amount = cost * (tip_percentage / 100)
    print(f"Leave ${tip_amount:.2f}")
calculate_tip_amount(meal_cost, percentage) # -------> set up the function to calculate and print tip amount