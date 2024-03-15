import pygame
from constants import *

def capture_fish():
    ret = 0
    mouse_pos = pygame.mouse.get_pos()
    for fish in special_fish_left:
        if fish.collidepoint(mouse_pos):
            ret = 1
        
    for fish in special_fish_right:
        if fish.collidepoint(mouse_pos):
            ret = 1
    return ret