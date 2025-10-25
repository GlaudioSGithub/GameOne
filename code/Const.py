# C
import pygame
from pygame.examples.grid import WINDOW_WIDTH

# Define cores usadas no jogo em formato RGB
C_ORANGE = (255, 128, 0)
C_GREEN = (0, 128, 0)
C_BLUE = (0, 0, 255)
C_RED = (255, 0, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_CYAN = (0, 128, 128)
C_BLACK = (0, 0, 0)

# E
# Define eventos customizados do Pygame
EVENT_ENEMY = pygame.USEREVENT + 1  # Evento para spawn de inimigos
EVENT_TIMEOUT = pygame.USEREVENT + 2  # Evento de tempo limite

# Define a velocidade de cada entidade no jogo
ENTITY_SPEED = {
    'Level1Bg1': 0,  # Fundo do nível 1, camada 1 não se move
    'Level1Bg2': 1,  # Fundo do nível 1, camada 2
    'Level1Bg3': 2,
    'Level1Bg4': 3,
    'Level1Bg5': 4,
    'Level1Bg6': 5,
    'Level1Bg7': 6,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Player1': 3,  # Velocidade do Player1
    'Player1Shot': 3,  # Velocidade do tiro do Player1
    'Player2': 1,
    'Player2Shot': 3,
    'Enemy1': 1,
    'Enemy1Shot': 3,
    'Enemy2': 1,
    'Enemy2Shot': 2
}

# Define a vida (health) de cada entidade
ENTITY_HEALTH = {
    'Level1Bg1': 999,  # Fundos são praticamente indestrutíveis
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level1Bg7': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Player1': 150,  # Vida do Player1
    'Player1Shot': 1,  # Tiro tem 1 de vida
    'Player2': 150,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1
}

# Define o dano que cada entidade causa
ENTITY_DAMAGE = {
    'Level1Bg1': 0,  # Fundos não causam dano
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level1Bg7': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Player1': 1,  # Player1 causa 1 de dano ao colidir
    'Player1Shot': 25,  # Tiro do Player1 causa 25 de dano
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
    'Explosion': 0  # Explosões não causam dano direto
}

# Define a pontuação que cada entidade dá ao ser destruída
ENTITY_SCORE = {
    'Level1Bg1': 0,  # Fundos não dão pontos
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level1Bg7': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Player1': 0,  # Jogadores não dão pontos
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,  # Enemy1 dá 100 pontos
    'Enemy1Shot': 0,
    'Enemy2': 120,  # Enemy2 dá 120 pontos
    'Enemy2Shot': 0,
    'Explosion': 0,
}

# Define o delay entre tiros de cada entidade
ENTITY_SHOT_DELAY = {
    'Player1': 10,  # Delay entre tiros do Player1
    'Player2': 10,
    'Enemy1': 100,
    'Enemy2': 100,
}

# m
# Define opções do menu do jogo
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
# Define teclas para controle dos players
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}  # Tecla de mover para cima
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}  # Tecla de mover para baixo
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}  # Tecla de mover para esquerda
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}  # Tecla de mover para direita
PLAYER_KEY_SHOT = {'Player1': pygame.K_RCTRL,
                   'Player2': pygame.K_LCTRL}  # Tecla de atirar

# S
SPAWN_TIME = 4000  # Tempo de spawn de inimigos em ms

# Define posições para exibir o score na tela
SCORE_POS = {
    'Title': (WINDOW_WIDTH / 2, 50),  # Título do score
    'EnterName': (WINDOW_WIDTH / 2, 80),  # Prompt para digitar nome
    'Label': (WINDOW_WIDTH / 2, 90),  # Label de score
    'Name': (WINDOW_WIDTH / 2, 110),  # Nome do jogador
    0: (WINDOW_WIDTH / 2, 110),  # Pontuação da posição 0
    1: (WINDOW_WIDTH / 2, 130),
    2: (WINDOW_WIDTH / 2, 150),
    3: (WINDOW_WIDTH / 2, 170),
    4: (WINDOW_WIDTH / 2, 190),
    5: (WINDOW_WIDTH / 2, 210),
    6: (WINDOW_WIDTH / 2, 230),
}

# T
TIMEOUT_STEP = 100  # Intervalo de checagem do tempo em ms
TIMEOUT_LEVEL = 60000  # Tempo limite de um nível em ms (60s)

# W
WIN_WIDTH = 576  # Largura da janela do jogo
WIN_HEIGHT = 324  # Altura da janela do jogo