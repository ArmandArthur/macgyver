"""
    Import os for file
 """
import os
from display import Display

class Grid:
    """
        Class Grid
    """
    display = 0

    def __init__(self):
        """
            Save display instance singleton
        """
        self.display = Display.getInstance()

    def loading(self, data_file):
        """
            Loading the map from a file .txt
            y(X1,X2),
            y1(X1,X2)
        """
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

    def set_position(self, name, position_tuple, maps):
        """
            Set the position of the object
        """
        if name == 'needle':
            letter = 'N'
        elif name == 'ether':
            letter = 'E'
        elif name == 'tube':
            letter = 'T'
        else:
            letter = ' '

        maps[position_tuple[0]][position_tuple[1]] = letter
        return maps

    def get_position_macgyver(self, maps):
        """
            Getting the position of MacGyver
        """
        for (index_y, line) in enumerate(maps):
            for (index_x, character) in enumerate(line):
                if character == 'M':
                    return (index_x, index_y)

    def draw(self, maps):
        """
            Set the position of the icone and load their image
        """

        for key, line in enumerate(maps):
            for index, tile in enumerate(line):
                if tile == 'X':
                    self.display.draw_tile('images/wall.png', index, key)
                elif tile == 'M':
                    self.display.draw_tile('images/MacGyver.png', index, key)
                elif tile == 'G':
                    self.display.draw_tile('images/gardien.png', index, key)
                elif tile == ' ':
                    self.display.draw_tile('images/wall_free.png', index, key)
                elif tile == 'N':
                    self.display.draw_tile('images/aiguille.png', index, key)
                elif tile == 'E':
                    self.display.draw_tile('images/ether.png', index, key)
                elif tile == 'T':
                    self.display.draw_tile('images/tube.png', index, key)
