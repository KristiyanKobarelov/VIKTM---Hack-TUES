import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Secrets of the deep')

clock = pygame.time.Clock()

background_surf = pygame.Surface((800, 400))
background_surf.fill((159, 252, 253))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surf, (0, 0))

    pygame.display.update()
    clock.tick(60)
