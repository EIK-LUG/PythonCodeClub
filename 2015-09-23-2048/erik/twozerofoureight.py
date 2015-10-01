import random
from arrows import Arrow


class TZFE:

    def __init__(self):
        self.board = [['-', '-', '-', '-'],
                      ['-', '-', '-', '-'],
                      ['-', '-', '-', '-'],
                      ['-', '-', '-', '-']]

        self.open_two()
        self.open_two()

    def play(self):
        self.print_board()

        key = Arrow.input()
        while key != Arrow.NONE and self.game_going():
            self.arrange_board(key)
            self.open_two()
            self.open_two()
            self.print_board()
            key = Arrow.input()

        if self.game_going():
            print("None of the arrow keys was pressed")
        else:
            print("Game over!")

    def move_left(self):
        moved = False
        for j in range(3):
            for i in range(4):
                if self.board[i][j] == '-' and self.board[i][j+1] != '-':
                    self.board[i][j], self.board[i][j+1] = self.board[i][j+1], self.board[i][j]
                    moved = True
        if moved:
            self.move_left()

    def merge_left(self):
        self.move_left()
        merged = False
        for j in range(3):
            for i in range(4):
                if self.board[i][j] == self.board[i][j+1] and self.board[i][j] != '-':
                    self.board[i][j] *= 2
                    self.board[i][j+1] = '-'
                    merged = True
        if merged:
            self.merge_left()

    def arrange_board(self, key):
        # bit hacky, but w/e :-)
        if key == Arrow.LEFT:
            self.merge_left()
        elif key == Arrow.RIGHT:
            self.reverse_board_rows()
            self.merge_left()
            self.reverse_board_rows()
        elif key == Arrow.UP:
            self.transpose_board()
            self.merge_left()
            self.transpose_board()
        elif key == Arrow.DOWN:
            self.transpose_board()
            self.reverse_board_rows()
            self.merge_left()
            self.reverse_board_rows()
            self.transpose_board()

    def reverse_board_rows(self):
        for i in range(len(self.board)):
            self.board[i] = list(reversed(self.board[i]))

    def transpose_board(self):
        self.board = [list(row) for row in zip(*self.board)]

    def open_two(self):
        indices = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == '-']
        i, j = random.choice(indices)
        self.board[i][j] = 2

    def print_board(self):
        for row in self.board:
            print(''.join(self.add_spaces(nr) for nr in row))
        print('')

    @staticmethod
    def add_spaces(nr):
        spaces = 6 - len(str(nr))
        spaces_before = spaces // 2
        spaces_after = spaces - spaces_before
        return '{}{}{}'.format(' ' * spaces_before, nr, ' ' * spaces_after)

    def game_going(self):
        sum_empty = sum([1 for i in range(4) for j in range(4) if self.board[i][j] == '-'])
        if sum_empty == 0:
            return False
        has_2048 = sum([1 for i in range(4) for j in range(4) if self.board[i][j] == 2048]) > 0
        if has_2048:
            return False

        return True