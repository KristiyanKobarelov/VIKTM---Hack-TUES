import pygame

WIDTH, HEIGHT = 800, 400

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND_COLOR = (113, 196, 237)

FPS = 60

PLAYER_SPEED = 3

FISH_HEIGHT = 20
FISH_WIDTH = 40
FISH_VEL = 4

fishes_right = []
fishes_left = []
rainbow_fish = []

BOAT_VEL = 7

game_active = False

player_surf = pygame.Surface((100, 40))
player_rect = player_surf.get_rect(center=(WIDTH/2, HEIGHT/2))


