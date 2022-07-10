import time


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # sinle list to rep 3X3 board
        self.current_winner = None

    def print_board(self):
        # getting each rows
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' | ')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2| etc (shows which number corresponds to which box on the board)
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' | ')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_moves(self):  # check empty moves/space left on the board
        return ' ' in self.board

    def num_of_moves_left(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, then assign square to letter then return true, if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check for winner if 3 matches in row anywhere
        # check row
        row_ind = square // 3
        row = self.board[row_ind * 3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        # check column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # check diagonal for winner pattern
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right to left
            if all([spot == letter for spot in diagonal2]):
                return True
            # if there are no winning pattern
        return False


def play(game, x_player, o_player, print_game=True):
    # return winner of the game or None for draw
    if print_game:
        game.print_board_nums()

    letter = 'x'  # start letter
    # we keep looping while there's still empty squares
    while game.empty_moves():
        if letter == 'o':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # defining a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' make a move to sqaure {square}')
                game.print_board()
                print('')  # empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

                # after move is made, we need to change the letters
            letter = 'o' if letter == 'x' else 'x'  # to change player

        time.sleep(0.10)

    if print_game:
        print('it\'s a draw')
