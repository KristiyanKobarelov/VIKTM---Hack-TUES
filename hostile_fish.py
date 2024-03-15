import random
import math
import time
from constants import *

player_x = WIDTH // 2
player_y = HEIGHT // 2


def hostile_fish_generator():
    for i in range(0, 3):
        hostile_fish_y = random.randint(0, 4*HEIGHT)

        side = random.randint(1, 2)
        # 1 is left, 2 is right

        if side == 1:
            hostile_fish_x = random.randint(-100, 0)
            size = random.uniform(1, 2)
            hostile_fish = pygame.Rect(hostile_fish_x, hostile_fish_y, HOSTILE_WIDTH * size, HOSTILE_HEIGHT * size)
            hostile_fishes_left.append(hostile_fish)

        else:
            hostile_fish_x = random.randint(WIDTH, WIDTH + 100)
            size = random.uniform(1, 2)
            hostile_fish = pygame.Rect(hostile_fish_x, hostile_fish_y, HOSTILE_WIDTH * size, HOSTILE_HEIGHT * size)
            hostile_fishes_right.append(hostile_fish)


def calculate_radius(hostile_fish):
    x = abs(hostile_fish.x - WIDTH/2)
    y = abs(hostile_fish.y - HEIGHT/2)
    r = math.sqrt(x*x + y*y)
    if r <= HOSTILE_RADIUS:
        return True
    else:
        return False


def hostile_fish_movement():
    for hostile_fish in hostile_fishes_left:
        if calculate_radius(hostile_fish):
            if hostile_fish.x > WIDTH / 2:
                hostile_fish.x -= 1
            else:
                hostile_fish.x += 1

            if hostile_fish.y > HEIGHT / 2:
                hostile_fish.y -= 1
            else:
                hostile_fish.y += 1
        else:
            hostile_fish.x += HOSTILE_VEL
            if hostile_fish.x > WIDTH + 100:
                hostile_fishes_left.remove(hostile_fish)
            elif hostile_fish.y < -100 or hostile_fish.y > HEIGHT + 100:
                hostile_fishes_left.remove(hostile_fish)

        if hostile_fish.x >= WIDTH//2:
            hostile_fishes_right.append(hostile_fish)
            hostile_fishes_left.remove(hostile_fish)

    for hostile_fish in hostile_fishes_right:
        if calculate_radius(hostile_fish):
            if hostile_fish.x > WIDTH/2:
                hostile_fish.x -= 1
            else:
                hostile_fish.x += 1

            if hostile_fish.y > HEIGHT/2:
                hostile_fish.y -= 1
            else:
                hostile_fish.y += 1
        else:
            hostile_fish.x -= HOSTILE_VEL
            if hostile_fish.x < -100:
                hostile_fishes_right.remove(hostile_fish)
            elif hostile_fish.y < -100 or hostile_fish.y > HEIGHT + 100:
                hostile_fishes_right.remove(hostile_fish)

        if hostile_fish.x <= WIDTH//2:
            hostile_fishes_left.append(hostile_fish)
            hostile_fishes_right.remove(hostile_fish)
