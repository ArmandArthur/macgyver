import pygame
import math
import random
import win32api

screen = pygame.display.init()
playing = True

class Checkerboard():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.checker = [[1, 2, 1, 1, 1, 1, 1, 1, 1, 1],[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],[1, 0, 1, 0, 1, 1, 0, 1, 0, 1],[1, 0, 1, 0, 0, 0, 0, 0, 0, 1],[1, 0, 0, 0, 1, 0, 1, 0, 1, 1],[1, 1, 1, 0, 0, 0, 1, 0, 1, 1],[1, 0, 0, 0, 1, 0, 0, 0, 0, 1],[1, 0, 1, 1, 0, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]]
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.liste_objets_draw = {}
        self.liste_objets= {}
        self.counter_object = 0
        self.liste_objets_position = {}
        self.draw()
        self.instance_objets()

    def update(self):
        pygame.display.update()

    def instance_objets(self):
        self.liste_objets_position = {}
        self.liste_objets_draw['aiguille'] = self.new_aiguille()
        self.liste_objets_draw['ether'] = self.new_ether()
        self.liste_objets_draw['gardien'] = self.new_gardien()
        self.liste_objets = self.liste_objets_draw.copy()
        self.draw_objets()

    def verify_position_before_draw(self):
        position_x = random.randint(0,9)
        position_y = random.randint(0,9)

        if str(position_x)+str(position_y) not in self.liste_objets_position:
            self.liste_objets_position[str(position_x)+str(position_y)] = True
            position = {}
            position['x'] = position_x
            position['y'] = position_y
            return position
        else :
            self.verify_position_before_draw()

        
         

    def new_aiguille(self):
        position = self.verify_position_before_draw()
        print(position['x'])
        return Object(position['x'], position['y'],'object','images/aiguille.png')
    def new_ether(self):
        position = self.verify_position_before_draw()
        return Object(position['x'], position['y'],'object','images/ether.png')
    def new_gardien(self):
        return Personnage(9, 8, 'gardien', 'images/gardien.png')
    def draw_objets(self):
        isComplete = False
        iteration = 0

        for key in self.liste_objets_draw.items():
            #obj est un tuple comme (aiguille, objet)
            obj = key 
            if self.objectIsWall(obj[1]) == False:
                #self.screen.blit(pygame.image.load(obj[1].path).convert(), (obj[1].position_x*20,obj[1].position_y*20))
                isComplete =True
                iteration = iteration + 1
            elif self.objectIsWall(obj[1]) == True:
                isComplete = False


        if isComplete == True and iteration == len(self.liste_objets_draw):
            for key in self.liste_objets_draw.items():
                obj = key 
                self.screen.blit(pygame.image.load(obj[1].path).convert(), (obj[1].position_x*20,obj[1].position_y*20))
        else :            
            self.instance_objets()
        self.update()

    def draw(self):
        for key, line  in enumerate(self.checker):
            for index, case in enumerate(line):
                if case == 1 :
                    self.screen.blit(pygame.image.load('images/wall.png').convert(), (key*20,index*20))
                elif case == 0:
                    self.screen.blit(pygame.image.load('images/wall_free.png').convert(), (key*20,index*20))
                elif case == 2:
                    self.screen.blit(pygame.image.load('images/depart.png').convert(), (key*20,index*20))

        self.update()

    def update_macgyver(self,macgyver):
        self.screen.blit(pygame.image.load(macgyver.path).convert(), (macgyver.position_x*20,macgyver.position_y*20))
        return macgyver
        #block = pygame.Surface((20, 20))
        #block_pos = block.get_rect()
        #block.convert()
        #pygame.draw.rect(block, 000, ((0, 0), block_pos.size))
    
    def delete_macgyver(self,macgyver):
            self.screen.blit(pygame.image.load('images/wall_free.png').convert(), (macgyver.old_position_x*20,macgyver.old_position_y*20))

    def positionIsWall(self,macgyver):
        if self.checker[macgyver.position_x][macgyver.position_y] == 1 or self.checker[macgyver.position_x][macgyver.position_y] == 2 :
            return True
        else:
            return False

    def objectIsWall(self, object_item):
        if self.checker[object_item.position_x][object_item.position_y] == 1 or self.checker[object_item.position_x][object_item.position_y] == 2 :
            return True
        else:
            return False

    def verify_if_objects_is_on_the_case(self, macgyver):
        for i in self.liste_objets.items() :
            if i[1].position_x == macgyver.position_x and i[1].position_y == macgyver.position_y and i[1].type != 'gardien':
                self.counter_object = self.counter_object + 1

    def verify_win(self, macgyver):
        if self.liste_objets['gardien'].position_x == macgyver.position_x and self.liste_objets['gardien'].position_y == macgyver.position_y and self.counter_object == 2:
            win32api.MessageBox(0, 'Vous avez gagné', 'Victoire')
            pygame.quit()
            exit()    
        elif self.liste_objets['gardien'].position_x == macgyver.position_x and self.liste_objets['gardien'].position_y == macgyver.position_y and self.counter_object != 2:
            win32api.MessageBox(0, 'Vous avez oublié de ramasser les objets','Défaite')
            pygame.quit()
            exit()
class Personnage():
    def __init__(self, position_x, position_y, type, path):
        self.position_x = position_x
        self.position_y = position_y
        self.old_position_x = position_x
        self.old_position_y = position_y
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

class Object():
    def __init__(self, position_x, position_y, type, path):
        self.position_x = position_x
        self.position_y = position_y
        self.type = type
        self.path = path


checkerboard = Checkerboard(200,200)
macgyver = Personnage(1,1,'heros','images/MacGyver.png')

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
                    checkerboard.verify_if_objects_is_on_the_case(macgyver)
                    checkerboard.verify_win(macgyver)
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
                    checkerboard.verify_if_objects_is_on_the_case(macgyver)
                    checkerboard.verify_win(macgyver)
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
                    checkerboard.verify_if_objects_is_on_the_case(macgyver)
                    checkerboard.verify_win(macgyver)                    
                else:
                    macgyver.move('up')

            if event.key == pygame.K_UP:
                macgyver.move('up')
                if checkerboard.positionIsWall(macgyver) == False:
                    checkerboard.delete_macgyver(macgyver)
                    checkerboard.update_macgyver(macgyver)
                    checkerboard.update()
                    checkerboard.verify_if_objects_is_on_the_case(macgyver)
                    checkerboard.verify_win(macgyver)                    
                else:
                    macgyver.move('down')       



    


