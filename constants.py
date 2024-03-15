import pygame

WIDTH, HEIGHT = 1500, 750

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND_COLOR = (96, 126, 181)

FPS = 60

PLAYER_SPEED = 3

FISH_HEIGHT = 20
FISH_WIDTH = 40
FISH_VEL = 4

HOSTILE_HEIGHT = 40
HOSTILE_WIDTH = 80
HOSTILE_VEL = 2
HOSTILE_RADIUS = 250

SPECIAL_FISH_RADIUS = 250
SPECIAL_FISH_VEL = 7

GOLDEN_FISH_HEIGHT = 10
GOLDEN_FISH_WIDTH = 20

fishes_right = []
fishes_left = []

special_fish_right = []
special_fish_left = []

unspecial_fish_left = []
unspecial_fish_right = []

hostile_fishes_right = []
hostile_fishes_left = []

BOAT_VEL = 7

PLAYER_WIDTH = 100
PLAYER_HEIGHT = 40

player_surf = pygame.Surface((100, 40))
player_rect = player_surf.get_rect(center=(WIDTH/2, HEIGHT/2))
