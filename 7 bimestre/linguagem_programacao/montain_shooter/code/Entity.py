from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    """
    - name deve ser com base nos assets
    """
    def __init__(self, name, position: tuple, ):
        self.name = name
        self.surf = pygame.image.load("./assets/" + name + ".png").convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.last_damage = "None"
        self.score = ENTITY_SCORE[self.name]


    @abstractmethod
    def move(self):
        pass
