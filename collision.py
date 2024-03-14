import pygame
from fish import *
from constants import *
from draw_function import background_surf


def detect_collision(player_health):
    for fish in fishes_left:
        if player_rect.colliderect(fish):
            player_health -= 1
            fishes_left.remove(fish)
            if player_health <= 0:
                exit()
    
    for fish in fishes_right:
        if player_rect.colliderect(fish):
            player_health -= 1
            fishes_right.remove(fish)
            if player_health <= 0:
                exit()

    return player_health
