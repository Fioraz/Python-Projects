import os

def clear():
    os.system("cls")

bidders = True
highest_bid = 0
uname = ""
dictionary_bids = {}

while bidders:
    for x in bidders:
        name[x] = input("What is your name?: ")
        bid = int(input("What's your bid?: "))
        bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
        dictionary_bids = {name[x]:bid}
        if highest_bid < dictionary_bids[name[x]] :
            highest_bid = dictionary_bids[name[x]]
    
    if bidders == "yes":
        bidders = True
        clear()
        continue
    else:
        clear()
        
for key in dictionary_bids:
    print(f"{key} has the highest bid of ${dictionary_bids[name[x]]}")
    bidders = False   
