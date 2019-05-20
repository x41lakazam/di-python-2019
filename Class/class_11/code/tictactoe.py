import game
from board import GameBoard

from itertools import cycle

class TicTacToe(game.Game):

    def __init__(self, name, players=[]):
        super().__init__(name, players)
        self.board = GameBoard()

    def play_turn(self, player):
        while True:
            self.board.display_board()
            self.board.display_ui_board()
            userinput = input("Choose a letter..\n>>> ")
            if self.board.modify_ui(player.symbol, userinput):
                break
            else:
                print("This place isn't available")

    def play(self):
        assert len(self.players) == 2 # Make sure that 2 players are in the list

        players_cycle = cycle(self.players)

        while True:
            current_player = next(players_cycle)
            self.play_turn(current_player)
            win = self.board.check_win()
            if win:
                print("{} won".format(current_player.name))
                break
            full = self.board.check_full_board()
            if full:
                print("Draw")
                break

class TictactoePlayer(game.Player):

    def __init__(self, name, symbol):
        super().__init__(name)
        self.symbol = symbol

tictactoe = TicTacToe('tic tac toe')

player1 = TictactoePlayer("Mario", "X")
player2 = TictactoePlayer("Luigi", "O")

tictactoe.add_player(player1)
tictactoe.add_player(player2)

tictactoe.play()
#######