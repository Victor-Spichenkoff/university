from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.Entity import Entity


class EnemyShot(Entity):
    def __init__(self, name, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]