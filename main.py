from sys import exit

from draw_function import *

clock = pygame.time.Clock()


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        draw(WINDOW)
        clock.tick(FPS)
