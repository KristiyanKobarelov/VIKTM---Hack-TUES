import random
import time
from constants import *


def fish_generator(num_fishes):
    fish_y = random.randint(-HEIGHT//2, HEIGHT)

    side = random.randint(1, 2)
    # 1 is left, 2 is right

    if side == 1:
        fish_x = random.randint(-100, 0)
        fish = pygame.Rect(fish_x, fish_y, FISH_WIDTH, FISH_HEIGHT)
        fishes_left.append(fish)

    else:
        fish_x = random.randint(WIDTH, WIDTH+100)
        fish = pygame.Rect(fish_x, fish_y, FISH_WIDTH, FISH_HEIGHT)
        fishes_right.append(fish)


def fish_movement():
    for fish in fishes_left:
        fish.x += FISH_VEL
        if fish.x > WIDTH:
            fishes_left.remove(fish)
    for fish in fishes_right:
        fish.x -= FISH_VEL
        if fish.x < -100:
            fishes_right.remove(fish)
