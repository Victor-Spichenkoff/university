from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShoot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShoot import PlayerShot


class EntityMediator:
    # __ -> privado
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, (Enemy, EnemyShot)):
            if ent.rect.right < 0:
                ent.health = 0
                ent.last_damage = "None"
        if isinstance(ent, PlayerShot):
            if ent.rect.left > WIN_WIDTH:
                ent.health = 0
                ent.last_damage = "None"

    @staticmethod
    def __verify_collision_entity(ent1: Entity, ent2: Entity):
        is_valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            is_valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            is_valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            is_valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            is_valid_interaction = True

        if not is_valid_interaction:
            return None

        if (ent1.rect.right >= ent2.rect.left and
            ent1.rect.left <= ent2.rect.right and
            ent1.rect.bottom >= ent2.rect.top and
            ent1.rect.top <= ent2.rect.bottom):
            ent1.health -= ent2.damage
            ent1.last_damage = ent2.name
            ent2.health -= ent1.damage
            ent2.last_damage = ent1.name


        return None


    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_damage == "Player1Shot":
            # procura pelo player 1
            for ent in entity_list:
                if ent.name == "Player1":
                    ent.score += enemy.score
        elif enemy.last_damage == "Player2Shot":
            # procura pelo player 1
            for ent in entity_list:
                if ent.name == "Player2":
                    ent.score += enemy.score


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)

            # colisão entre
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)


    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
