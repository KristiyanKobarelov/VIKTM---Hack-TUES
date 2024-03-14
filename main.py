from draw_function import *
from fish import *
from collision import *
from camera_movement import *
from sys import exit

pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Secrets of the deep')

clock = pygame.time.Clock()

# game_active = False
# start_time = 0

def main_gameplay():
    fish_timer = 0
    player_health = 7
    add_fish = 500

    while True:
        fish_timer += clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if fish_timer > add_fish:
            # Creating 3 stars
            fish_generator(5)
            # We start counting again for the next new stars
            fish_timer = 0

        fish_movement()

        player_health = detect_collision(player_health)

        draw(WINDOW)


if __name__ == '__main__':
    main_gameplay()
