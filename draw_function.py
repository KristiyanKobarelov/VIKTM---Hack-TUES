import pygame.transform

from fish import *

player_surf.fill('green')

background_surf = pygame.Surface((WIDTH, HEIGHT))
background_surf.fill(BACKGROUND_COLOR)

pygame.font.init()
text_font = pygame.font.Font('Font/Pixeltype.ttf', 50)
text_surf = text_font.render('Health: ', False, 'Black')

start_font = pygame.font.Font('Font/Pixeltype.ttf', 50)
start_font_surf = start_font.render('Start', False, 'Blue')

max_heart_surf = pygame.image.load('Hearts/7 hearts.png').convert_alpha()
max_heart_surf = pygame.transform.rotozoom(max_heart_surf, 0, 0.3)
broken_heart_surf = pygame.image.load('Hearts/broken heart.png').convert_alpha()
broken_heart_surf = pygame.transform.rotozoom(broken_heart_surf, 0, 0.3)

new_cursor = pygame.image.load('Cursor/noun-viewfinder-92699.png').convert_alpha()
new_cursor = pygame.transform.rotozoom(new_cursor, 0, 0.1)
pygame.mouse.set_visible(False)


def draw(window, player_health, temp_x=0):
    # Draw everything on screen

    window.blit(background_surf, (0, 0))

    window.blit(player_surf, player_rect)

    window.blit(text_surf, (5, 5))

    cursor_rect = new_cursor.get_rect(center=pygame.mouse.get_pos())
    WINDOW.blit(new_cursor, cursor_rect)

    for fish in fishes_left:
        fish_surf = pygame.Surface((fish.width, fish.height))
        window.blit(fish_surf, (fish.x, fish.y))
    for fish in fishes_right:
        fish_surf = pygame.Surface((fish.width, fish.height))
        window.blit(fish_surf, (fish.x, fish.y))

    for i in range(player_health):
        if i == 0:
            temp_x = 90
        elif i == 1:
            temp_x = 105
        elif i == 2:
            temp_x = 120
        elif i == 3:
            temp_x = 135
        elif i == 4:
            temp_x = 150
        elif i == 5:
            temp_x = 165
        elif i == 6:
            temp_x = 180
        window.blit(max_heart_surf, (temp_x, -7))
        temp_x = 0

    if player_health < 1:
        window.blit(broken_heart_surf, (70, -45))
    if player_health < 2:
        window.blit(broken_heart_surf, (85, -45))
    if player_health < 3:
        window.blit(broken_heart_surf, (100, -45))
    if player_health < 4:
        window.blit(broken_heart_surf, (115, -45))
    if player_health < 5:
        window.blit(broken_heart_surf, (130, -45))
    if player_health < 6:
        window.blit(broken_heart_surf, (145, -45))
    if player_health < 7:
        window.blit(broken_heart_surf, (160, -45))

    pygame.display.update()


def start_screen(window):

    start_surf = pygame.Surface((200, 200))
    start_surf.fill('white')
    start_rect = start_surf.get_rect(center=(WIDTH/2, HEIGHT/2))

    start_screen_surf = pygame.Surface((WIDTH, HEIGHT))
    start_screen_surf.fill('black')

    window.blit(start_screen_surf, (0, 0))
    window.blit(start_surf, start_rect)

    window.blit(start_screen_surf, ())

    pygame.display.update()

    mouse_pos = pygame.mouse.get_pos()
    if start_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            return True
        