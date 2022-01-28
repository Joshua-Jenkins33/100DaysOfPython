from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

continueApp = True

bid_information = []

while continueApp:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bid_information.append({
        "name": name,
        "bid": bid,
    })

    other_bidders = input("Are there other users who want to bid? (Yes or No) ")

    if other_bidders.lower() == 'no':
        continueApp = False
    else:
        clear()

highest = {"name": "noone", "bid": 0}
for bid in bid_information:
    if bid["bid"] > highest["bid"]:
        highest = bid
print(
    f'The highest bidder is {highest["name"]}, with a bid of ${highest["bid"]}!'
)