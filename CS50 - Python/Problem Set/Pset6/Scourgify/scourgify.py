import csv
import sys

headers = ["first", "last", "house"]
try:
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    else:
        result = []
        with open(sys.argv[1], "r") as file:
            response = csv.DictReader(file)

            for i in response:
                last_name = i["name"][0:i["name"].index(",")]
                first_name = i["name"][i["name"].index(",") + 2:]
                result.append({"first": first_name, "last": last_name, "house": i["house"]})

            print(result)


        with open(sys.argv[2], "w", newline="") as something:
            make = csv.DictWriter(something, fieldnames=headers)
            make.writeheader()
            for h in result:
                make.writerow(h)






except FileNotFoundError:
    sys.exit(f"could not read {sys.argv[1]}")
