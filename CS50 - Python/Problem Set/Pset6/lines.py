import sys
try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")

    else:
        file_name = sys.argv[1]
        if file_name[-2:] != "py":
            sys.exit("Not a Python file")
        else:
            with open(file_name, "r") as dom:
                count = 0
                for i in dom:
                    if i[0] == "#":
                        pass
                    else:
                        count = count + 1
            print(count)
                    

except FileNotFoundError:
    print("File does not exist")
