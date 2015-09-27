from twozerofoureight import *

game_board = board()
	
game_board.generate_newpiece("start")
game_board.generate_newpiece("start")
game_board.print_board("normal")

def move(direction):
	original_board = list(game_board.board_list)
	if direction == "left":
		game_board.move_left_right("left")
	elif direction == "right":
		game_board.move_left_right("right")
	elif direction == "up":
		game_board.upkey()
	elif direction == "down":
		game_board.downkey()
	else:
		pass
	if original_board == game_board.board_list:
		game_board.generate_newpiece("checkforloss")
	else:
		game_board.generate_newpiece("normal")

def play():
	key = Arrow.input()
	while key != Arrow.NONE:
			# print(key)
			if key == Arrow.UP:
				move("up")
			elif key == Arrow.DOWN:
				move("down")
			elif key == Arrow.LEFT:
				move("left")				
			elif key == Arrow.RIGHT:
				move("right")
			key = Arrow.input()

	print("None of the arrow keys was pressed")


if __name__ == "__main__":
	play()
