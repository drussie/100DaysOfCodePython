import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
print("Welcome to the game of Rock, Paper, Scissors!")
user_choice = input("What do you choose, Rock, Paper, or Scissors? ").lower()
if user_choice == "rock":
  print(rock)
elif user_choice == "paper":
    print(paper)
elif user_choice == "scissors":
    print(scissors)
else:
    print("Invalid choice. You lose.")
    exit()

computer_choice = random.randint(0, 2)
print("Computer choice:")    
print(game_images[computer_choice])

if user_choice == "rock" and computer_choice == 0:
    print("It's a draw.")
elif user_choice == "rock" and computer_choice == 1:
    print("You lose.")
elif user_choice == "rock" and computer_choice == 2:    
    print("You win.")
elif user_choice == "paper" and computer_choice == 0:
    print("You win.")
elif user_choice == "paper" and computer_choice == 1:
    print("It's a draw.")
elif user_choice == "paper" and computer_choice == 2:
    print("You lose.")
elif user_choice == "scissors" and computer_choice == 0:
    print("You lose.")
elif user_choice == "scissors" and computer_choice == 1:
    print("You win.")
elif user_choice == "scissors" and computer_choice == 2:
    print("It's a draw.")
else:
    print("Invalid choice. You lose.")
    exit()
print("Thank you for playing!")
# End of RockPaperScissors.py