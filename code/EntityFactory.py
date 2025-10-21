import random

import pygame

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case "Level1Bg":
                list_bg = []
                # Chamar as imagens
                for i in range(1, 8):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))  # Chamar as 7 imagens
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            # ----- PLAYERS -----
            case "Player1":
                return Player("Player1", (10, WIN_HEIGHT / 2 - 30))
            case "Player2":
                return Player("Player2", (10, WIN_HEIGHT / 2 + 30))

            # ----- ENEMIES -----
            case "Enemy1":
                enemy = Enemy("Enemy1", (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
                enemy.surf = pygame.transform.flip(enemy.surf, True, False)  # Flip horizontal
                return enemy
            case "Enemy2":
                enemy = Enemy("Enemy2", (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
                enemy.surf = pygame.transform.flip(enemy.surf, True, False)
                return enemy

