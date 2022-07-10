from player import HumanPlayer, RandomComputerPlayer
from game import TicTacToe, play

if __name__ == '__main__':
    x_player = HumanPlayer('x')
    o_player = RandomComputerPlayer('o')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)