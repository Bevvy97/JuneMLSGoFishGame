import random


class CmpPlayer:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.books = []  # list of ranks this player has completed

    def add_card(self, card):
        if card is not None:
            self.hand.append(card)

    def add_cards(self, cards):
        self.hand.extend(cards)

    def has_rank(self, rank):
        return any(card.rank == rank for card in self.hand)

    def remove_rank(self, rank):
        matches = [card for card in self.hand if card.rank == rank]
        self.hand = [card for card in self.hand if card.rank != rank]
        return matches

    def check_for_books(self):
        counts = {}
        for card in self.hand:
            if card.rank in counts:
                counts[card.rank] += 1
            else:
                counts[card.rank] = 1

        completed = []
        for rank in counts:
            if counts[rank] >= 4:
                completed.append(rank)

        for rank in completed:
            self.remove_rank(rank)
            self.books.append(rank)

        return completed

    def score(self):
        return len(self.books)

    def known_ranks(self):
        from card import Card

        unique_ranks = []
        for card in self.hand:
            if card.rank not in unique_ranks:
                unique_ranks.append(card.rank)


        sorted_ranks = []
        for rank in Card.RANKS:
            if rank in unique_ranks:
                sorted_ranks.append(rank)
        return sorted_ranks

    def choose_rank_to_ask(self):
        return random.choice(self.known_ranks())

    def show_hand(self):
        return ", ".join(str(card) for card in self.hand) if self.hand else "(empty)"

    def show_books(self):
        return ", ".join(self.books) if self.books else "(none)"

    def is_hand_empty(self):
        return len(self.hand) == 0

    def __str__(self):
        return f"{self.name} - books: {self.show_books()} | hand: {self.show_hand()}"


class HmnPlayer(CmpPlayer):

    def choose_rank_to_ask(self):
        options = self.known_ranks()
        print(f"Your hand: {self.show_hand()}")
        while True:
            choice = input(f"Which rank do you want to ask for? {options}: ").strip().upper()
            if choice in options:
                return choice
            print("You can only ask for a rank you already hold. Try again.")