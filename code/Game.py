import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):  # Construtor
        pygame.init()
        pygame.mixer.init()
        self.snd_shoot = pygame.mixer.Sound('./assets/snd/shoot.wav')
        self.snd_shoot.set_volume(0.5)  # volume de 0.0 a 1.0
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # Constante do tamanho da imagem

    def run(self):

        while True:
            score = Score(self.window)
            menu = Menu(self.window)  # Chamar a tela de Menu
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                # Inicializa pontuação e jogadores
                player_score = {'Player1': 0, 'Player2': 0, 'Player1_health': None, 'Player2_health': None}
                player_objects = {}  # vai guardar objetos Player entre fases

                # Fase 1
                level = Level(self.window, 'Level1', menu_return, player_score, players=player_objects)
                level_return = level.run(player_score)

                if level_return:
                    # Fase 2, mantém o mesmo modo de jogo e players
                    level = Level(self.window, 'Level2', menu_return, player_score, players=player_objects)
                    level_return = level.run(player_score)

                # Ao final, salva a pontuação
                score.save(game_mode=menu_return, player_score=[player_score['Player1'], player_score['Player2']],
                           name='')


            elif menu_return == MENU_OPTION[3]:
                score.show()

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Close Window
                quit()  # end pygame
            else:
                pass
