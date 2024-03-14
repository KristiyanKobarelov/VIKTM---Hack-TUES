import pygame

WIDTH, HEIGHT = 800, 400

BACKGROUND_COLOR = (159, 252, 253)

FPS = 60

FISH_HEIGHT = 20
FISH_WIDTH = 40
FISH_VEL = 4

fishes_right = []
fishes_left = []

player_surf = pygame.Surface((100, 40))
player_rect = player_surf.get_rect(center=(WIDTH/2, HEIGHT/2))

game_active = False
start_time = 0
