import random
from card import Card

class Deck:
    

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        self.cards = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            return None
        return self.cards.pop()

    def cards_remaining(self):
        return len(self.cards)

    def is_empty(self):
        return len(self.cards) == 0

    def reset(self):
        self.build()
        self.shuffle()