import pygame
from fish import *
from constants import *

def detect_collision():
    for fish in fishes_left:
        if player_rect.colliderect(fish):
            player_heatlh -= 20
            if(player_health == 0):
                exit()
    
    for fish in fishes_right:
        if player_rect.colliderect(fish):
            player_heatlh -= 20
            if(player_health == 0):
                exit()

