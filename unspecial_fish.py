from constants import *
from specialfish import *

def unspecial_fish_movement():
    for fish in unspecial_fish_left:
            if calculate_radius_special_fish(fish):
                if fish.x > WIDTH / 2:
                    fish.x += 7
                else:
                    fish.x -= 7

                if fish.y > HEIGHT / 2:
                    fish.y += 5
                else:
                    fish.y -= 5
            fish.x += SPECIAL_FISH_VEL
            if fish.x > WIDTH:
                unspecial_fish_left.remove(fish)
    for fish in unspecial_fish_right:
        if calculate_radius_special_fish(fish):
            if fish.x > WIDTH / 2:
                fish.x += 7
            else:
                fish.x -= 7

            if fish.y > HEIGHT / 2:
                fish.y += 5
            else:
                fish.y -= 5
        fish.x += SPECIAL_FISH_VEL
        if fish.x < -100:
            unspecial_fish_right.remove(fish)
