import pygame
from sys import exit

from constants import *
from draw_function import *
from fish import *

pygame.init()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Secrets of the deep')

clock = pygame.time.Clock()


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        fish_generator(5)
        fish_movement()

        draw(WINDOW)
        clock.tick(FPS)


if __name__ == '__main__':
    main()
