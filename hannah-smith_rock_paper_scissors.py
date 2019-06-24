"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
import time


def print_pause(string):
    print(string)
    time.sleep(1.5)


moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.score = 0
        self.player_move = 'rock'

    def move(self):
        return self.player_move

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()

    def learn(self, my_move, their_move):
        self.player_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()

    def learn(self, my_move, their_move):
        if my_move == 'rock':
            self.player_move = 'paper'
        elif my_move == 'paper':
            self.player_move = 'scissors'
        else:
            self.player_move = 'rock'


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        decision = input("Choose your move: Rock, paper, or scissors?"
                         " (Type 'quit' to quit.)\n").lower()
        if 'quit' in decision:
            exit()
        while True:
            if decision not in moves:
                print_pause("Invalid choice. Choose rock, "
                            "paper or scissors.")
                decision = input("Choose your move: Rock, "
                                 "paper, or scissors?\n").lower()
            else:
                return decision


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print_pause(f"Player 1: {move1}\nPlayer 2: {move2}")

        if beats(move1, move2):
            print_pause(f"{move1} beats {move2}. Player 1 wins this round.")
            self.p1.score += 1
            print_pause(f"Current Score:\nPlayer1: {self.p1.score}\t"
                        f"Player2: {self.p2.score}")
        elif beats(move2, move1):
            print_pause(f"{move2} beats {move1}. Player 2 wins this round.")
            self.p2.score += 1
            print_pause(f"Current Score:\nPlayer1: {self.p1.score}"
                        f"\tPlayer2: {self.p2.score}")
        else:
            print_pause(f"Tie. Choose your moves again.")
            print_pause(f"Current Score:\nPlayer1: {self.p1.score}"
                        f"\tPlayer2: {self.p2.score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print_pause("Game start! First to score 3 wins.")

        if isinstance(self.p1, HumanPlayer):
            print_pause("You are Player 1.")
        elif isinstance(self.p2, HumanPlayer):
            print_pause("You are Player 2.")

        round = 1
        while self.p1.score < 3 and self.p2.score < 3:
            print_pause(f"\nRound {round}:")
            self.play_round()
            round += 1
        if self.p1.score > self.p2.score:
            print_pause("\nPlayer 1 Wins!")
        else:
            print_pause("\nPlayer 2 Wins!")
        print_pause("Game over!")


if __name__ == '__main__':
    game = Game(ReflectPlayer(), RandomPlayer())
    game.play_game()
