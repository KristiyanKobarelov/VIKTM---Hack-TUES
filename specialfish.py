import pygame
import random
from constants import *

def special_fish_generator():
    specialty = random.randint(100,100)
    if specialty == 100:
        fish_y = random.randint(0, 4*HEIGHT)

        side = random.randint(1, 2)
        # 1 is left, 2 is right

        if side == 1:
            fish_x = random.randint(-100, 0)
            size = random.uniform(1,2)
            fish = pygame.Rect(fish_x, fish_y, FISH_WIDTH * size, FISH_HEIGHT * size)
            special_fish_left.append(fish)


        else:
            fish_x = random.randint(WIDTH, WIDTH+100)
            size = random.uniform(1,2)
            fish = pygame.Rect(fish_x, fish_y, FISH_WIDTH * size, FISH_HEIGHT * size)
            special_fish_right.append(fish)
    
def special_fish_movement():
    for fish in special_fish_left:
        fish.x += FISH_VEL
        if fish.x > WIDTH:
            special_fish_left.remove(fish)
    for fish in special_fish_right:
        fish.x -= FISH_VEL
        if fish.x < -100:
            special_fish_right.remove(fish)