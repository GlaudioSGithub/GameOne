# code/Explosion.py
import pygame
from code.Entity import Entity

class Explosion(Entity):
    def __init__(self, x, y):
        # ✅ Passa um tuple (x, y) como segundo argumento, conforme Entity
        super().__init__('Explosion', (x, y))

        # Substitui a imagem padrão pela da explosão
        self.surf = pygame.image.load('./assets/img/explosion.png').convert_alpha()
        self.rect = self.surf.get_rect(center=(x, y))

        # Duração curta antes de sumir (frames)
        self.life_timer = 15
        self.health = 1
        self.damage = 0
        self.score = 0

    def move(self):
        # Explosão não se move — apenas “vive” por um tempo e some
        self.life_timer -= 1
        if self.life_timer <= 0:
            self.health = 0


