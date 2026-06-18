name_list = [] # -----> Set up the name list
# Try ----> Input -----> While 
try:
    while True:
        secret_text = input("Name: ") # -----> Ask user for the name
        name_list.append(secret_text) # ------> Put name in name list
# Error -------> Except
except EOFError:
    print("") # -----> EOFError ----> Print Nothing


# If length name_list == 1 ------> print output with 1 name
if len(name_list) == 1:
    print(f"Adieu, adieu, to {name_list[0]}")

# If length name_list == 2 ------> print output with 2 name
elif len(name_list) == 2:
    print(f"Adieu, adieu, to {name_list[0]} and {name_list[1]}")

# If length name_list is not equal to 1 and 2
else:
    last_name = name_list.pop() # -----> Pop out the last name of the list ---> Store in variable
    per_list = "" # -----> Set up blank string
    for k in name_list: 
        per_list += k # -----> Add name
        per_list += "," # -----> Add comma ----> ","
        per_list += " " # ------> Add space ---> " "
    print(f"Adieu, adieu, to {per_list}and {last_name}") # ----> Print output with the amount of name



    
    
    

    
        
