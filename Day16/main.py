rep = CoffeeMaker()
coin = MoneyMachine()
is_on = True
while is_on:
    user_input = input(f"What would you like? {start.get_items()} ").lower()
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        rep.report()
        print(coin.report())
        continue
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        drink_name = start.find_drink(user_input)
        if rep.is_resource_sufficient(drink_name):
            if coin.make_payment(drink_name):
                rep.make_coffee(drink_name)
