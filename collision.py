import pygame
from fish import *
from constants import *

def detect_collision(player_rect, fish_rect):
    if player_rect.colliderect(fish_rect):
        pygame.quit()
        exit()