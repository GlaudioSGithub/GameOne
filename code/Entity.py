from abc import ABC, abstractmethod
import os
import pygame
from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        img_path = os.path.join('assets', 'img', f'{name}.png')

        if not os.path.isfile(img_path):
            print(f"⚠️ ERRO: arquivo de imagem não encontrado: {img_path}")
            # cria uma superfície de fallback rosa chamativa para debug
            self.surf = pygame.Surface((50, 50))
            self.surf.fill((255, 0, 255))
        else:
            self.surf = pygame.image.load(img_path).convert_alpha()

        self.rect = self.surf.get_rect(topleft=position)
        self.speed = 0
        self.health = ENTITY_HEALTH.get(self.name, 1)  # evita KeyError se nome não existir
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        pass
