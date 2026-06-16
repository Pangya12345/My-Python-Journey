# List of month names used to map text inputs to their corresponding numeric values
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    # Get user input and strip any accidental leading/trailing whitespace
    user_input = input("Date: ").strip()
    try:
        # Check if the input is in numeric format (e.g., "9/8/1636")
        if "/" in user_input:
            month, day, year = user_input.split("/")
            # Convert strings to integers for validation and formatting
            m, d, y = int(month), int(day), int(year)

            # Validate that month and day fall within realistic calendar ranges
            if 1 <= m <= 12 and 1 <= d <= 31:
                # Print in YYYY-MM-DD format with zero-padding for single digits
                print(f"{y}-{m:02}-{d:02}")
                break

        # Check if the input is in text format (e.g., "September 8, 1636")
        elif "," in user_input:
            # Split the string at the comma to separate the year from the month and day
            month_day, year = user_input.split(",")
            # Split the month name and day number by whitespace
            month_name, day = month_day.split()

            # Verify that the extracted month name exists in our months list
            if month_name in months:
                # Find the 1-based index of the month (index + 1)
                m = months.index(month_name) + 1
                d, y = int(day), int(year.strip())

                # Validate that the day falls within a realistic calendar range
                if 1 <= d <= 31:
                    # Print in YYYY-MM-DD format with zero-padding for single digits
                    print(f"{y}-{m:02}-{d:02}")
                    break
                    
    except (ValueError, KeyError, IndexError):
        # If any parsing, conversion, or lookup errors occur, ignore them and prompt again
        pass