import random

import pygame

from code.Const import WIN_HEIGHT, COLOR_WHITE, MENU_OPTIONS, EVENT_ENEMY, SPAW_TIME
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.helpers import check_events


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.timeout = 20000
        self.entity_list.extend(EntityFactory.get_entity("Level1Bg"))
        self.entity_list.append(EntityFactory.get_entity("Player1"))
        if game_mode in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            self.entity_list.append(EntityFactory.get_entity("Player2"))

        pygame.time.set_timer(EVENT_ENEMY, SPAW_TIME)

    def run(self):
        pygame.mixer_music.load(f'./assets/{self.name}.mp3')
        pygame.mixer_music.set_volume(0.3)
        # TODO: DECOMMENT
        # pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()  # manter taxa de atualização constante
        while True:
            clock.tick(60)  # FPS

            # EVENT
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                # if isinstance(ent, Player):
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # fechou, executo mesmo
                    pygame.quit()
                    quit()  # acabar com o pygame (init)
                if event.type == EVENT_ENEMY:
                    choice = random.choice(("Enemy1", "Enemy1", "Enemy2"))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

            # COLLISIONS
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
