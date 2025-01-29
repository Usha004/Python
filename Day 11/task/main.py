from art import logo
print(logo)
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

    user_cards = []
    computer_cards = []
    user_score = user_cards.append(deal_card())
    computer_score = computer_cards.append(deal_card())


def calculate_score(cards):
     return sum(cards)
    Ace = 11
    Jack_Queen_King = 10
    Blackjack = Ace + Jack_Queen_King

    if Blackjack == True:
        return 0
    if user_score > 21:
        user_score.remove(11)
        user_score.append(1)
    elif computer_score > 21:
        computer_choice.remove(11)
        computer_score.append(1)

    print(f"your cards are: {user_cards}")
    print(f"Computer's first card: {computer_cards}")
    if user_score > 21 and Blackjack == 0:
        print("game end")
    else:
        choice = input("Type 'y' to get another card,type 'n' to pass: ")
        if choice == 'y':
            deal_card()
        else:
            print("game end")
def compare(user_score,computer_score,Blackjack):

    if user_score == Blackjack:
        print("you won!")
    elif computer_score == Blackjack:
        print("computer win!")
    elif user_score == computer_score:
        print("draw")
    else:
        print("player with highest score wins")

    calculate_score()

compare(user_score = 0,computer_score = 0,Blackjack = 0)



















