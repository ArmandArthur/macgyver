import os

class Character:

	def __init__(self):
		self.number_objet_getting = 0

	def create(self, data_file, character_name):
		directory = os.path.dirname(__file__)
		path_to_file = os.path.join(directory, 'data', data_file)

		position = []

		with open(path_to_file) as file:
			for line in file:
				spliter = line.split(' ')
				if(spliter[0] == character_name):
					return int(spliter[1]), int(spliter[2])

	def moove(self, maps, direction, position):

		position_x = int(position[0])
		position_y = int(position[1])

		position_x_general = 0
		position_y_general = 0

		# Commentaire
		if direction == 'l':
			position_x_general = position_x-1
			position_y_general = position_y
		elif direction == 'r':
			position_x_general = position_x+1
			position_y_general = position_y
		elif direction == 'u':
			position_x_general = position_x
			position_y_general = position_y-1
		elif direction == 'd':
			position_x_general = position_x
			position_y_general = position_y+1

		if maps[position_y_general][position_x_general] == 'X':
			print('Mur !')
		elif maps[position_y_general][position_x_general] in ['A','E', 'T']:
			self.number_objet_getting = self.number_objet_getting + 1
			maps[position_y][position_x] = ' '
			maps[position_y_general][position_x_general] = 'M'
		elif (maps[position_y_general][position_x_general] == 'G' and self.number_objet_getting < 3):
			print('Loose')
			exit()
		elif (maps[position_y_general][position_x_general] == 'G' and self.number_objet_getting == 3):
			print('Winning')
			exit()
		else :
			maps[position_y][position_x] = ' '
			maps[position_y_general][position_x_general] = 'M'

		return maps