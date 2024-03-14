import pygame
from sys import exit

from constants import *
from draw_function import *

pygame.init()
WINDOW = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption('Secrets of the deep')

clock = pygame.time.Clock()

background_surf = pygame.Surface(WIDTH, HEIGHT)
background_surf.fill(BACKGROUND_COLOR)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()



        draw(WINDOW)
        clock.tick(FPS)
