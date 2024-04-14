# Higher Lower Game
import hl_art
import hl_data
import random
from replit import clear

score = 0

def play_game():
    clear()
    print(hl_art.logo)
    print("Welcome to the Higher Lower Game!")
    print("Can you guess who has more followers on Instagram?")

    score = 0
    game_over = False
    first_flag = True
    
    while not game_over:
        if first_flag == True:  
            choice_a = random.choice(hl_data.data)
            first_flag = False
        else:
            choice_a = choice_b    
        choice_b = random.choice(hl_data.data)
        print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
        print(hl_art.vs)
        print("\n")
        print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")

        choice  = input("Who has more followers? Type 'A' or 'B': ").lower()

        if choice == 'a':
                if choice == 'a' and choice_a['follower_count'] > choice_b['follower_count']:
                    score += 1
                    print(f"Your score is {score}.")
                else:
                    print(f"Sorry, that's wrong. Your final score is {score}. Thank you for playing.")
                    game_over = True

        if choice == 'b':
                if choice == 'b' and choice_b['follower_count'] > choice_a['follower_count']:
                    score += 1
                    print(f"Your score is {score}.")
                else:
                    print(f"Sorry, that's wrong. Your final score is {score}. Thank you for playing.")            
                    game_over = True
                   
play_game()        
        



