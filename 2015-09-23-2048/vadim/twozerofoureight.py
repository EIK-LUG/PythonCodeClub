from arrows import Arrow
import random


class TZFE:
    def __init__(self):
        self.game_board = [[" " for x in range(4)] for y in range(4)]

    def add_number(self):
        now = random.randrange(0, 100)
        if now < 80:
            number = 2
        else:
            number = 4
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        if self.game_board[row][col] == " ":
            self.game_board[row][col] = number
        else:
            self.add_number()

    def turn_finish(self):
        for row_number, row in enumerate(self.game_board):
            for col_number, col in enumerate(row):
                if col != ' ':
                    if col % 2 == 1:
                        self.game_board[row_number][col_number] -= 1

    def move(self, r, c, true_turn=True, moves=0):
        for row in range(4):
            for col in range(4):
                if self.game_board[row][col] != ' ':
                    if c == -1 and col > 0 or c == 1 and col < 3 or r == 1 and row < 3 or r == -1 and row > 0:
                        if self.game_board[row + r][col + c] == ' ':
                            moves += 1
                            if true_turn:
                                self.game_board[row + r][col + c] = self.game_board[row][col]
                                self.game_board[row][col] = ' '
                                self.move(r, c)
                        elif 0 <= row + r*2 <= 3 and 0 <= col + c*2 <= 3 and\
                                self.game_board[row + r][col + c] == self.game_board[row][col] and\
                                self.game_board[row + r*2][col + c*2] == self.game_board[row][col]:
                            pass
                        elif self.game_board[row + r][col + c] == self.game_board[row][col] and\
                                self.game_board[row + r][col + c] % 2 == 0 and\
                                self.game_board[row][col] % 2 == 0:
                            moves += 1
                            if true_turn:
                                self.game_board[row + r][col + c] = self.game_board[row][col] * 2 + 1
                                self.game_board[row][col] = ' '
                                self.move(r, c)
        return moves

    def turn(self, key, true_turn=True):
        if key == Arrow.LEFT:
            moves = self.move(0, -1, true_turn)
        if key == Arrow.RIGHT:
            moves = self.move(0, 1, true_turn)
        if key == Arrow.DOWN:
            moves = self.move(1, 0, true_turn)
        if key == Arrow.UP:
            moves = self.move(-1, 0, true_turn)
        return moves

    def print_board(self):
        print("-"*28)
        print()
        for i in self.game_board:
            for j in i:
                print("|", end="")
                print("{: ^5}".format(j), end="")
                print("|", end="")
            print()
            print()
            print("-"*28)
            print()

    def lose_check(self):
        for j in self.game_board:
            for i in j:
                if i == ' ':
                    break
                virtual_moves = 0
                for key in [Arrow.UP, Arrow.DOWN, Arrow.LEFT, Arrow.RIGHT]:
                    virtual_moves += self.turn(key, False)
                if virtual_moves == 0:
                    print("You lost!")
                    return True
        return False
    def play(self):
        self.add_number()
        self.add_number()
        self.print_board()
        key = Arrow.input()
        while key != Arrow.NONE:
            print(key)
            moves = self.turn(key)
            if moves != 0:
                self.turn_finish()
                self.add_number()
            self.print_board()
            if self.lose_check():
                break
            key = Arrow.input()

        print("None of the arrow keys was pressed")
