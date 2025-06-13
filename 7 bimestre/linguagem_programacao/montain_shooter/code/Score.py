import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font
from pygame import Surface

from code.Const import COLOR_YELLOW, SCORE_POS, MENU_OPTIONS, COLOR_WHITE
from code.DbProxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surface = pygame.image.load("./assets/ScoreBg.png").convert_alpha()
        self.rect = self.surface.get_rect(left=0, top=0)  # rect -> retângulo

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load("./assets/Score.mp3")
        # TODO: DESCOMENTAR PARA MÚSICA
        pygame.mixer_music.play(-1)  # toca; -1 -> infinito

        db_proxy = DBProxy("DBScore")
        name = ""

        while True:
            self.window.blit(source=self.surface, dest=self.rect)
            self.score_text(48, "You WIN!!!", COLOR_YELLOW, SCORE_POS['Title'])
            text = ""
            score = -1
            if game_mode == MENU_OPTIONS[0]:
                score = player_score[0]
                text = "Player 1 enter your name (4 characters)"
            if game_mode == MENU_OPTIONS[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = "Enter team name (4 characters)"
            if game_mode == MENU_OPTIONS[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = "Player 1 enter your name (4 characters)"
                else:
                    score = player_score[0]
                    text = "Player 2 enter your name (4 characters)"

            self.score_text(20, text, COLOR_WHITE, SCORE_POS['EnterName'])


            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # fechou, executo mesmo
                    pygame.quit()
                    quit()
                    # SALVAR O NOME (TYPING)
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({ "name": name, 'score': score, 'date': get_formatted_date() })
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name = name + event.unicode

            self.score_text(20, name, COLOR_WHITE, SCORE_POS['Name'])

            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load('./assets/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surface, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', COLOR_YELLOW, SCORE_POS['Title'])
        self.score_text(20, 'NAME     SCORE           DATE      ', COLOR_YELLOW, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}     {score:05d}     {date}', COLOR_YELLOW,
                            SCORE_POS[list_score.index(player_score)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()
    # def show(self):
    #     pygame.mixer_music.load("./assets/Score.mp3")
    #     # TODO: DESCOMENTAR PARA MÚSICA
    #     pygame.mixer_music.play(-1)  # toca; -1 -> infinito
    #
    #     self.score_text(48, 'TOP 10 SCORE', COLOR_YELLOW, SCORE_POS['Title'])
    #     self.score_text(20, 'NAME     SCORE           DATE      ', COLOR_YELLOW, SCORE_POS['Label'])
    #     self.window.blit(source=self.surface, dest=self.rect)
    #
    #     db_proxy = DBProxy("DBScore")
    #     list_score = db_proxy.retrieve_top10()
    #     db_proxy.close()
    #     for player_score in list_score:
    #         id_, name, score, date = player_score
    #         self.score_text(20, f'{name}     {score:05d}     {date}', COLOR_YELLOW,
    #                         SCORE_POS[list_score.index(player_score)])
    #
    #     while True:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:  # fechou, executo mesmo
    #                 pygame.quit()
    #                 quit()
    #             if event.type == pygame.KEYDOWN:
    #                 if event.key == K_ESCAPE:
    #                     return
    #
    #         pygame.display.flip()


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)



def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"