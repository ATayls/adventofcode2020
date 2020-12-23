from copy import copy

with open(r"data/day22_in.txt", "r") as f:
    puzzle_input = [x.strip() for x in f.readlines()]


class Standard_Game:
    def __init__(self, p1_deck, p2_deck):
        self.round = 1
        self.p1_deck = copy(p1_deck)
        self.p2_deck = copy(p2_deck)

    def status(self):
        print(f"\n-- Round {self.round} --")
        print(f"Player 1's deck: {self.p1_deck}")
        print(f"Player 2's deck: {self.p2_deck}")
        print(f"Player 1 plays: {self.p1_deck[0]}")
        print(f"Player 2 plays: {self.p2_deck[0]}")

    def play_round(self):
        self.status()
        card_p1 = self.p1_deck[0]
        card_p2 = self.p2_deck[0]
        if card_p1 > card_p2:
            print("Player 1 wins the round!")
            self.p1_deck.append(self.p1_deck.pop(0))
            self.p1_deck.append(self.p2_deck.pop(0))
        elif card_p1 < card_p2:
            print("Player 2 wins the round!")
            self.p2_deck.append(self.p2_deck.pop(0))
            self.p2_deck.append(self.p1_deck.pop(0))
        else:
            raise ValueError("don't know what to do")
        self.round += 1

    def run_game(self):
        while self.p1_deck and self.p2_deck:
            self.play_round()

        print("\n== Post-game results ==")
        print(f"Player 1's deck: {self.p1_deck}")
        print(f"Player 2's deck: {self.p2_deck}")

        p1_score = sum(
            ind * val
            for ind, val in zip(self.p1_deck, list(range(len(self.p1_deck), 0, -1)))
        )
        p2_score = sum(
            ind * val
            for ind, val in zip(self.p2_deck, list(range(len(self.p2_deck), 0, -1)))
        )
        winning_score = max(p1_score, p2_score)
        print(f"Winning score {winning_score}")

        if winning_score == p1_score:
            print(f"Player 1 Wins!")
            return "P1", winning_score
        else:
            print(f"Player 2 Wins!")
            return "P2", winning_score


class Recursive_Game:
    def __init__(self, p1_deck, p2_deck, game_num=1):
        self.round = 1
        self.game_num = game_num
        self.state_store = []
        self.p1_deck = copy(p1_deck)
        self.p2_deck = copy(p2_deck)

    def status(self):
        print(f"\n-- Round {self.round} (Game {self.game_num})--")
        print(f"Player 1's deck: {self.p1_deck}")
        print(f"Player 2's deck: {self.p2_deck}")
        print(f"Player 1 plays: {self.p1_deck[0]}")
        print(f"Player 2 plays: {self.p2_deck[0]}")

    def adjust_deck(self, winner):
        if winner == "P1":
            self.p1_deck.append(self.p1_deck.pop(0))
            self.p1_deck.append(self.p2_deck.pop(0))
        elif winner == "P2":
            self.p2_deck.append(self.p2_deck.pop(0))
            self.p2_deck.append(self.p1_deck.pop(0))
        else:
            raise ValueError("Unexpected Winner")

    def check_occured(self):
        for i in self.state_store:
            if (self.p1_deck, self.p2_deck) == i:
                return True
        return False

    def play_round(self):
        self.status()
        self.state_store.append((copy(self.p1_deck), copy(self.p2_deck)))
        card_p1 = self.p1_deck[0]
        card_p2 = self.p2_deck[0]
        if card_p1 < len(self.p1_deck) and card_p2 < len(self.p2_deck):
            print(f"Playing a sub-game to determine the winner...")
            subgame = Recursive_Game(
                copy(self.p1_deck[1 : self.p1_deck[0] + 1]),
                copy(self.p2_deck[1 : self.p2_deck[0] + 1]),
                self.game_num + 1,
            )
            winner, score = subgame.run_game()
            self.adjust_deck(winner)
        elif card_p1 > card_p2:
            print("Player 1 wins the round!")
            self.adjust_deck("P1")
        elif card_p1 < card_p2:
            print("Player 2 wins the round!")
            self.adjust_deck("P2")
        else:
            raise ValueError("don't know what to do")
        self.round += 1

    def run_game(self):
        while self.p1_deck and self.p2_deck:
            if self.check_occured():
                print(f"The INSTANT winner of game {self.game_num} is player 1!")
                return "P1", None
            else:
                self.play_round()

        print(f"\n== Post-game {self.game_num} results ==")
        print(f"Player 1's deck: {self.p1_deck}")
        print(f"Player 2's deck: {self.p2_deck}")

        p1_score = sum(
            ind * val
            for ind, val in zip(self.p1_deck, list(range(len(self.p1_deck), 0, -1)))
        )
        p2_score = sum(
            ind * val
            for ind, val in zip(self.p2_deck, list(range(len(self.p2_deck), 0, -1)))
        )
        winning_score = max(p1_score, p2_score)
        print(f"Winning score {winning_score}")

        if winning_score == p1_score:
            print(f"Player 1 Wins game {self.game_num}!")
            return "P1", winning_score
        else:
            print(f"Player 2 Wins game {self.game_num}!")
            return "P2", winning_score


def parse_input(puzzle_input):
    player_decks = []
    deck = []
    for line in puzzle_input:
        if line.isdigit():
            deck.append(int(line))
        elif deck:
            player_decks.append(deck)
            deck = []
    if deck:
        player_decks.append(deck)
        deck = []
    return player_decks


example = [
    "Player 1:",
    "9",
    "2",
    "6",
    "3",
    "1",
    "Player 2:",
    "5",
    "8",
    "4",
    "7",
    "10",
]

example2 = [
    "Player 1:",
    "43",
    "19",
    "Player 2:",
    "2",
    "29",
    "14",
]

# Part1
player_decks = parse_input(example)
game = Standard_Game(player_decks[0], player_decks[1])
game.run_game()

# Part2
player_decks = parse_input(puzzle_input)
game = Recursive_Game(player_decks[0], player_decks[1])
game.run_game()

print("")
