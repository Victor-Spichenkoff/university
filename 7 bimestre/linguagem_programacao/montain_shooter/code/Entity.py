from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):
    """
    - name deve ser com base nos assets
    """
    def __init__(self, name, position: tuple, ):
        self.name = name
        self.surf = pygame.image.load("./assets/" + name + ".png")
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0


    @abstractmethod
    def move(self):
        pass
