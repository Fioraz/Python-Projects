from resources import MENU, resources

def drinks_dict():
    drinks = {
        "espresso" : [(MENU["espresso"]["ingredients"]["water"]), (MENU["espresso"]["ingredients"]["coffee"]), 0],
        "latte" : [(MENU["latte"]["ingredients"]["water"]), (MENU["latte"]["ingredients"]["coffee"]), (MENU["latte"]["ingredients"]["milk"])],
        "cappuccino" : [(MENU["cappuccino"]["ingredients"]["water"]), (MENU["cappuccino"]["ingredients"]["coffee"]), (MENU["cappuccino"]["ingredients"]["milk"])],
        "available_resources" : [resources["water"], resources["coffee"], resources["milk"]]
    }
    return drinks

def cost_dict():
    cost = {
        "espresso" : MENU["espresso"]["cost"],
        "latte" : MENU["latte"]["cost"],
        "cappuccino" : MENU["cappuccino"]["cost"],
        "available_money" : 0
    }
    return cost

# Print report
def print_report(drinks, cost):
    available_resources = drinks["available_resources"]
    available_money = cost["available_money"]
    print(f"Water: {available_resources[0]}ml")
    print(f"Milk: {available_resources[2]}ml")
    print(f"Coffee: {available_resources[1]}g")
    print(f"Money: ${available_money}")  
    return available_resources

# Process coins.
def process_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total

def update_resources(drinks, cost, user_input, money):  
    drinks["available_resources"][0] -= drinks[user_input][0]
    drinks["available_resources"][1] -= drinks[user_input][1]
    drinks["available_resources"][2] -= drinks[user_input][2]
    cost["available_money"] += money
    return drinks, cost

# Check transaction successful?
def check_transaction(drinks, cost, money, user_input):
    total = process_coins()
    if total > money:
        change = round((total - money),2)
        print(f"Here is ${change} in change.")
        # Make Coffee.
        print(f"Here is your {user_input} ☕ Enjoy!")
        drinks, cost = update_resources(drinks, cost, user_input, money)
        return drinks, cost
    elif total == money:
        # Make Coffee.
        print(f"Here is your {user_input} ☕ Enjoy!")
        drinks, cost = update_resources(drinks, cost, user_input, money)
        return drinks, cost
    else:
        print("Sorry that's not enough money. Money refunded.")
     
# Check resources sufficient?
def check_resources(drinks, cost):
    turn_off = False
    available_resources =  drinks["available_resources"]
    espresso = drinks["espresso"]
    latte = drinks["latte"]
    cappuccino = drinks["cappuccino"]
    # proceed = False
    money = 0
    while not turn_off:
        # Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
        user_input = input("What would you like? (espresso/latte/cappuccino): ")
        if user_input == "report":
            print_report(drinks, cost)
        elif user_input == "espresso":
            if (available_resources[0] >= espresso[0]) and (available_resources[1] >= espresso[1]) :
                print("Please insert coins.")
                money = cost[user_input]
                check_transaction(drinks, cost, money, user_input)
            else:
                if available_resources[0] < espresso[0]:
                    print("Sorry there is not enough water")
                elif available_resources[2] < espresso[2]:
                    print("Sorry there is not enough coffee")
                else:
                    print("Sorry there is not enough water and coffee")
            
        elif user_input == "latte":
            if (available_resources[0] >= latte[0]) and (available_resources[1] >= latte[1]) and (available_resources[2] >= latte[2]):
                print("Please insert coins.")
                money = cost[user_input]
                check_transaction(drinks, cost, money, user_input)
            else:
                if available_resources[0] < latte[0]:
                    print("Sorry there is not enough water")
                elif available_resources[1] < latte[1]:
                    print("Sorry there is not enough coffee")
                elif available_resources[2] < latte[2]:
                    print("Sorry there is not enough milk")
                else:
                    print("Sorry there is not enough water, milk and coffee")
        elif user_input == "cappuccino":
            if (available_resources[0] >= cappuccino[0]) and (available_resources[1] >= cappuccino[1]) and (available_resources[2] >= cappuccino[2]):
                print("Please insert coins.")
                proceed = True
                money = cost[user_input]
                check_transaction(drinks, cost, money, user_input)
            else:
                if available_resources[0] < cappuccino[0]:
                    print("Sorry there is not enough water")
                elif available_resources[1] < cappuccino[1]:
                    print("Sorry there is not enough coffee")
                elif available_resources[2] < cappuccino[2]:
                    print("Sorry there is not enough milk")
                else:
                    print("Sorry there is not enough water, milk and coffee")
        else:
            turn_off = True

check_resources(drinks = drinks_dict(), cost = cost_dict())