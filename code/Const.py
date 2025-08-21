
import pygame

# C

BLACK = (0,0,0)         #000000
WHITE = (255,255,255)   #FFFFFF
BLUE = (35,12,230)      #200CE6
YELLOW = (255,252,43)   #FFFC2B
GREEN = (13,255,12)     #0DFF0C
RED = (255,46,12)       #FF2E0C
BROWN = (128,45,16)     #802D10
C_1 = (79,199,137)      #4FC789
C_2 = (73,131,199)      #4983C7

# E

EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'BG0': 2,
    'BG1': 3,
    'BG2': 4,
    'BG3': 5,
    'BG4': 6,
    'Player': 3,
    'EnemyH1': 2,
    'EnemyH2': 1,
}

#H
ENTITY_HEALTH = {
    'BG0': 777,
    'BG1': 777,
    'BG2': 777,
    'BG3': 777,
    'BG4': 777,
    'Player': 300,
    'EnemyH1': 50,
    'EnemyH2': 50,
}

#M
MENU_OPTION = ('NEW GAME - EASY MODE',
               'NEW GAME - HARD MODE',
               'NEW GAME - HARD AND TOUGH MODE',
               'ABOUT THE GAME AND SCORE',
               'EXIT')

# W
WIN_WIDTH = 860
WIN_HEIGHT = 630