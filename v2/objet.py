import random


def create(grid):
	position_x = random.randint(0,14)
	position_y = random.randint(0,14)

	if (grid[position_x][position_y] != 'X' and grid[position_x][position_y] != 'M' and
	grid[position_x][position_y] != 'O' and grid[position_x][position_y] != 'G' ) :
		return (position_x,position_y)
	else :
		create(grid)
