from constants import *


def unspecial_fish_movement():
    for fish in unspecial_fish_left:
        fish.x += FISH_VEL
        if fish.x > WIDTH:
            fishes_left.remove(fish)
    for fish in unspecial_fish_right:
        fish.x -= FISH_VEL
        if fish.x < -100:
            fishes_right.remove(fish)
