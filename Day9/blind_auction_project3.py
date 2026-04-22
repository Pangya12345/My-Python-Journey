from art import logo
print(logo)
print("Welcome to silent bids auction game!")
bids = {}
stop = False
while not stop:
    name = input("What is your name? ")
    bid_price = int(input("What is your bid price? $"))
    bids[name] = bid_price
    any_bidders = input("Are there any other bidders? type 'yes' or 'no' ").lower()
    if any_bidders == "yes":
        print("\n" * 100)
    elif any_bidders == "no":
        stop = True
top_bid = 0
top_bid_name = ""
for bidder in bids:
    if bids[bidder] > top_bid:
        top_bid = bids[bidder]
        top_bid_name = bidder
print(f"The winner is {top_bid_name} with a bid of ${top_bid}")
