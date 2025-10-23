import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOT, ENTITY_SHOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):  # Erda os atributos da Entidade
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        # 🔊 Carrega som de tiro
        self.snd_shoot = pygame.mixer.Sound('./assets/snd/shoot.wav')
        self.snd_shoot.set_volume(0.5)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_KEY_RIGHT[self.name]] and self.rect.left < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay <= 0:
            self.shot_delay = ENTITY_SHOT_DELAY.get(self.name, 60)
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[PLAYER_KEY_SHOT[self.name]]:
                # 🔊 toca o som AQUI, antes de criar o tiro
                self.snd_shoot.play()

                # reseta o delay e cria o tiro
                self.shot_delay = ENTITY_SHOT_DELAY[self.name]

                # cria um tiro temporário para pegar a altura do sprite
                temp_shot = PlayerShot(name=f'{self.name}Shot', position=(0, 0))

                # calcula a posição do tiro
                offset_x = -7  # ajusta horizontalmente, negativo se necessário para "encostar" na nave
                shot_x = self.rect.right + offset_x
                shot_y = self.rect.top + (self.rect.height // 2) - (temp_shot.rect.height // 2)

                return PlayerShot(name=f'{self.name}Shot', position=(shot_x, shot_y))


