from collision import *
from camera_movement import *
from cutscene1 import *
from cutscene2 import *
from specialfish import *
from sys import exit

pygame.init()

pygame.display.set_caption('Secrets of The Deep')

clock = pygame.time.Clock()

start_time = 0


def main_gameplay():
    fish_timer = 0
    hostile_fish_timer = 0
    special_fish_timer = 0

    add_fish = 500
    add_hostile_fish = 2000
    add_special_fish = 5000

    player_health = 7

    game_active = 0
    depth_pixels = 500  # 50 pixels = 1 meter

    # draw_cutscene1(WINDOW)
    # draw_cutscene2(WINDOW)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if game_active == 1:
            h = clock.tick(FPS)
            fish_timer += h
            hostile_fish_timer += h
            special_fish_timer += h

            if fish_timer > add_fish:
                fish_generator()
                fish_timer = 0

            if hostile_fish_timer > add_hostile_fish:
                hostile_fish_generator()
                hostile_fish_timer = 0

            if special_fish_timer > add_special_fish:
                special_fish_generator()
                special_fish_timer = 0

            fish_movement()
            hostile_fish_movement()
            special_fish_movement()

            depth_pixels = player_movement(depth_pixels)

            player_health = detect_collision(player_health)

            draw(WINDOW, player_health)

        elif game_active == 0:
            game_active = start_screen(WINDOW)

        elif game_active == 2:
            game_active = controls_menu(WINDOW)


if __name__ == '__main__':
    main_gameplay()
