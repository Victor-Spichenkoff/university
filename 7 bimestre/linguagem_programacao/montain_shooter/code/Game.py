import pygame

from code.Cont import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):


        while True:
            menu = Menu(self.window)
            menu.run()
            # get events

