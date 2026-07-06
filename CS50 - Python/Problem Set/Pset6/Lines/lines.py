import sys  # Import the sys module to handle command-line arguments

try:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")  # Exit if no file argument is provided

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")  # Exit if too many arguments are provided

    else:
        file_name = sys.argv[1]  # Get the target file name from arguments
        if file_name[-3:] != ".py":  # Check if the file extension is '.py'
            sys.exit("Not a Python file")  # Exit if it is not a Python file
        else:
            with open(file_name, "r") as dom:  # Open the file in read-only mode
                count = 0  # Initialize the line counter
                for i in dom:  # Iterate through each line in the file
                    freak = i.rstrip()  # Remove trailing whitespaces and newlines (\n)
                    new = freak.replace(" ", "")  # Remove all internal spaces to assist checking
                    if new == "":  # Skip blank lines
                        pass 
                    elif new[0] == "#":  # Skip comment lines
                        pass
                    else:
                        count = count + 1  # Increment count for valid lines of code
                print(count)  # Output the final line count

except FileNotFoundError:
    sys.exit("File does not exist")  # Exit with an error message if the file is missing