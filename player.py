import math
import random


class Player:
    def __init__(self, letter):
        # letter id x or o
        self.letter = letter

    # players to get their next move
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        squares = random.choice(game.available_moves())
        return squares


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_moves = False
        val = None
        while not valid_moves:
            squares = input(self.letter + '\'s turn. Enter your move (0-8: )')
            # check the value is correct by trying to cast casting to integer and if its not we say its invalid
            # and if not available we say its we say its invalid
            try:
                val = int(squares)
                if val not in game.available_moves():
                    raise ValueError
                valid_moves = True  # succesful move, GOOD!
            except ValueError:
                print('Invalid Move, try again')
        return val


