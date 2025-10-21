from abc import ABC, abstractmethod

import pygame

from code.Const import ENTITY_HEALTH


class Entity(ABC):  # Classe abstrata
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/img/' + name + '.png').convert_alpha()  # Trata as imagens
        self.rect = self.surf.get_rect(left=position[0], top=position[1])  # x e y
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]

    @abstractmethod
    def move(self, ):
        pass
