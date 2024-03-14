import pygame
import random
import time

FISH_HEIGHT = 20
FISH_WIDTH = 40

fishes = []

def fish_generator():
        number = random.randint(1,10)
        if(number < 5):
            side = random.randint(1,2)
            #1 is left, 2 is right
        fish_y = random.randint(100, HEIGHT)
        if side == 1:
            fish_x = random.randint(WIDTH - 100, WIDTH/2)
            FISH_VEL = 6

        else:
            fish_x = random.randint(WIDTH/2, WIDTH + 100)
            FISH_VEL = -6
        fish = pygame.Rect(fish_x, fish_y, FISH_WIDTH, FISH_HEIGHT)

        fishes.append(fish)