import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
NEAR_WHITE = (220, 220, 220)
DARK_BLUE = (0, 0, 60)
ORANGE = (255, 160, 0)
MID_ORANGE = (210, 130, 0)
DARK_ORANGE = (160, 90, 0)
RED = (255, 0, 0)
MID_RED = (190, 0, 0)
DARK_RED = (100, 0, 0)
CYAN = (0, 255, 190)
DARK_CYAN = (0, 200, 140)
GREEN = (0, 255, 0)

SCREEN_SIZE = (1200, 550)
WIDTH = SCREEN_SIZE[0]
HEIGHT = SCREEN_SIZE[1]
screen = pygame.display.set_mode(SCREEN_SIZE)

font100 = pygame.font.SysFont('OCR A EXTENDED', 100)
font65 = pygame.font.SysFont('OCR A EXTENDED', 65)
font25 = pygame.font.SysFont('OCR A EXTENDED', 25)

my_icon = pygame.image.load('dark blue.png').convert_alpha()
background = pygame.image.load('city_background_clean.png').convert_alpha()

button_sfx = pygame.mixer.Sound('vgmenuselect.wav')
