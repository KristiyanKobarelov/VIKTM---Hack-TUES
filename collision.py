from constants import *
from draw_function import background_surf
import math

player_x = WIDTH // 2
player_y = HEIGHT // 2

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

    for hostile_fish in hostile_fishes_left:
        angle = math.atan2(player_y - hostile_fish[1], player_x - hostile_fish[0])
        hostile_speed = 1
        hostile_fish[0] += hostile_speed * math.cos(angle)
        hostile_fish[1] += hostile_speed * math.sin(angle)

    for hostile_fish in hostile_fishes_right:
        angle = math.atan2(player_y - hostile_fish[1], player_x - hostile_fish[0])
        hostile_speed = 1
        hostile_fish[0] += hostile_speed * math.cos(angle)
        hostile_fish[1] += hostile_speed * math.sin(angle)

    for hostile_fish in hostile_fishes_left:
        if player_rect.colliderect(hostile_fish):
            player_health -= 2
            hostile_fishes_left.remove(hostile_fish)
            if player_health <= 0:
                exit()

    for hostile_fish in hostile_fishes_right:
        if player_rect.colliderect(hostile_fish):
            player_health -= 2
            hostile_fishes_right.remove(hostile_fish)
            if player_health <= 0:
                exit()

    for fish in unspecial_fish_left:
        if player_rect.colliderect(fish):
            player_health -= 1
            unspecial_fish_left.remove(fish)
            if player_health <= 0:
                exit()
    
    for fish in unspecial_fish_right:
        if player_rect.colliderect(fish):
            player_health -= 1
            unspecial_fish_right.remove(fish)
            if player_health <= 0:
                exit()
    return player_health
