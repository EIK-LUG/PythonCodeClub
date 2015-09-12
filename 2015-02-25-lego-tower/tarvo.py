# TASK: https://dl.dropboxusercontent.com/u/61384159/Mek/20150225Tower.pdf #
###################################################################

# @param smallBricks number of available bricks, size: small (1 unit tall)
# @param bigBricks number of available bricks, size: big (5 units tall)
# @param towerHeight height of a tower we must build (in units)
def tower(smallBricks, bigBricks, towerHeight):
	SMALL_BRICK_HEIGHT = 1;
	BIG_BRICK_HEIGHT = 5;

	# laying small bricks (haha)
	for i in range(0, bigBricks):
		if (towerHeight >= BIG_BRICK_HEIGHT):
			towerHeight -= BIG_BRICK_HEIGHT;

	# laying big bricks (hehe)
	for j in range(0, smallBricks):
		if (towerHeight > 0):
			towerHeight -= SMALL_BRICK_HEIGHT;

	# printing the result
	if towerHeight == 0:
		print("We did it boys, tower has been successfully built!");
		return True;
	else:
		print("We got a deficit of ", towerHeight, " unit-size brick(s) - fuck this job, I'm out of here...");
		return False;


# Function calls
tower(3, 1, 9); #FALSE
tower(3, 1, 8); #TRUE
tower(3, 1, 4); #FALSE
tower(0, 0, 2); #FALSE