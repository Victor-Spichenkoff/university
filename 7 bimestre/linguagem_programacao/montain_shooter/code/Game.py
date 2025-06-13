import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            game_mode = menu.run()

            if game_mode in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]:
                player_score = [0, 0]


                level = Level(self.window, "Level1", game_mode, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, "Level2", game_mode, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        score.save(game_mode, player_score)


            elif game_mode == MENU_OPTIONS[3]:
                score.show()
            elif game_mode == MENU_OPTIONS[4]:
                pygame.display.quit()
                quit()
