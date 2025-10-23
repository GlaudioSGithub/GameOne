# C
from pickle import EMPTY_TUPLE

import pygame
from pygame.examples.grid import WINDOW_WIDTH

C_ORANGE = (255, 128, 0)
C_GREEN = (0, 128, 0)
C_BLUE = (0, 0, 255)
C_RED = (255, 0, 0)
C_YELLOW = (255, 255, 128)
C_WHITE = (255, 255, 255)
C_CYAN = (0, 128, 128)
C_BLACK = (0, 0, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg1': 0,
    'Level1Bg2': 1,
    'Level1Bg3': 2,
    'Level1Bg4': 3,
    'Level1Bg5': 4,
    'Level1Bg6': 5,
    'Level1Bg7': 6,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Player1': 3,
    'Player1Shot': 3,
    'Player2': 1,
    'Player2Shot': 3,
    'Enemy1': 1,
    'Enemy1Shot': 3,
    'Enemy2': 1,
    'Enemy2Shot': 2
}

ENTITY_HEALTH = {
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level1Bg7': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Player1': 150,
    'Player1Shot': 1,
    'Player2': 150,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1
}

ENTITY_DAMAGE = {
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level1Bg7': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Player1': 1,  # Player1 have damage 1
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15
}

ENTITY_SCORE = {
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level1Bg7': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 120,
    'Enemy2Shot': 0
}

ENTITY_SHOT_DELAY = {
    'Player1': 10,
    'Player2': 10,
    'Enemy1': 100,
    'Enemy2': 100,
}

# m
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                 'Player2': pygame.K_d}
PLAYER_KEY_SHOT = {'Player1': pygame.K_RCTRL,
                 'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000
SCORE_POS = {
    'Title': (WINDOW_WIDTH / 2, 50),
    'EnterName': (WINDOW_WIDTH / 2, 80),
    'Label': (WINDOW_WIDTH / 2, 90),
    'Name': (WINDOW_WIDTH / 2, 110),
    0: (WINDOW_WIDTH / 2, 110),
    1: (WINDOW_WIDTH / 2, 130),
    2: (WINDOW_WIDTH / 2, 150),
    3: (WINDOW_WIDTH / 2, 170),
    4: (WINDOW_WIDTH / 2, 190),
    5: (WINDOW_WIDTH / 2, 210),
    6: (WINDOW_WIDTH / 2, 230),
}

# T
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 20000  # 20s

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324