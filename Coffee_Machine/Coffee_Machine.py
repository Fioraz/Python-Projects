from resources import MENU, resources

def drinks_dict():
    drinks = {
        "espresso" : [(MENU["espresso"]["ingredients"]["water"]), (MENU["espresso"]["ingredients"]["coffee"])],
        "latte" : [(MENU["latte"]["ingredients"]["water"]), (MENU["latte"]["ingredients"]["coffee"]), (MENU["espresso"]["ingredients"]["milk"])],
        "cappuccino" : [(MENU["espresso"]["ingredients"]["water"]), (MENU["espresso"]["ingredients"]["coffee"]), (MENU["espresso"]["ingredients"]["milk"])],
        "available_resources" : [resources["water"], resources["coffee"], resources["milk"]]
    }
    return drinks

def cost_dict():
    cost = {
        "espresso" : MENU["espresso"]["cost"],
        "latte" : MENU["latte"]["cost"],
        "cappuccino" : MENU["cappuccino"]["cost"]
    }

# def select_espresso():
#     espresso = []

#     espresso.append(MENU["espresso"]["ingredients"]["water"])
#     espresso.append(0)
#     espresso.append(MENU["espresso"]["ingredients"]["coffee"])
#     espresso.append(MENU["espresso"]["cost"])
#     return espresso

# def select_latte():
#     latte = []
#     latte.append(MENU["latte"]["ingredients"]["water"])
#     latte.append(MENU["espresso"]["milk"])
#     latte.append(MENU["latte"]["ingredients"]["coffee"])
#     latte.append(MENU["espresso"]["cost"])
#     return latte
    
# def select_cappuccino():
#     cappuccino = []
#     cappuccino.append(MENU["latte"]["ingredients"]["water"])
#     cappuccino.append(MENU["espresso"]["milk"])
#     cappuccino.append(MENU["latte"]["ingredients"]["coffee"])
#     cappuccino.append(MENU["espresso"]["cost"])
#     return cappuccino

# Turn off the Coffee Machine by entering “off” to the prompt
def off():
    turn_off = True
    return turn_off

# Print report
def print_report():
    available_resources = drinks["available_resources"]
    print(f"Water: {available_resources[0]}ml")
    print(f"Milk: {available_resources[2]}ml")
    print(f"Coffee: {available_resources[1]}g")
    print(f"Money: ${available_resources[3]}")  #########<<<<<<<<<<<<<<<
    return available_resources

# Check resources sufficient?
def check_resources():
    available_resources = print_report()
    espresso = drinks["espresso"]
    latte = drinks["latte"]
    cappuccino = drinks["cappuccino"]
    proceed = False
    money = 0

    if user_input == "report":
        print_report()
    elif user_input == "espresso":
        if (available_resources[0] >= espresso[0]) and (available_resources[1] >= espresso[1]) :
            print("Please insert coins.")
            proceed = True
            money = espresso[3]
            return proceed, money, user_input
        else:
            if available_resources[0] < espresso[0]:
                print("Sorry there is not enough water")
            elif available_resources[2] < espresso[2]:
                print("Sorry there is not enough coffee")
            else:
                print("Sorry there is not enough water and coffee")
            # return proceed, money
        
    elif user_input == "latte":
        if (available_resources[0] >= espresso[0]) and (available_resources[1] >= espresso[1]) :
            print("Please insert coins.")
            proceed = True
            money = espresso[3]
            return proceed, money, user_input
    elif user_input == "cappuccino":
        print      #####<<<<<<<<<<<<<<<<<<<
    else:
        off()


# Process coins.
def process_coins():
    proceed, money, user_input = check_resources()
    change = 0
    if proceed:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    if total > money:
        change = total - money
        print(f"Here is ${change} in change.")
        print(f"Here is your {user_input} ☕ Enjoy!")
    elif total == money:
        print("Here is your coffee")
    


# Check transaction successful?

# Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while off():
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    

# Make Coffee.
