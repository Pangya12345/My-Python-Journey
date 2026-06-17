name_list = []
try:
    while True:
        secret_text = input("Name: ")
        name_list.append(secret_text)
except EOFError:
    print("")

if len(name_list) == 1:
    print(f"Adieu, adieu, to {name_list[0]}")

elif len(name_list) == 2:
    print(f"Adieu, adieu, to {name_list[0]} and {name_list[1]}")


else:
    last_name = name_list.pop()
    per_list = ""
    for k in name_list:
        per_list += k
        per_list += ","
        per_list += " "
    print(f"Adieu, adieu, to {per_list}and {last_name}")



    
    
    

    
        
