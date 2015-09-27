from arrows import Arrow
from random import randrange
import os

def cls():
    os.system(['clear','cls'][os.name == 'nt'])

class board:
	board_list = []

	def __init__(self):
		for i in range(0,4):
			self.board_list.append([0,0,0,0])

	def move_left_right(self,direction):
		for n in range(len(self.board_list)):
			self.board_list[n] = [x for x in self.board_list[n] if x != 0]
			try:
				for i in range(len(self.board_list[n])-1):
					if self.board_list[n][i+1] == self.board_list[n][i]:
						self.board_list[n][i] = self.board_list[n][i] * 2
						del self.board_list[n][i+1]
			except:
				pass
			if direction == "left":
				while len(self.board_list[n]) != 4:
					self.board_list[n].append(0)
			elif direction == "right":
				while len(self.board_list[n]) != 4:
					self.board_list[n].insert(0,0)

	def print_board(self, condition):
		cls()
		# print "\n"
		for row in self.board_list:
			print row
		if condition == "win":
			print "WIN"
			quit()
		elif condition == "lose":
			print "LOSE"
			quit()
		else:
			pass


	def flip_board(self):
		reversed_list = []
		for row in self.board_list:
			reversed_list.append([])
		for row in self.board_list:
			for n in range(len(self.board_list)):
				reversed_list[n].append(row[n])
		self.board_list = list(reversed_list)

	def upkey(self):
		self.flip_board()
		self.move_left_right("left")
		self.flip_board()

	def downkey(self):
		self.flip_board()
		self.move_left_right("right")
		self.flip_board()

	def generate_newpiece(self, condition):
		x = randrange(0,4)
		y = randrange(0,4)
		newvalue = randrange(2,6,2)

		zeroes = 0
		for row in self.board_list:
			zeroes += row.count(0)

		win = 0
		for row in self.board_list:
			win += row.count(2048)

		if zeroes > 0 or condition == "start":
			while self.board_list[x][y] != 0:
				x = randrange(0,4)
				y = randrange(0,4)
			else:
				self.board_list[x][y] = newvalue

			self.print_board("normal")
		elif win > 0:
			self.print_board("win")
		elif zeroes == 0 and condition == "checkforloss":
			self.print_board("lose")
