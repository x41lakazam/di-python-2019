class GameBoard:

    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
                      ]

        self.map = {
            "A": [0,0],
            "B": [0,1],
            "C": [0,2],
            "D": [1,0],
            "E": [1,1],
            "F": [1,2],
            "G": [2,0],
            "H": [2,1],
            "I": [2,2]
        }

    def display_board(self):
        print("   |   |   ")
        print(" {} | {} | {} ".format(self.board[0][0], self.board[0][1], self.board[0][2]))
        print("___|___|___")
        print("   |   |   ")
        print(" {} | {} | {} ".format(self.board[1][0], self.board[1][1], self.board[1][2]))
        print("___|___|___")
        print("   |   |   ")
        print(" {} | {} | {} ".format(self.board[2][0], self.board[2][1], self.board[2][2]))
        print("   |   |   ")
        print("\n")

    def modify(self, fill_value, row, col):
        if self.board[row][col] != ' ':
            return False
        self.board[row][col] = fill_value
        return True

    def modify_ui(self, fill_value, letter):
        coords = self.map[letter.capitalize()]
        row = coords[0]
        col = coords[1]
        return self.modify(fill_value, row, col)

    def display_ui_board(self):

        print("   |   |   ")
        print(" A | B | C ")
        print("___|___|___")
        print("   |   |   ")
        print(" D | E | F ")
        print("___|___|___")
        print("   |   |   ")
        print(" G | H | I ")
        print("   |   |   ")

    def check_full_board(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def l2v(self, letter):
        coords = self.map[letter]
        row = coords[0]
        col = coords[1]
        return self.board[row][col]

    def check_win(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True

        # Check columns
        col1 = [self.l2v('A'), self.l2v('D'), self.l2v('G')]
        col2 = [self.l2v('B'), self.l2v('E'), self.l2v('H')]
        col3 = [self.l2v('C'), self.l2v('F'), self.l2v('I')]

        for col in [col1, col2, col3]:
            if col[0] == col[1] == col[2] != ' ':
                return True

        # Check diagonals
        if self.l2v('A') == self.l2v('E')== self.l2v('I')!= ' ':
            return True
        if self.l2v('C')== self.l2v('E')== self.l2v('G')!= ' ':
            return True

        return False
