from Higher_Lower_game_art import logo, vs
from game_data import data
import random
import os

# Clear the terminal
def clear():
    os.system("cls")
 

# Select random dictionaries
def selection():
    return random.choice(data)


# Compare the dictionaries whether they have the same random choice
def compare(dict, is_same):
    while is_same:
        if dict['d1'] != dict['d2']:
            is_same = False
        else:
            dict['d2'] = selection()
    return dict


# Game continue until user's answer is wrong
def play_game():
    d1 = selection()         # Select a random value from the dictionary to d1
    d2 = selection()         # Select a random value from the dictionary to d2
    dict = {                 # Assign d1 and d2 dictionaries to the dict dictionary
            "d1" : d1,
            "d2" : d2
        }
    is_same = True
    score = 0
    end_game = False
    print(logo)                         # Print Game logo
    while not end_game:
        compare(dict, is_same)          # Compare the selected d1 and d2 values to check whether they are not identical
        print(f"Compare A: {dict['d1']['name']} a {dict['d1']['description']}, from {dict['d1']['country']}.")
        print(vs)
        print(f"Against B: {dict['d2']['name']} a {dict['d2']['description']}, from {dict['d2']['country']}.")
        user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
        clear() 
        if ((dict['d1']['follower_count'] > dict['d2']['follower_count']) and user_input == 'A') or ((dict['d1']['follower_count'] < dict['d2']['follower_count']) and user_input == 'B'):
            score += 1
            print(f"You're right! Current score: {score}.")
            dict['d1'] = dict['d2']
            compare(dict, is_same)      # As d1 and d2 are identical, use this function to select a non identical value to d2
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            end_game = True
        

play_game()   