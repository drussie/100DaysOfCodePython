# Description: A simple game of Hangman
import random
import hangman_art
import hangman_words
from replit import clear

# word_list = ["aardvark", "baboon", "camel"]
word_list = hangman_words.word_list

word = random.choice(word_list)
blank_word = []

for n in range(len(word)):
    blank_word.append("_")

print(hangman_art.logo)
print(hangman_art.stages[6])
print("Welcome to the game of Hangman!")

lives = 6
word_length = len(word)
letters_found = 0
checked_letters = []

while lives > 0 and letters_found <= word_length - 1:  
    found = False 
    count = 0
    while count <= 3:
        guess = input("Guess a letter: ").lower()  
        clear()
        if guess == "0":
            exit()
        if guess in checked_letters:
            print("You already guessed that letter.\nEnter a different letter.")
            count += 1
        else:
            checked_letters.append(guess)
            break    
        if count == 3:
            print("You entered a guessed letter too many times.\nGame over!")
            exit()    

    for n in range(word_length):
         if word[n] == guess:
              blank_word[n] = guess
              letters_found += 1
              found = True
    if not found:
        lives -= 1
        print(hangman_art.stages[lives])
        print(f"You have {lives} lives left.")  
    for n in range(len(blank_word)):
        print(blank_word[n], end="  ")
    print(f"\nletters guessed: {checked_letters}")    
    print("\n")  

if lives <= 0:
    print(f"You lose. Game over!\nThe word was {word}.")
else:
     print("You win! Congratulations")