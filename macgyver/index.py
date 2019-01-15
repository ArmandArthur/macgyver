import pygame
import math

screen = pygame.display.init() 
playing = True


class Checkerboard():
    
    def __init__(self, width, height):
    	self.width = width
    	self.height = height
    	self.image_macgyver = ''
    	self.checker = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1],[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],[1, 0, 1, 0, 1, 1, 0, 1, 0, 1],[1, 0, 1, 0, 0, 0, 0, 0, 0, 1],[1, 0, 0, 0, 1, 0, 1, 0, 1, 1],[1, 1, 1, 0, 0, 0, 1, 0, 1, 1],[1, 0, 0, 0, 1, 0, 0, 0, 0, 1],[1, 0, 1, 1, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]]
    	self.screen = pygame.display.set_mode((self.width ,self.height))
    	self.draw()

    def update(self):
	    pygame.display.update()

    def draw(self):
    	for key, line  in enumerate(self.checker):
    		for index, case in enumerate(line):
    		    if case == 1 :
    		    	self.screen.blit(pygame.image.load('wall.png').convert(), (key*20,index*20))
    		    elif case == 0:
    		    	self.screen.blit(pygame.image.load('wall_free.png').convert(), (key*20,index*20))
    	self.update()

    def update_macgyver(self,macgyver):
    	if self.image_macgyver == '':
    		self.load_image_macgyver(macgyver)
    	self.screen.blit(self.image_macgyver, (macgyver.position_x*20,macgyver.position_y*20))
    	return macgyver
    	#block = pygame.Surface((20, 20))
    	#block_pos = block.get_rect()
    	#block.convert()
    	#pygame.draw.rect(block, 000, ((0, 0), block_pos.size))
    
    def delete_macgyver(self,macgyver):
    		self.screen.blit(pygame.image.load('wall_free.png').convert(), (macgyver.old_position_x*20,macgyver.old_position_y*20))

    def positionIsWall(self,macgyver):
    	if self.checker[macgyver.position_x][macgyver.position_y] == 1:
    		return True
    	else:
    	    return False

    def load_image_macgyver(self,macgyver):
    	self.image_macgyver = pygame.image.load(macgyver.path).convert()

class Personnage():
    def __init__(self, position_x, position_y, type, path):
    	self.position_x = position_x
    	self.position_y = position_y
    	self.next_position_x = 1
    	self.next_position_y = 1
    	self.type = type
    	self.path = path

    def move(self, direction):
    	self.old_position_y = self.position_y
    	self.old_position_x = self.position_x
    	if direction == 'right':
    		self.position_x = self.position_x +1
    	if direction == 'down':
    		self.position_y = self.position_y +1
    	if direction == 'up':
    		self.position_y = self.position_y -1    		
    	if direction == 'left':
    		self.position_x = self.position_x -1    		

checkerboard = Checkerboard(200,200)
macgyver = Personnage(0,1,'heros','MacGyver.png')
checkerboard.update_macgyver(macgyver)
checkerboard.update()

while playing:
	#checkerboard.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_RIGHT:
        		macgyver.move('right')
	        	if checkerboard.positionIsWall(macgyver) == False:
	        		checkerboard.delete_macgyver(macgyver)
	        		checkerboard.update_macgyver(macgyver)
	        		checkerboard.update()
        		else:
        			# REVERSE POSITION MACGYVER
        			# dans le cas où c'est un mur
        			macgyver.move('left')
        	if event.key == pygame.K_LEFT:
        		macgyver.move('left')
	        	if checkerboard.positionIsWall(macgyver) == False:
	        		checkerboard.delete_macgyver(macgyver)
	        		checkerboard.update_macgyver(macgyver)
	        		checkerboard.update()
        		else:
        			# REVERSE POSITION MACGYVER
        			# dans le cas où c'est un mur
        			macgyver.move('right')        			
        	if event.key == pygame.K_DOWN:
        		macgyver.move('down')
	        	if checkerboard.positionIsWall(macgyver) == False:
	        		checkerboard.delete_macgyver(macgyver)
	        		checkerboard.update_macgyver(macgyver)
	        		checkerboard.update()
        		else:
        			macgyver.move('up')

        	if event.key == pygame.K_UP:
        		macgyver.move('up')
	        	if checkerboard.positionIsWall(macgyver) == False:
	        		checkerboard.delete_macgyver(macgyver)
	        		checkerboard.update_macgyver(macgyver)
	        		checkerboard.update()
        		else:
        			macgyver.move('down')		



	


