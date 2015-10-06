from arrows import Arrow
import random

class TZFE:
    """2048 Game in python"""
    def __init__(self):
        self.board = [[ None for x in range(4)] for x in range(4)]
        self.init_gameboard()

    def init_gameboard(self):
        # init board.size/2 many spots
        for _ in range(int(len(self.board)/2)):
            while True:
                x = random.randrange(0, len(self.board))
                y = random.randrange(0, len(self.board))
                if not self.board[x][y]:
                    self.board[x][y] = random.choice((2, 4))
                    break
                else: # retry if there is a colision
                    pass

    def print_board(self):
        """MAGIC"""
        print(" "+("-------"*len(self.board[0]))[:-1])
        for row in self.board:
            print("|", end="")
            for cell in row:
                print("      |".format(str(cell)), end="")
            print("\n|", end="")
            for cell in row:
                if cell == None:
                    print("      |".format(str(cell)), end="")
                else:
                    print(" {: ^4} |".format(str(cell)), end="")
            print("\n|", end="")
            for cell in row:
                print("      |".format(str(cell)), end="")
            print()
            print(" "+("-------"*len(row))[:-1])
        """MORE MAGIC"""

    def shift_up(self):
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    print("got cell", cell, "at", x, y)
                    if not (x-1 < 0):
                        print("moving cell", cell, "to", x-1, y)
                        if not self.board[x-1][y]:
                            print("cell", x-1, y, "empty")
                            self.board[x-1][y] = cell
                            self.board[x][y] = None

    def shift_down(self):
        pass

    def shift_left(self):
        pass

    def shift_right(self):
        pass

    def play(self):
        key = Arrow.input()
        while key != Arrow.NONE:
            print(key)
            key = Arrow.input()

        print("None of the arrow keys was pressed")

if __name__ == "__main__":
    g = TZFE()
    g.print_board()
    g.shift_up()
    g.print_board()
