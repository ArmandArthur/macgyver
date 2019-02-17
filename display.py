import pygame


class Display:
    # Instance.
    __instance = None

    @staticmethod
    def getInstance():
        """
        Instance if not exist
        """
        if Display.__instance == None:
            Display()
        return Display.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Display.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Display.__instance = self

    def init_pygame(self, macgyver, maps, grid):
        self.pygame = pygame
        self.window = pygame.display.init()
        self.pygame.display.set_caption('MacGyver')
        self.screen = pygame.display.set_mode((300, 320))
        self.font_init = pygame.font.init()

        self.macgyver = macgyver
        self.maps = maps
        self.grid = grid

    def update(self):
        self.pygame.display.update()

    def set_text(self, text):
        self.screen.fill((255, 255, 255))
        self.draw_text(text)

    def draw_text(self, text):
        main_font = self.pygame.font.SysFont("Arial", 20)
        text_surf, text_rect = self.text_objects(text, main_font)
        text_rect.center = (150, 310)
        self.screen.blit(text_surf, text_rect)

    def text_objects(self, text, font):
        text_surface = font.render(text, True, (0, 0, 0))
        return text_surface, text_surface.get_rect()

    def draw_tile(self, image, position_x, position_y):
        self.screen.blit(self.pygame.image.load(image), [position_x * 20, position_y * 20])

    def listener(self):
        playing = True

        while playing:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    playing = False
                elif event.type == self.pygame.KEYDOWN:
                    position_macgyver = self.grid.get_position(self.maps, 'M')
                    if event.key == self.pygame.K_RIGHT:
                        self.maps = self.macgyver.move(self.maps, 'r', position_macgyver)
                    if event.key == self.pygame.K_LEFT:
                        self.maps = self.macgyver.move(self.maps, 'l', position_macgyver)
                    if event.key == self.pygame.K_DOWN:
                        self.maps = self.macgyver.move(self.maps, 'd', position_macgyver)
                    if event.key == self.pygame.K_UP:
                        self.maps = self.macgyver.move(self.maps, 'u', position_macgyver)

                    # Redraw
                    self.grid.draw(self.maps)
                    self.update()

