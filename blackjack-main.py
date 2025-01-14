from art import logo
import random

def deal_card():
    # returns a random card from the deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def check_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_scores(p_score, c_score):
    if p_score == c_score:
        return "Draw."
    elif c_score == 0:
        return "Computer got blackjack. You lose."
    elif p_score == 0:
        return "You got blackjack. You win!"
    elif p_score > 21:
        return "You went over 21. You lose."
    elif c_score > 21:
        return "Computer went over 21. You win!"
    elif p_score > c_score:
        return "You win!"
    else:
        return "You lose."

def play_game():
    print(logo)
    player_cards = []
    computer_cards = []
    p_current_score = -1
    c_current_score = -1
    game_over = False

    for i in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        p_current_score = check_score(player_cards)
        c_current_score = check_score(computer_cards)
        print(f"   Your cards: {player_cards}, current score: {p_current_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if p_current_score == 0 or c_current_score == 0 or p_current_score > 21:
            game_over = True
        else:
            another = input("Type 'y' to get another card, type 'n' to pass: ")
            if another == 'y':
                player_cards.append(deal_card())
            else:
                game_over = True

    while c_current_score != 0 and c_current_score < 17:
        computer_cards.append(deal_card())
        c_current_score = check_score(computer_cards)

    print(f"   Your final hand: {player_cards}, final score: {p_current_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {c_current_score}")
    print(compare_scores(p_current_score, c_current_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n' ") == "y":
    print("\n" * 20)
    play_game()
