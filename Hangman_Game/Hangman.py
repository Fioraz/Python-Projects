import random
import hangman_art
from wordList import words

print(hangman_art.logo)
random_word = random.choice(words)
str_length = len(random_word)
word = []

for i in range(0,str_length):
    word.append("_")
    
str_word1  = " ".join(word)
print(str_word1)


lives = 6
space_count = str_length

while lives >= 0 and space_count > 0:
    correct_answer = False
    input_letter = input("Enter a letter:\n")
    for x in range(0,str_length):
        if input_letter == random_word[x]:
            word[x] = input_letter
            space_count -= 1
            correct_answer = True
            if space_count >= 1:
                continue
            else:
                print("You won")
                break
    str_word2 = " ".join(word)
    print(str_word2)

    if not correct_answer and lives >= 0: 
        lives -= 1
        print(f"Lives left: {lives}")
        if lives == 5:
            print(hangman_art.stages[5])
          #       '''
          #   +----+
          #   |    |
          #   |    0
          #   |    
          # -----    
          #   ''')
        elif lives == 4:
            print(hangman_art.stages[4])
          #       '''
          #   +----+
          #   |    |
          #   |    0
          #   |    | 
          # -----   
          #   ''')
        elif lives == 3:
            print(hangman_art.stages[3])
          #       '''
          #   +----+
          #   |    |
          #   |    0
          #   |   /| 
          # -----    
          #   ''')
        elif lives == 2:
            print(hangman_art.stages[2])
          #       '''
          #   +----+
          #   |    |
          #   |    0
          #   |   /|\ 
          # -----    
          #   ''')
        elif lives == 1:
            print(hangman_art.stages[1])
          #       '''
          #   +----+
          #   |    |
          #   |    0
          #   |   /|\ 
          # ----- /  
          #   ''')
        else:
            print(hangman_art.stages[0])
          #       '''
          #   +----+
          #   |    |
          #   |    0
          #   |   /|\ 
          # ----- / \ 
          #   ''')
            print("You lost!")
            break
    







