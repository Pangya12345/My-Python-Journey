meal_cost = float(input("How much was the meal? ").replace("$", ""))
percentage = float(input("What percentage would you like to tip? ").replace("%", ""))

def calculate_tip_amount(cost, tip_percentage):
    tip_amount = cost * (tip_percentage / 100)
    print(f"Leave ${tip_amount:.2f}")
calculate_tip_amount(meal_cost, percentage)
