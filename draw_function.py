from fish import *

player_surf.fill('green')

background_surf = pygame.Surface((WIDTH, HEIGHT))
background_surf.fill(BACKGROUND_COLOR)


def draw(window):
    # Draw everything on screen
    window.blit(background_surf, (0, 0))

    window.blit(player_surf, player_rect)

    for fish in fishes_left:
        fish_surf = pygame.Surface((fish.width, fish.height))
        window.blit(fish_surf, (fish.x, fish.y))
    for fish in fishes_right:
        fish_surf = pygame.Surface((fish.width, fish.height))
        window.blit(fish_surf, (fish.x, fish.y))

    pygame.display.update()



def start_screen(window, start_surf, quit_surf):

    start_surf = pygame.Surface((START_WIDTH, START_HEIGHT))
    start_surf.fill('white')

    quit_surf = pygame.Surface((START_WIDTH, START_HEIGHT))
    quit_surf.fill('white')

    background_surf.fill('black')
    window.blit(background_surf, (0, 0))

    window.blit(start_surf, (200, 200))
    window.blit(quit_surf, (200, 500))