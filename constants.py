import pygame

WIDTH, HEIGHT = 800, 400

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND_COLOR = (96, 126, 181)

FPS = 60

PLAYER_SPEED = 3

FISH_HEIGHT = 20
FISH_WIDTH = 40
FISH_VEL = 4

fishes_right = []
fishes_left = []

HOSTILE_HEIGHT = 40
HOSTILE_WIDTH = 80
HOSTILE_VEL = 2
HOSTILE_RADIUS = 250

hostile_fishes_right = []
hostile_fishes_left = []

rainbow_fish = []

BOAT_VEL = 7

player_surf = pygame.Surface((100, 40))
player_rect = player_surf.get_rect(center=(WIDTH/2, HEIGHT/2))
