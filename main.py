import random


moves = ['rock', 'paper', 'scissors']


class Player:
    p1_move = random.choice(moves)
    p2_move = random.choice(moves)

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


class CyclePlayer(Player):
    def move(self):
        index = moves.index(self.p1_move) + 1
        if index >= len(moves):
            index = 0
        return moves[index % len(moves)]

    def learn(self, p1_move, p2_move):
        self.p1_move = p1_move


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
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player One: {move1}  Player Two: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if move1 == move2:
            print("A tie.")
        elif beats(move1, move2):
            print("Player One wins this round.")
            self.p1_score += 1
        else:
            print("Player Two wins this round.")
            self.p2_score += 1
        print(f"Scores: Player One, {self.p1_score}; Player Two,"
              f" {self.p2_score}")

    def play_game(self):
        length = None
        while True:
            length = input('How many rounds to play? Numeric '
                           'integers like 3 or 7 only.')
            try:
                length = int(length)
                break
            except:
                continue
        for round in range(length):
            print(f"Round {round+1} of {length}:")
            self.play_round()
        if self.p1_score > self.p2_score:
            print(f"Player One wins with a score of {self.p1_score}.")
        elif self.p1_score == self.p2_score:
            print(f"The game is a tie at {self.p1_score}.")
        else:
            print(f"Player Two wins with a score of {self.p2_score}.")


if __name__ == '__main__':
    strategies = [
        CyclePlayer(),
        RockPlayer(),
        RandomPlayer(),
        ReflectPlayer()
    ]
    p1 = HumanPlayer()
    p2 = random.choice(strategies)
    game = Game(p1, p2)
    game.play_game()
