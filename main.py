import pygame.mouse

from draw_function import *
from collision import *
from camera_movement import *
from cutscene1 import *
from sys import exit

pygame.init()

pygame.display.set_caption('Secrets of The Deep')

clock = pygame.time.Clock()

start_time = 0


def main_gameplay():
    fish_timer = 0
    player_health = 7
    add_fish = 500
    game_active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if game_active:
            fish_timer += clock.tick(FPS)

            if game_active:
                if fish_timer > add_fish:
                    fish_generator()

                    fish_timer = 0

            fish_movement()

            player_movement()

            player_health = detect_collision(player_health)

            draw(WINDOW, player_health)

        else:
            draw_cutscene1(WINDOW)
            game_active = start_screen(WINDOW)


if __name__ == '__main__':
    main_gameplay()
