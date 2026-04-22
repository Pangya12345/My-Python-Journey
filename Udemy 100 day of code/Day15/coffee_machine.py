
.# 3 coffee flavor and cost for each (Espresso, latte, cappuccino)
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
# Resource in the coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# Define the function that perform the convertion of 'cent' to 'dollar'
def convert_coin():
    penny = 1 / 100
    dime = 10 / 100
    nickel  = 5 / 100
    quarter = 25 / 100
    return penny, dime, nickel, quarter
pennies, dimes, nickels, quarters = convert_coin()
# Define the function that allow machine to make a transaction
def coin_input_and_change():
    print("Please Insert coin:")
    quarter_input = int(input("How many quarter? "))
    total_quarter = quarters * quarter_input
    dime_input = int(input("How many dime? "))
    total_dime = dimes * dime_input
    nickel_input = int(input("How many nickel? "))
    total_nickel = nickels * nickel_input
    penny_input = int(input("How many penny? "))
    total_penny = pennies * penny_input
    total_coin_input = total_quarter + total_dime + total_nickel + total_penny

    if total_coin_input < MENU[game_decision]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    elif total_coin_input >= MENU[game_decision]["cost"]:
        change = total_coin_input - MENU[game_decision]["cost"]
        real_change = round(change, 2)
        print(f"Here is your {game_decision} enjoy!")
        print(f"change: {real_change}")
        resources["money"] = MENU[game_decision]["cost"]
# Define the function to make the report statement
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources["money"]}")

# Define the loop of the machine
while True:
    game_decision = input("What Would you like? (espresso/latte/cappuccino): ").lower()
# If the user pick 'report' the report statement will be display
    if game_decision == "report":
       print_report()
# If the user pick 'espresso':
    elif game_decision == "espresso":
        if MENU[game_decision]["ingredients"]["water"] > resources["water"] or resources["water"] <= 0:
            print("Sorry there is not enough water.")
            continue
        elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"] or resources["coffee"] <= 0:
            print("Sorry there is not enough coffee.")
            continue
        water_left = resources["water"] - MENU[game_decision]["ingredients"]["water"]
        resources["water"] = water_left
        coffee_left = resources["coffee"] - MENU[game_decision]["ingredients"]["coffee"]
        resources["coffee"] = coffee_left
        coin_input_and_change()
# If the user picked 'latte' or 'cappuccino';
    elif game_decision == "latte" or game_decision == "cappuccino":
        if MENU[game_decision]["ingredients"]["water"] > resources["water"] or resources["water"] <= 0:
            print("Sorry there is not enough water.")
            continue
        elif MENU[game_decision]["ingredients"]["coffee"] > resources["coffee"] or resources["coffee"] <= 0:
            print("Sorry there is not enough coffee.")
            continue
        elif MENU[game_decision]["ingredients"]["milk"] > resources["milk"] or resources["milk"] <= 0:
            print("Sorry there is not enough milk.")
            continue
        water_left = resources["water"] - MENU[game_decision]["ingredients"]["water"]
        resources["water"] = water_left
        milk_lef = resources["milk"] - MENU[game_decision]["ingredients"]["milk"]
        resources["milk"] = milk_lef
        coffee_left = resources["coffee"] - MENU[game_decision]["ingredients"]["coffee"]
        resources["coffee"] = coffee_left
        coin_input_and_change()
# If the user pick 'off', the machine will stop working
    elif game_decision == "off":
        break
    else:
        print("You put the invalid command")
print("Thank you! hope you enjoy  our service.")

print("Thank you, Hope y






