import random

class Objet:
	def create(self, grid):
		position_x = random.randint(0, 14)
		position_y = random.randint(0, 14)
		if (grid[position_x][position_y] == ' '):
			return (position_x, position_y)
		else:
			return self.create(grid)