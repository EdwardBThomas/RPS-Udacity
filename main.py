"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

import random
# from itertools import cycle
# cycled_moves = cycle(moves)


class Player:
    score = 0

    def __init__(self):
        self.p1_move = random.choice(moves)
        self.p2_move = random.choice(moves)

    def name(self): #code to display the player name: Cycle, Reflect...
        return self.__class__.__name__

    def learn(self, p1_move, p2_move):
        pass


class RockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def move(self):
        return self.p2_move

    def learn(self, p1_move, p2_move):
        self.p2_move = p2_move
        # if self.p2_move is None:
        #     return random.choice(moves)
        # else:
        #     return self.p2_move


class CyclePlayer(Player):

    def __init__(self):
        super().__init__()
        self.index = None
        #A PyCharm prompt stated a self.index was necessary to make the
        # modulus operation work; another PyCharm prompt said a super() was
        # needed to make the self.index work...

    def learn(self, p1_move, p2_move):
        self.p1_move = p1_move

    # def move(self):
    #     if self.p1_move is None:
    #         return random.choice(moves)
    #     else:
    #         while True:
    #             move = moves[self.index]
    #             self.index = (self.index + 1) % len(moves)

    def move(self):
        if self.p1_move is None:
            return random.choice(moves)
        else:
            move = moves[self.index]
            self.index = (self.index + 1) % len(moves)

    # def move(self):
    #     move = moves[self.index]
    #     self.index = (self.index + 1) % len(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Enter 'rock', 'paper', or 'scissors'.")
            if move in moves:
                return move
            else:
                print('Wrong move.')


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move
        move2 = self.p2.move
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if self.p1.move == self.p2.move:
            print("A tie.")
        elif beats(self.p1.move, self.p2.move):
            self.p1.score += 1
        else:
            self.p2.score += 1

    def play_game(self):
        print("Game start!")
        for round in range(5):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    strategies = [
        CyclePlayer(),
        RockPlayer(),
        RandomPlayer(),
        ReflectPlayer()
    ]
    p1 = HumanPlayer()
    p2 = CyclePlayer()
    game = Game(p1, p2)
    game.play_game()
