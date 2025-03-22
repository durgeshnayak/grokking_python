import art

print(art.logo)

exit_program = False
bids = {}

while not exit_program:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid

    more_bids = input("Are there any more bidders?: please enter 'yes' or 'no': ")
    if more_bids == "no":
        exit_program = True

winner = ""
winning_bid = 0
for bidder in bids:
    if bids[bidder] > winning_bid:
        winner = bidder
        winning_bid = bids[bidder]

print(f"The winner is {winner} with a bid of ${winning_bid}")
