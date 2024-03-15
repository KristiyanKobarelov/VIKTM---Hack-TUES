from constants import *
pygame.init()

clock3 = pygame.time.Clock()

Golden_Fish = pygame.Surface((GOLDEN_FISH_WIDTH, GOLDEN_FISH_HEIGHT))
background_surf = pygame.Surface((WIDTH, HEIGHT))
background_surf.fill(BACKGROUND_COLOR)


def draw_cutscene2(window):
    player_y = -100
    golden_fish_y = 100

    while True:
        clock3.tick(FPS)

        if player_y < HEIGHT/2:
            player_y += PLAYER_SPEED
        else:
            golden_fish_y += SPECIAL_FISH_VEL

        window.blit(background_surf, (0, 0))
        window.blit(player_surf, (WIDTH/2 - PLAYER_WIDTH/2, player_y - PLAYER_SPEED/2))
        window.blit(Golden_Fish, (WIDTH/2 - GOLDEN_FISH_WIDTH/2, HEIGHT / 2 + golden_fish_y))

        if golden_fish_y >= HEIGHT + 100:
            break

        pygame.display.update()
