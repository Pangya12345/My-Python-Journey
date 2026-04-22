from art import logo
print(logo)
def biding_record(winner_bidding):
    top_bidding_price = 0
    top_bidding_name = ""
    for bidding in winner_bidding:
        if winner_bidding[bidding] > top_bidding_price:
            top_biding_price = winner_bidding[bidding]
            top_biding_name = bidding
    print(f"The winner is {top_biding_name} with a bid of ${top_biding_price}")

stop = False
bids = {}
while not stop:
    name = input("What is your name? ")
    bid_price = float(input("What is you bid? $ "))
    bids[name] = bid_price
    any_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if any_bidder == "yes":
        print("\n" * 100)
    elif any_bidder == "no":
        stop = True
        biding_record(winner_bidding = bids)

