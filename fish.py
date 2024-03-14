import pygame
import random
import time
from constants import *

fishes = []


def fish_generator(num_fishes):
    for _ in range(num_fishes):
        fish_y = random.randint(HEIGHT, -HEIGHT//2)

        side = random.randint(1, 2)
        # 1 is left, 2 is right
        if side == 1:
            fish_x = random.randint(-100, 0)
        else:
            fish_x = random.randint(WIDTH, WIDTH+100)
        fish = pygame.Rect(fish_x, fish_y, FISH_WIDTH, FISH_HEIGHT)

        fishes.append(fish)

    return fishes
