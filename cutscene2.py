from constants import *
pygame.init()

clock3 = pygame.time.Clock()

background_surf = pygame.image.load('Background/Underwater BG Blank.png').convert_alpha()
background_surf = pygame.transform.rotozoom(background_surf, 0, 0.8)

player_surf = pygame.image.load('Player/vodolaz1.webp').convert_alpha()
player_surf = pygame.transform.rotozoom(player_surf, 0, 0.8)
player_surf_diving = pygame.image.load('Player/diver.webp').convert_alpha()
player_surf_diving = pygame.transform.rotozoom(player_surf_diving, 0, 0.8)


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
        if player_y < HEIGHT/4:
            window.blit(pygame.transform.flip(player_surf, 0, 1),
                        (WIDTH/2 - PLAYER_WIDTH/2, player_y - PLAYER_SPEED/2))
        else:
            window.blit(player_surf_diving, (WIDTH/2 - PLAYER_WIDTH/2, player_y - PLAYER_SPEED/2))
        window.blit(Golden_fish_surf, (WIDTH/2 - GOLDEN_FISH_WIDTH/2 - 30, HEIGHT / 2 + golden_fish_y))

        if golden_fish_y >= HEIGHT + 100:
            break

        pygame.display.update()
