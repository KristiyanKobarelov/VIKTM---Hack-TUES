from constants import *
pygame.init()

SKY_COLOR_CUTSCENE1 = (191, 250, 255)

sky_surf = pygame.Surface((WIDTH, HEIGHT))
sky_surf.fill(SKY_COLOR_CUTSCENE1)

water_serf = pygame.Surface((WIDTH, 100))
water_serf.fill(BACKGROUND_COLOR)


def draw_cutscene1(window):
    while player_rect.top < HEIGHT + 100:
        window.blit(sky_surf, (0, 0))
        window.blit(water_serf, (0, HEIGHT - 100))

        pygame.display.update()


if __name__ == '__main__':
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    draw_cutscene1(WINDOW)
