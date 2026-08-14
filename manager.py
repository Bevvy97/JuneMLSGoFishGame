from deck import Deck
from players import CmpPlayer, HmnPlayer

HAND_SIZE = 7
TOTAL_BOOKS = 13  # one book per rank, 2/3/4/.../A


class Manager:
    
    def __init__(self):
        self.deck = Deck()
        self.human = HmnPlayer("You")
        self.computer = CmpPlayer("Computer")
        self.players = [self.human, self.computer]
        self.turn_index = 0

    def initialize_game(self):
        self.deck.reset()
        for player in self.players:
            player.hand = []
            player.books = []
        for player in self.players:
            for _ in range(HAND_SIZE):
                player.add_card(self.deck.draw())
        self.turn_index = 0

    def current_player(self):
        return self.players[self.turn_index]

    def other_player(self, player):
        return self.computer if player is self.human else self.human

    def display_books(self):
        for player in self.players:
            print(f"{player.name}'s books: {player.show_books()} ({player.score()})")

    def announce_books(self, player, completed_ranks):
        for rank in completed_ranks:
            print(f"*** {player.name} completed the book of {rank}s! ***")

    def take_turn(self, player):
        opponent = self.other_player(player)
        keep_going = True

        while keep_going:
            keep_going = False  # this turn ends unless something below re-earns it

            if player.is_hand_empty():
                self.refill_hand(player)
                if player.is_hand_empty():
                    return  # no cards anywhere left for this player

            rank = player.choose_rank_to_ask()
            print(f"\n{player.name} asks {opponent.name} for {rank}s...")

            if opponent.has_rank(rank):
                won_cards = opponent.remove_rank(rank)
                player.add_cards(won_cards)
                print(f"{opponent.name} had {len(won_cards)}! {player.name} goes again.")
                self.announce_books(player, player.check_for_books())
                self.announce_books(opponent, opponent.check_for_books())
                self.refill_hand(opponent)
                if not self.is_game_over():
                    keep_going = True  # go again
            else:
                print(f"{opponent.name} says: Go Fish!")
                drawn = self.deck.draw()
                if drawn is not None:
                    player.add_card(drawn)
                    print(f"{player.name} draws from the pond.")
                    self.announce_books(player, player.check_for_books())
                    if drawn.rank == rank:
                        print(f"{player.name} drew a {rank}! Goes again.")
                        if not self.is_game_over():
                            keep_going = True  # go again
                        continue
                else:
                    print("The pond is empty.")
                self.refill_hand(player)

    def refill_hand(self, player):
        if player.is_hand_empty() and not self.deck.is_empty():
            card = self.deck.draw()
            if card is not None:
                player.add_card(card)
                print(f"{player.name}'s hand was empty and drew a new card.")

    def is_game_over(self):
        total_books = self.human.score() + self.computer.score()
        if total_books >= TOTAL_BOOKS:
            return True
        if self.deck.is_empty() and self.human.is_hand_empty() and self.computer.is_hand_empty():
            return True
        return False

    def determine_winner(self):
        print("\n" + "=" * 40)
        print("GAME OVER")
        self.display_books()
        if self.human.score() > self.computer.score():
            result = "You win!"
        elif self.human.score() < self.computer.score():
            result = "Computer wins!"
        else:
            result = "It's a tie!"
        print(result)
        return result

    def play_round(self):
        self.initialize_game()
        while not self.is_game_over():
            player = self.current_player()
            self.take_turn(player)
            self.turn_index = (self.turn_index + 1) % len(self.players)
        self.determine_winner()

    def start(self):
        print("Welcome to Go Fish!")
        playing = True
        while playing:
            self.play_round()
            playing = self.ask_play_again()

    def ask_play_again(self):
        while True:
            choice = input("\nPlay again? (y/n): ").strip().lower()
            if choice in ('y', 'yes'):
                return True
            if choice in ('n', 'no'):
                print("Thanks for playing!")
                return False
            print("Please enter 'y' or 'n'.")