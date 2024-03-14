import pygame
from fish import *
from constants import *

def detect_collision():
    for fish in fishes_left:
        if player_rect.colliderect(fish):
            pygame.quit()
            exit()
    
    for fish in fishes_right:
        if player_rect.colliderect(fish):
            pygame.quit()
            exit()

