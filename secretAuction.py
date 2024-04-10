from replit import clear

from gavel_art import logo

print(logo)

user_name = input("What is your name? ")
print(f"Welcome to the secret auction program {user_name}")

bid = input(f"What is your bid {user_name}? $")
bids = {}
bids[user_name] = bid

more_bids = input("Are there any other bidders? Type 'yes' or 'no' ")

clear()

while more_bids == "yes":
    user_name = input("What is your name? ")
    bid = input(f"What is your bid {user_name}? $")
    bids[user_name] = bid
    more_bids = input("Are there any other bidders? Type 'yes' or 'no' ")
    if more_bids == "yes":
        clear()

clear()
highest_bid = 0
winner = ""
for key in bids:
    if int(bids[key]) > highest_bid:
        highest_bid = int(bids[key])
        winner = key

print(f"The winner is {winner} with a bid of ${highest_bid}")




