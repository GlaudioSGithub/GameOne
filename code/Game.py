import pygame

from code.Menu import Menu

class Game:
    def __init__(self):  #Construtor
        pygame.init()
        self.window = pygame.display.set_mode(size=(800, 600))

    def run(self):
        while True:
                menu = Menu(self.window)   # Chamar a tela de Menu
                menu.run()
                pass

            # Check for all events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()   # Close Window
            #         quit()  # end pygame