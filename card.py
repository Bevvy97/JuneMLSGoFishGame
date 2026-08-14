class Card:

    SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    SUIT_SYMBOLS = {'Spades': '♠', 'Hearts': '♥', 'Diamonds': '♦', 'Clubs': '♣'}

    def __init__(self, suit, rank):
        if suit not in Card.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        if rank not in Card.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        self.suit = suit
        self.rank = rank

    def __str__(self):
        symbol = Card.SUIT_SYMBOLS[self.suit]
        return f"{self.rank}{symbol}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return isinstance(other, Card) and self.suit == other.suit and self.rank == other.rank