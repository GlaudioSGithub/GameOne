# Quando o inimigo passa da tela ele ainda continua existindo
# Necessario destrui-lo para não ocupar memoria
import pygame

from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot

pygame.init()
pygame.mixer.init()

class EntityMediator:
    # 🔊 Som de explosão (carregado uma única vez)
    explosion_snd = pygame.mixer.Sound('./assets/snd/explosion.wav')
    explosion_snd.set_volume(0.6)

    @staticmethod
    def __verify_collision_window(ent: Entity):  # Metodo privado que só funciona aqui dentro
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):  # Verificação de colisão entre entidades
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        # Perguntas sobre a Colisão
        # A borda Direita de Ent1 está a Direita da borda Esquerda de Ent2?
        # A borda Esquerda de Ent1 está a Esquerda da borda Direita de Ent2?
        # A borda Inferior de Ent1 está a Abaixo da borda Superior de Ent2?
        # A borda Superior de Ent1 está a Acima da borda Inferior de Ent2?
        if valid_interaction:  # if valid_interaction == True:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):

                ent1.health -= ent2.damage  # A vida da Ent1 diminui de acordo com o dano da Ent2
                ent2.health -= ent1.damage
                # para pontuação
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':  # Se Enemy foi morto pelo Player1
            for ent in entity_list:
                if ent.name == 'Player1':  # Encontro o Player1
                    ent.score += enemy.score
        if enemy.last_dmg == 'Player2Shot':  # Se Enemy foi morto pelo Player2
            for ent in entity_list:
                if ent.name == 'Player2':  # Encontro o Player2
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    # 💣 Mata as entidades e toca som de explosão
    # Mata as entidades
    @staticmethod
    # def verify_health(entity_list: list[Entity]):
    #     entity_list[:] = [ent for ent in entity_list if ent.health > 0]
    def verify_health(entity_list: list[Entity]):
        to_remove = []
        for ent in entity_list:
            if ent.health <= 0:
                # ✅ toca som apenas se for inimigo ou jogador (não para tiros)
                if isinstance(ent, (Enemy, Player)):
                    EntityMediator.explosion_snd.play()

                # ✅ dá pontuação se foi inimig
                if isinstance(ent, Entity):
                    EntityMediator.__give_score(ent, entity_list)

                to_remove.append(ent)

        # Remove todos depois do loop (evita erro de alteração da lista)
        for ent in to_remove:
            if ent in entity_list:
                entity_list.remove(ent)
