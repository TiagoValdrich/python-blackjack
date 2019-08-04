import random
from .Card import Card

class Deck():

    def __init__(self, ranks, suits, values):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank, values[rank]))
        
    def __str__(self):
        for card in self.deck:
            print('We have the card {} on the deck'.format(card))
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()