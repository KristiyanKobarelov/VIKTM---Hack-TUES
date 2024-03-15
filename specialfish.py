import pygame
import random
from constants import *
import math


def special_fish_generator():
    fish_y = random.randint(0, 4*HEIGHT)

    side = random.randint(1, 2)
    # 1 is left, 2 is right

    if side == 1:
        fish_x = random.randint(-100, 0)
        size = random.uniform(1,2)
        fish = pygame.Rect(fish_x, fish_y, FISH_WIDTH * size, FISH_HEIGHT * size)
        special_fish_left.append(fish)

<<<<<<< Updated upstream

    else:
        fish_x = random.randint(WIDTH, WIDTH+100)
        size = random.uniform(1,2)
        fish = pygame.Rect(fish_x, fish_y, FISH_WIDTH * size, FISH_HEIGHT * size)
        special_fish_right.append(fish)
    
=======
        else:
            fish_x = random.randint(WIDTH, WIDTH+100)
            size = random.uniform(1,2)
            fish = pygame.Rect(fish_x, fish_y, FISH_WIDTH * size, FISH_HEIGHT * size)
            special_fish_right.append(fish)


>>>>>>> Stashed changes
def special_fish_movement():
    for fish in special_fish_left:
        if calculate_radius(fish):
            if fish.x > WIDTH / 2:
                fish.x += 1
            else:
                fish.x -= 1

            if fish.y > HEIGHT / 2:
                fish.y += 1
            else:
                fish.y -= 1
        fish.x += FISH_VEL
        if fish.x > WIDTH:
            special_fish_left.remove(fish)
    for fish in special_fish_right:
        if calculate_radius(fish):
            if fish.x > WIDTH / 2:
                fish.x += 1
            else:
                fish.x -= 1

            if fish.y > HEIGHT / 2:
                fish.y += 1
            else:
                fish.y -= 1
        fish.x += FISH_VEL
        fish.x -= FISH_VEL
        if fish.x < -100:
            special_fish_right.remove(fish)

def calculate_radius(special_fish):
    x = abs(special_fish.x - WIDTH/2)
    y = abs(special_fish.y - HEIGHT/2)
    r = math.sqrt(x*x + y*y)
    if r <= HOSTILE_RADIUS:
        return True
    else:
        return False