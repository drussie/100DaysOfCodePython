import random
from blackjack_art import logo  # Uncomment if logo is available
from replit import clear  # Uncomment if running on Replit

cards = {"A": 11, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "J": 10, "Q": 10, "K": 10}

def deal_card():
    return random.choice(list(cards.keys()))

def calculate_score(card_keys):
    score = sum(cards[card] for card in card_keys)
    if len(card_keys) == 2 and score == 21:
        return 0  # Blackjack
    while score > 21 and 'A' in card_keys:
        card_keys.remove('A')
        card_keys.append(1)  # Replace Ace with 1
        score = sum(cards[card] for card in card_keys)
    return score

def deal_initial_cards():
    player_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    return player_cards, computer_cards

def play_blackjack():
    clear()  # Uncomment if running on Replit
    print(logo)  # Uncomment if logo variable is available

    player_cards, computer_cards = deal_initial_cards()
    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                player_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    if player_score > 21:
        print("You went over. You lose.")
    elif computer_score > 21 or player_score > computer_score:
        print("You win!")
    elif player_score < computer_score:
        print("You lose!")
    else:
        print("It's a draw!")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_blackjack()
