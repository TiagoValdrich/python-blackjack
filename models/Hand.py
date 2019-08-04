class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def show_hand(self):
        for card in self.cards:
            print(card)

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        
        # Aces can be one or eleven, so if the total value
        # is greather than 21, it changes the ace to be one
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1