
import random

number_objet_getting = 0

def create(grid):
	position_x = random.randint(0,14)
	position_y = random.randint(0,14)

	if (grid[position_x][position_y] != 'X' and grid[position_x][position_y] != 'M' and
	grid[position_x][position_y] != 'O' and grid[position_x][position_y] != 'G' ) :		
		return (position_x,position_y)
	else :
		create(grid)

def moove(maps, direction, position):
	global number_objet_getting

	position_x = int(position[0])
	position_y = int(position[1])

	position_x_general = 0
	position_y_general = 0

	if(direction == 'l'):
		position_x_general = position_x-1
		position_y_general = position_y
	if(direction == 'r'):
		position_x_general = position_x+1
		position_y_general = position_y
	if(direction == 'u'):
		position_x_general = position_x
		position_y_general = position_y-1
	if(direction == 'd'):
		position_x_general = position_x
		position_y_general = position_y+1

	if maps[position_y_general][position_x_general] == 'X':
		print('Mur !')
	elif maps[position_y_general][position_x_general] == 'O':
		number_objet_getting = number_objet_getting + 1
		maps[position_y][position_x] = ' '
		maps[position_y_general][position_x_general] = 'M'
	elif (maps[position_y_general][position_x_general] == 'G' and number_objet_getting < 3):
		print('Loose')
		exit()
	elif (maps[position_y_general][position_x_general] == 'G' and number_objet_getting == 3):
		print('Winning')
		exit()
	else :
		maps[position_y][position_x] = ' '
		maps[position_y_general][position_x_general] = 'M'

	return maps