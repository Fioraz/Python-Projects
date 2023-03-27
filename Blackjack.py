import random
import Blackjack_art

card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards_list = {}
computer_cards_list = {}

def computer_score(computer_cards_list):
    length = len(computer_cards_list["cards"])
    current_score = 0
    for x in range(0,length):
        current_score += computer_cards_list["cards"][x]
    return current_score

def user_score(user_cards_list, computer_cards_list):
    length = len(user_cards_list["cards"])
    current_score = 0
    ccard = computer_cards_list["cards"][0]
    ucard = user_cards_list["cards"]
    for x in range(0,length):
        current_score += user_cards_list["cards"][x]
    print(f"Your cards: {ucard}, current score: {current_score}")
    print(f"Computer's first card: {ccard}")
    return current_score

def decision(uscore, cscore):
    if (21 > uscore > cscore) or (uscore == 21 and cscore < 21):
        print("You win 😃")
    elif (21 > uscore and cscore > 21):
        print("Opponent went over. You win 😁")
    elif cscore == uscore:
        print("Draw 🙃")
    elif uscore > 21:
        print("You went over. You lose 😭")
    else:
        print("You lose 😤")
    

def display():
    print(Blackjack_art.logo)
    user_cards_list = {"cards":[random.choice(card_list), random.choice(card_list)]}
    computer_cards_list = {"cards":[random.choice(card_list), random.choice(card_list)]}
    uscore = user_score(user_cards_list, computer_cards_list)
    cscore = computer_score(computer_cards_list)
    if uscore == 21 or cscore == 21:
        decision(uscore, cscore)
        print(f"Computer's cards {computer_cards_list['cards']}, computer score {cscore}")
    else:
        while uscore < 21 and cscore < 21:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                if uscore > 10:
                    new_card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
                    user_cards_list["cards"].append(random.choice(new_card_list))
                else:
                    user_cards_list["cards"].append(random.choice(card_list))
                uscore = user_score(user_cards_list, computer_cards_list)
                if uscore >= 21:
                    decision(uscore, cscore)
                    print(f"Computer's cards {computer_cards_list['cards']}, computer score {cscore}")
                    uscore = uscore > 21
                    break
                else:
                    continue
            else:
                cscore = computer_score(computer_cards_list)
                if cscore < 17:
                    while cscore < 17:
                        if cscore > 10:
                            new_card_list = new_card_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
                            computer_cards_list["cards"].append(random.choice(new_card_list))
                        else:
                            computer_cards_list["cards"].append(random.choice(card_list))
                        cscore = computer_score(computer_cards_list)
                    decision(uscore, cscore)
                    print(f"Computer's cards {computer_cards_list['cards']}, computer score {cscore}")
                    break
                

display()