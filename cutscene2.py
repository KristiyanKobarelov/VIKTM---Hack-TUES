from constants import *
pygame.init()

clock3 = pygame.time.Clock()

background_surf = pygame.Surface((WIDTH, HEIGHT))
background_surf.fill(BACKGROUND_COLOR)


def draw_cutscene2(window):
    Golden_fish_surf = pygame.image.load('Golden_fish/golden_fish.png').convert_alpha()
    Golden_fish_surf = pygame.transform.rotozoom(Golden_fish_surf, 0, 0.5)
    Golden_fish_surf = pygame.transform.rotate(Golden_fish_surf, 90)
    yes = True

    player_y = -100
    golden_fish_y = 100

    while True:
        clock3.tick(FPS)

        if player_y < HEIGHT/2:
            player_y += PLAYER_SPEED
        else:
            if yes:
                Golden_fish_surf = pygame.transform.rotate(Golden_fish_surf, 180)
                yes = False
            golden_fish_y += SPECIAL_FISH_VEL

        window.blit(background_surf, (0, 0))
        window.blit(player_surf, (WIDTH/2 - PLAYER_WIDTH/2, player_y - PLAYER_SPEED/2))
        window.blit(Golden_fish_surf, (WIDTH/2 - GOLDEN_FISH_WIDTH/2 - 30, HEIGHT / 2 + golden_fish_y))

        if golden_fish_y >= HEIGHT + 100:
            break

        pygame.display.update()
