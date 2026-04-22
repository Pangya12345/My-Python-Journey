print("Welcome to the tip calculator! ")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage you would like to tip? 10, 12 ,15 "))
calculate_tip = tip / 100
total_amount_of_tip = bill * calculate_tip
total_amount_of_bill = bill + total_amount_of_tip
people = int(input("How many people split the bill? "))
final_share = total_amount_of_bill / people
final_amount = round(final_share, 2)
print(f"Everybody should pay {final_amount} dollars")

print("Welcome to the tip calculator! ")
def main():
    bill = float(input("What was the total bills?" ))
    tip = int(input("What percentage you ewould like to tip? 10, 12, 15 "))
    people = int(input("How many people split the bill? "))
    final_share = calculate_amount(tip, bill)
    print(f"Everybody should pay {final_share}")

def calculate_amount(tip, bill,):
    tip_percentage = tip / 100
    total_amount_of_tip = bill * tip_percentage
    total_amount = total_amount_of_tip + bill
    final_share =  total_amount / people
    final_final_share = round(final_share, 2)
    return final_final_share

main()

