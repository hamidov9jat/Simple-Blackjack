import os
import random

deck = {'A1': 11, 'A2': 1,
        '1': 1, '2': 2,
        '3': 3, '4': 4,
        '5': 5, '6': 6,
        '7': 7, '8': 8,
        '9': 9, 'J': 10,
        'Q': 10, 'K': 10
        }


def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def deal_card():
    """Returns a random card from the deck"""
    card = random.choice(deck)
    return card


def calculate_score(cards: list):
    """Take a list of cards and return the score from the cards"""
    scores = list(map(deck.get, cards))
    # print(list(score))

    if sum(scores) == 21 and len(cards) == 2:
        return 0

    if 11 in scores and sum(scores) > 21:
        cards.remove('A1')
        cards.append('A2')
        scores.remove(deck.get('A1'))
        scores.append(deck.get('A2'))

    return sum(scores)


def compare(user_score, computer_score):

    # Both computer and the user scores are over 21
    if user_score > 21 and computer_score > 21:
        return 'You went lose (Busting). You lose 😤'

    if user_score == computer_score:
        return "It's a draw 🙃."
    elif computer_score == 0:
        return "Lose, computer has Blackjack 😱"
    elif user_score == 0:
        return "Congrats! You got Blackjack! 😎"

    # Computer has less than 21 but you not
    elif user_score > 21:
        return "Busting. You lose 😭."
    # You have less than 21 but computer not
    elif computer_score > 21:
        return "Computer lose. "
    # Both of you have scores less than 21 but yours is higher
    elif user_score > computer_score:
        return "You win 😃."
    # Both of you have scores less than 21 but yours is less
    else:
        return "You lose 😤."


if __name__ == '__main__':
    print(calculate_score(['A1', 'J', '3']))
