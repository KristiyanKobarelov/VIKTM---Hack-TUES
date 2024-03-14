import os
from constants import *
pygame.init()

background_cutscene1_surf = pygame.transform.scale(
    pygame.image.load(os.path.join('images', 'ocean_background.png')), (WIDTH, HEIGHT))

boat_serf = pygame.image.load(
    os.path.join('images', 'boat.png'))

player_cutscene_serf = pygame.Surface((40, 100))

clock2 = pygame.time.Clock()


def draw_cutscene1(window):
    boat_width = -200

    while boat_width < WIDTH//2 - 250:
        clock2.tick(FPS)

        window.blit(background_cutscene1_surf, (0, 0))

        boat_width += BOAT_VEL

        window.blit(boat_serf, (boat_width, HEIGHT - 150))
        window.blit(player_cutscene_serf, (boat_width + 70, HEIGHT - 180))

        pygame.display.update()

    player_x = boat_width + 70
    player_y = HEIGHT - 180
    up = True

    while True:
        clock2.tick(FPS)

        window.blit(background_cutscene1_surf, (0, 0))

        if player_y > HEIGHT - 250 and up:
            player_y -= 4
        else:
            up = False
            player_y += 4

        if player_x <= boat_width + 250:
            player_x += 6

        window.blit(boat_serf, (boat_width, HEIGHT - 150))
        window.blit(player_cutscene_serf, (player_x, player_y))

        pygame.display.update()

        if player_y > HEIGHT + 200:
            break
