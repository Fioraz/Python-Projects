import random

card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards_list = {}
computer_cards_list = {}


# current_score = 0


# def card_selection_for_user():
#     user_cards_list = {"cards":[random.choice(card_list), random.choice(card_list)]}
#     return user_cards_list

# def card_selection_for_computer():
#     computer_cards_list = {"cards":[random.choice(card_list), random.choice(card_list)]}
#     return computer_cards_list

def computer_score(computer_cards_list):
    # computer_cards_list = card_selection_for_computer()
    length = len(computer_cards_list)
    current_score = 0
    for x in range(0,length):
        current_score += computer_cards_list["cards"][x]
    return current_score

def user_score(user_cards_list, computer_cards_list):
    # user_cards_list = card_selection_for_user()
    # computer_cards_list = card_selection_for_computer()
    length = len(user_cards_list["cards"])
    current_score = 0
    ccard = computer_cards_list["cards"][0]
    ucard = user_cards_list["cards"]
    for x in range(0,length):
        current_score += user_cards_list["cards"][x]
    print(f"Your cards: {ucard}, current score: {current_score}")
    print(f"Computer's first card: {ccard}")
    return current_score

# def another_selection_for_user(user_cards_list):
#     user_cards_list["cards"].append(random.choice(card_list))
#     return user_cards_list

# def another_selection_for_computer(computer_cards_list):
#     # length = len(computer_cards_list["cards"])
#     computer_cards_list["cards"].append(random.choice(card_list))
#     return computer_cards_list

def decision(uscore, cscore):
    # uscore = user_score()
    # cscore = computer_score()
    if (21 > uscore > cscore) or (uscore == 21 and cscore < 21):
        print("You won")
    elif 21 > computer_score() > user_score():
        print("You lose")
    else:
        print("Draw")

def display():
    user_cards_list = {"cards":[random.choice(card_list), random.choice(card_list)]}
    computer_cards_list = {"cards":[random.choice(card_list), random.choice(card_list)]}
    uscore = user_score(user_cards_list, computer_cards_list)
    cscore = computer_score(computer_cards_list)
    while uscore < 21 or cscore < 21:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == 'y':
            user_cards_list["cards"].append(random.choice(card_list))
            print(user_cards_list)
            uscore = user_score(user_cards_list, computer_cards_list)
            if uscore >= 21:
                decision(uscore, cscore)
                print(f"Computer's cards {computer_cards_list['cards']}, computer score {cscore}")
                break
            else:
                continue
        elif another_card == "n":
            decision(uscore, cscore)
            print(f"Computer's cards {computer_cards_list['cards']}, computer score {cscore}")
            break

        elif computer_score(computer_cards_list) < 17:
            # another_selection_for_computer(computer_cards_list)
            computer_cards_list["cards"].append(random.choice(card_list))
            cscore = computer_score(computer_cards_list)
            if cscore >= 21:
                decision(uscore, cscore)
                print(f"Computer's cards {computer_cards_list['cards']}, computer score {cscore}")
                break
            else:
                decision(uscore, cscore)
                print(f"Computer's cards {computer_cards_list['cards']}, computer score {cscore}")
                break
        else:
            decision(uscore, cscore)
            print(f"Computer's cards {computer_cards_list['cards']}, computer score {cscore}")
            break

    # decision(user_score, computer_score)
    

display()
# user_score()