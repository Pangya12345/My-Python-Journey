import sys
import csv
from tabulate import tabulate

try:

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    else:
        compare = sys.argv[1]
        if compare[-3:] != "csv":
            sys.exit("Not a CSV file")
        else:

            regular_grid = []
            with open(compare, "r") as file:
                response = csv.DictReader(file)

                for t in response:
                    regular_grid.append(t)
            print(tabulate(regular_grid, headers="keys", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
