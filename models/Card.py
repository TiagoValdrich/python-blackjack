class Card():

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
    
    def __str__(self):
        return '{rank} of {suit}'.format(rank=self.rank, suit=self.suit)