import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_ORANGE, MENU_OPTION, C_WHITE, C_YELLOW


class Menu:

    def __init__(self, window):
        self.window = window
        # DRAW IMAGES
        self.surf = pygame.image.load('./assets/img/Menu.png').convert_alpha()  # Carregar o Background
        self.rect = self.surf.get_rect(left=0, top=0)  # Desenhar um retangulo

    def run(self, ):
        menu_option = 0
        # Adicionar som
        pygame.mixer_music.load('./assets/snd/Menu.wav')  # Importar musica
        pygame.mixer_music.play(-1)  # Tocar infinito (-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # Imagem aparecer no retangulo
            # Titulo
            self.menu_text(50, "Space", C_ORANGE, ((WIN_WIDTH / 2), 70))  # NOmeio do exixo X na altura de 70
            self.menu_text(50, "Defender", C_ORANGE, ((WIN_WIDTH / 2), 120))  # NOmeio do exixo X na altura de 120

            # OPTIONS
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW,
                                   ((WIN_WIDTH / 2), 200 + 25 * i))  # NOmeio do exixo X na altura de 70
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE,
                                   ((WIN_WIDTH / 2), 200 + 25 * i))  # NOmeio do exixo X na altura de 70

            pygame.display.flip()  # Atualizar a tela

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # If is DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # If is UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option < len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # If is ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
