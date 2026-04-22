import random
budget = 1000
day = 1
event_list = ["You are hungry", "You are thristy", "You are sick", "Power outage"]
inventory_item = {}
player_inventory = []
inventory_item_order = {}
main_inventory = {}
game_direction = {}
game_logic_maping = {}
game_logic_maping["You are hungry"] = "Food"
game_logic_maping["You are thristy"] = "Water"
game_logic_maping["You are sick"] = "Medicine"
game_logic_maping["Power outage"] = "Flashlight"
inventory_item["Food"] = 100
inventory_item["Water"] = 50
inventory_item["Medicine"] = 200
inventory_item["Flashlight"] = 150
print("=====SURVIVAL SHOP=====")
print(f"Money left: {budget}")
print("\n")
for rep in inventory_item:
    main_inventory[rep] = 0
count = 1
for item in inventory_item:
    print(f"{count}. {item} {inventory_item[item]}")
    count = count + 1
print("5. Done")
inventory_count = 1
for i in inventory_item:
    inventory_item_order[inventory_count] = i
    inventory_item_order[5] = "done"
    inventory_count += 1
stop = False
while not stop:
    def buy_item():
        buy_item = int(input("Choose item: "))
        global budget
        global player_inventory
        global inventory_item_order
        global inventory_item
        global stop
        global main_inventory
        if buy_item not in inventory_item_order:
            print("Invalid number")
            print("Try Again")
        elif buy_item == 5:
            stop = True
        else:
            player_inventory.append(inventory_item_order[buy_item])
            budget -= inventory_item[inventory_item_order[buy_item]]
            if budget <= 0:
                print("You run out of the budget!")
                stop = True
            elif budget != 0:
                main_inventory[inventory_item_order[buy_item]] += 1
                print(f"{inventory_item_order[buy_item]} added.")
                print(f"Money left: {budget}")
    buy_item()
day = 0
print("=====SURVIVAL START=====")
print("\n")
def game_logic():
    global day
    while True:
        event_random = random.choice(event_list)
        day = day + 1
        print(f"Day: {day}")
        if day < 5 and main_inventory[game_logic_maping[event_random]] > 0:
            print(f"Event: {event_random}")
            main_inventory[game_logic_maping[event_random]] -= 1
            print(f"{game_logic_maping[event_random]} used.")
            print(f"Inventory: {main_inventory}")
            print("\n")
        elif day <= 5 and main_inventory[game_logic_maping[event_random]] == 0:
            print(f"Event: {event_random}")
            print(f"no {game_logic_maping[event_random]} left...")
            print("GAME OVER")
            break
        elif day == 5 and main_inventory[game_logic_maping[event_random]] > 0:
             print(f"Event: {event_random}")
             main_inventory[game_logic_maping[event_random]] -= 1
             print(f"{game_logic_maping[event_random]} used.")
             print("\n")
             print(f"You survived 5 days!")
             print("FINAL INVENTORY:")
             print(main_inventory)
             break
game_logic()
