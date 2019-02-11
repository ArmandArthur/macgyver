import os


class Grid:

	def loading(self,data_file):

		directory = os.path.dirname(__file__)
		path_to_file = os.path.join(directory, 'data', data_file)

		grid = []

		with open(path_to_file) as file:
			for line in file:
				maps = []
				for character in line:
					if character != '\n':
						maps.append(character)
				grid.append(maps)
		return grid

	def set_position_macgyver(self,position_tuple, maps):
		maps[position_tuple[0]][position_tuple[1]] = 'M'
		return maps

	def set_position_gardien(self,position_tuple, maps):
		maps[position_tuple[0]][position_tuple[1]] = 'G'
		return maps

	def set_position_objet(self, nom, position_tuple, maps):
		if nom == 'aiguille':
			letter = 'A'
		elif nom == 'ether':
			letter = 'E'
		elif nom == 'tube':
			letter = 'T'
		maps[position_tuple[0]][position_tuple[1]] = letter
		return maps

	def get_position_macgyver(self, maps):
		for (y, line) in enumerate(maps):
			for (x, character) in enumerate(line):
				if character == 'M':
					return x, y


	def draw(self, pygame, screen, maps):
		for key, line in enumerate(maps):
			for index, case in enumerate(line):
				if case == 'X':
					screen.blit(pygame.image.load('images/wall.png'), [index * 20, key * 20])
				elif case == 'M':
					screen.blit(pygame.image.load('images/MacGyver.png'), [index * 20, key * 20])
				elif case == 'G':
					screen.blit(pygame.image.load('images/gardien.png'), [index * 20, key * 20])
				elif case == ' ':
					screen.blit(pygame.image.load('images/wall_free.png'), [index * 20, key * 20])
				elif case == 'A':
					screen.blit(pygame.image.load('images/aiguille.png'), [index * 20, key * 20])
				elif case == 'E':
					screen.blit(pygame.image.load('images/ether.png'), [index * 20, key * 20])
				elif case == 'T':
					screen.blit(pygame.image.load('images/tube_plastique.png'), [index * 20, key * 20])
