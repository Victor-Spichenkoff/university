import random

import pygame.image

from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    """
    - name deve ser com base nos assets
    """
    def __init__(self, name, position: tuple):
        print("NAME: " + name)
        super().__init__(name, position)




    def move(self):
        print(self.name)
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH