from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # Veloc das imagens, do dicionario pega a palavra chame do nome
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH  # Quando a imagem chegar no final trazer o inicio da mesma