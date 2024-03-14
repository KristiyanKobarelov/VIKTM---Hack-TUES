import pygame
from constants import *

pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Secrets of the deep')

player_surf = pygame.Surface((100, 40))
player_rect = player_surf.get_rect(center=(WIDTH/2, HEIGHT/2))
player_surf.fill('red')

background_surf = pygame.Surface((WIDTH, HEIGHT))
background_surf.fill(BACKGROUND_COLOR)


def draw(window):
    # Draw everything on screen
    WINDOW.blit(player_surf, player_rect)
    pygame.display.update()
