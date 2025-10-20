import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu

class Game:
    def __init__(self):  #Construtor
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # Constante do tamanho da imagem

    def run(self):

        while True:
                menu = Menu(self.window)   # Chamar a tela de Menu
                menu.run()
                pass
