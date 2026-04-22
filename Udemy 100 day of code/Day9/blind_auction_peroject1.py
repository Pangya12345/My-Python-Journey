# First version without function

from art import logo
print(logo)
print("Welcome to the 'Silent Auction program'")
bids = {}
stop = False
while not stop:
    name = input("What is your name? ")
    bids_price = float(input("What is your bid? $"))
    bids[name] = bids_price
    any_bidder = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if any_bidder == "yes":
        print("\n" * 100)
    elif any_bidder == "no":
        stop = True
for i in bids:
    top_bid = 0
    top_bid_name = ""
    if bids[i] > top_bid:
        top_bid = bids[i]
        top_bid_name = i
        print(f"The winner is {top_bid_name} with a bid of ${top_bid}")



