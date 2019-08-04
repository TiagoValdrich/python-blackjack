import random

from models.Card import Card
from models.Deck import Deck
from models.Hand import Hand
from models.Chips import Chips

# Global variables
playing = True

# Defining functions
def take_bet(chips):

    while True:
        print("You have {} chips.".format(chips.total))
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Invalid input, provide a integer value")
        else:
            if chips.bet > chips.total:
                print("You don't have enough chips to bet! You have only {}".format(chips.total))
            else:
                break

def hit(deck, hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        option = input('Hit or Stand? Enter h or s ')

        if option[0].lower() == 'h':
            hit(deck, hand)
        elif option[0].lower() == 's':
            print("Player stands Dealer's turn")
            playing = False
        else:
            print("Sorry, I didn't understand that, Please enter h or s only!")
            continue

        break

def show_some(player_hand, dealer_hand):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print(dealer_hand.cards[1])
    print("")
    print("\nPlayer's Hand:")
    player_hand.show_hand()

def show_all(player_hand, dealer_hand):
    print("\nDealer's Hand:")
    dealer_hand.show_hand()
    print("")
    print("Dealer's Hand = {}".format(dealer_hand.value))
    print("\nPlayer's Hand:")
    player_hand.show_hand()
    print("Player's Hand = {}".format(player_hand.value))

def player_busts(chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(chips):
    print("BUST DEALER!")
    chips.win_bet()

def dealer_wins(chips):
    print("DEALER WINS!")
    chips.lose_bet()

def push():
    print("Dealer and player tie! PUSH")

def main():
    global playing

    # Declaring variables
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    
    while True:
        print("Welcome to BlackJack!")

        # Create the deck and cards
        deck = Deck(ranks, suits, values)
        deck.shuffle()

        # Create the player hand
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        # Create the dealer hand
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Create the player chips to bet
        player_chips = Chips()

        # Get the player bet
        take_bet(player_chips)
        # Show their hands
        show_some(player_hand, dealer_hand)

        while playing:

            # Ask to the player if he/she wants to hit or stand
            hit_or_stand(deck, player_hand)
            # Show their hands
            show_some(player_hand, dealer_hand)
            # Check if hands exceeds 21
            if player_hand.value > 21:
                player_busts(player_chips)
                break

        # If the player hasn't busted
        if player_hand.value <= 21:

            while dealer_hand.value < player_hand.value:
                hit(deck, dealer_hand)

            # Show all cards
            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_chips)
            else:
                push()

        print('\n Player total chips are at: {}'.format(player_chips.total))

        new_game = input("Would you like to play another hand? y/n ")
        
        if new_game[0] == 'y':
            playing = True
            continue
        else:
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()