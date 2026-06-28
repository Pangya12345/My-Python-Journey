import sys  # Bring in the system tools to read extra info given to the script

try:
    # If the user typed too few words in the terminal, stop and show a message
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    
    # If the user typed too many words in the terminal, stop and show a message
    elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")


    # If the number of words is just right, do this:
    else:
        file_name = sys.argv[1] # Save the file name the user typed
        
        # Look at the end of the file name. If it does not end with "py", stop
        if file_name[-2:] != "py": 
            sys.exit("Not a Python file")
            
        # If the file name is good, open it
        else:
            with open(file_name, "r") as dom: # Open the file so we can read it
                count = 0 # Start our code line counter at 0
                
                # Look at the file line by line, from top to bottom
                for i in dom: 
                    freak = i.rstrip() # Cut off any extra spacing at the very end of the line
                    new = freak.replace(" ", "") # Take away all spaces inside the line
                    
                    if new == "": # If there is absolutely nothing left on the line, skip it
                        pass 
                    elif new[0] == "#": # If the line starts with a "#" symbol, it is a comment, so skip it
                        pass
                    else:
                        count = count + 1 # If the line has real code, add 1 to our count
                        
                print(count) # Show the final number of code lines on the screen

                    

except FileNotFoundError: # If the computer cannot find the file name you typed
    print("File does not exist") # Show a message saying the file is missing