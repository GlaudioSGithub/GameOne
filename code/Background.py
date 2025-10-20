from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name] # Velocidade das imagens, do dicionario pega a palavra chame do nome
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH # Quando a imagem chegar no final trazer o inicio da mesma