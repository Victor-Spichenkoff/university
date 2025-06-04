import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            game_mode = menu.run()

            if game_mode in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]:
                level = Level(self.window, "Level 1", game_mode)
                level_return = level.run()
            elif game_mode == MENU_OPTIONS[3]:
                pass
            elif game_mode == MENU_OPTIONS[4]:
                pygame.display.quit()
                quit()
