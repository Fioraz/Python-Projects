import os

def clear():
    os.system("cls")

bidders = True
highest_bid = 0
uname = ""
dictionary_bids = {}

while bidders:

    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")

    dictionary_bids[name] = bid
    
    if bidders == "yes":
        bidders = True
        clear()
        continue
    else:
        clear()
        for name in dictionary_bids:
            if highest_bid < dictionary_bids[name]:
                highest_bid = dictionary_bids[name]
                uname = name
        print(f"{uname} has the highest bid of ${highest_bid}")
        break
    
    bidders = False   
