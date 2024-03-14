import pygame

from constants import *

player_surf = pygame.Surface((100, 40))
player_rect = player_surf.get_rect(center=(WIDTH/2, HEIGHT/2))
player_surf.fill('green')

background_surf = pygame.Surface((WIDTH, HEIGHT))
background_surf.fill(BACKGROUND_COLOR)


def draw(window):
    # Draw everything on screen
    window.blit(background_surf, (0, 0))
    window.blit(player_surf, player_rect)
    pygame.display.update()
