import pygame
from code.Entity import Entity  # Import da classe base

class Explosion(Entity):
    def __init__(self, position: tuple):
        super().__init__('Explosion', position)

        # Carrega os frames da explosão
        self.frames = [pygame.image.load(f'./assets/img/explosion{i}.png').convert_alpha() for i in range(5)]
        self.current_frame = 0
        self.frame_delay = 5  # ticks antes de mudar de frame
        self.counter = 0      # contador de ticks
        self.finished = False

        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=position)

    def move(self):
        self.counter += 1
        if self.counter >= self.frame_delay:
            self.counter = 0
            self.current_frame += 1
            if self.current_frame < len(self.frames):
                self.image = self.frames[self.current_frame]
            else:
                self.finished = True  # animação finalizada

    def draw(self, window):
        window.blit(self.image, self.rect)

