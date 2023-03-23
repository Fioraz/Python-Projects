import os

def clear():
    os.system("cls")

bidders = True

while bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")

    highest_bid = 0

    if highest_bid < bid :
        highest_bid = bid
    else:
        if bidders == "yes":
            bidders = True
            clear()
        else:
            bidders = False
            print(f"highest bid is: {highest_bid}")   
