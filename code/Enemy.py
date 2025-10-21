from code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # Veloc das imagens, do dicionario pega a palavra chame do nome

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay <= 0:
            self.shot_delay = ENTITY_SHOT_DELAY.get(self.name, 60)
            # tiros saem da lateral esquerda do inimigo, centralizados verticalmente
            shot_x = self.rect.left
            shot_y = self.rect.top + self.rect.height // 2
            return EnemyShot(name=f'{self.name}Shot', position=(shot_x, shot_y))