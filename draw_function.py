from constants import *

player_surf.fill('red')

background_surf = pygame.Surface((WIDTH, HEIGHT))
background_surf.fill(BACKGROUND_COLOR)


def draw(window):
    # Draw everything on screen
    window.blit(background_surf, (0, 0))
    window.blit(player_surf, player_rect)
    pygame.display.update()
