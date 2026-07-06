# Import all necessary modules
import sys
import csv
from tabulate import tabulate

try:

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")  # Exit if no file name argument is provided

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")  # Exit if more than one file argument is provided

    else:
        compare = sys.argv[1]
        if compare[-3:] != "csv": # Exit the program if the file is not a CSV file
            sys.exit("Not a CSV file")
        else:

            regular_grid = [] # Initialize an empty list to store row dictionaries
            with open(compare, "r") as file: # Open the target file in read-only mode
                response = csv.DictReader(file) # Read the CSV file as a sequence of dictionaries

                for t in response:
                    regular_grid.append(t) # Append each row dictionary to the list
            print(tabulate(regular_grid, headers="keys", tablefmt="grid")) # Format and print the data as a grid table
except FileNotFoundError:
    sys.exit("File does not exist") # Exit with an error message if the file is not found

