# Number guessing game
import random
import ngg_art

easy_level = 10
hard_level = 5
# computer_number = random.randint(1, 100)

def play_game():
    turns = 0
    if level == 'easy':
        turns = easy_level
        print(f"You have {easy_level} attempts to guess the number.")
    else:
        turns = hard_level
        print(f"You have {hard_level} attempts to guess the number.")

    while turns > 0:
        guess = int(input("Make a guess: "))
        if guess == computer_number:
            print("You got it!")
            return "You win! Congratulations."
        elif guess > computer_number:
            turns -= 1
            print("Too high.")
            print(f"You have {turns} attempts remaining.")
        else:
            turns -= 1
            print("Too low.")
            print(f"You have {turns} attempts remaining.")

        if turns == 0:
            print(f"You've run out of guesses. You lose. The number was {computer_number}.")    
    return   

play_again = 'y'
while play_again == 'y':
    computer_number = random.randint(1, 100)
    print(ngg_art.logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    play_game()

    play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    
     




