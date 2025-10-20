import pygame
from pygame import Surface, Rect
from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:

    def __init__(self, window):
        self.window = window
        # Adicionar imagem
        self.surf = pygame.image.load('./assets/img/Menu.png')  # Carregar o Background
        self.rect = self.surf.get_rect(left=0,top=0)  # Desenhar um retangulo

    def run(self, ):
        # Adicionar som
        pygame.mixer_music.load('./assets/snd/Menu.wav')  # Importar musica
        pygame.mixer_music.play(-1)     # Tocar infinito (-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # Imagem aparecer no retangulo
            # Titulo
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70)) # NOmeio do exixo X na altura de 70
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))  # NOmeio do exixo X na altura de 120

            # Opções
            for i in range(len(MENU_OPTION)):
                self.menu_text(30, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 30 * i))  # NOmeio do exixo X na altura de 70

            pygame.display.flip() # Atualizar a tela

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()   # Close Window
                    quit()  # end pygame

    def menu_text(self, text_size: int, text: str,text_color: tuple, text_center_pos: tuple):
           text_font = pygame.font.SysFont('Lucida Sans Typewriter', size=text_size)
           text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
           text_rect: Rect = text_surf.get_rect(center=text_center_pos)
           self.window.blit(source=text_surf, dest=text_rect)