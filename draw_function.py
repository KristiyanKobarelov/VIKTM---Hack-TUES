from fish import *

player_surf.fill('green')

background_surf = pygame.Surface((WIDTH, HEIGHT))
background_surf.fill(BACKGROUND_COLOR)


def draw(window):
    # Draw everything on screen
    window.blit(background_surf, (0, 0))
    window.blit(player_surf, player_rect)
    for fish in fishes_left:
        window.blit(fish_surf, (fish.x, fish.y))
    for fish in fishes_right:
        window.blit(fish_surf, (fish.x, fish.y))
    pygame.display.update()
