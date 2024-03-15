import pygame.transform
from animations import *
from sys import exit
from hostile_fish import *

player_surf.fill('green')

background_surf = pygame.Surface((WIDTH, HEIGHT))
background_surf.fill(BACKGROUND_COLOR)

pygame.font.init()
text_font = pygame.font.Font('Font/Pixeltype.ttf', 50)
text_surf = text_font.render('Health: ', False, 'Black')

start_text = pygame.font.Font('Font/Pixeltype.ttf', 75)
start_text_surf = start_text.render('START', False, 'Black')

controls_text = pygame.font.Font('Font/Pixeltype.ttf', 75)
controls_text_surf = controls_text.render('Controls:', False, 'Black')

moving_text = pygame.font.Font('Font/Pixeltype.ttf', 75)
moving_text_surf = moving_text.render('Moving - WASD or Arrow keys', False, 'Black')

photo_text = pygame.font.Font('Font/Pixeltype.ttf', 65)
photo_text_surf = photo_text.render('Taking photos - Left Mouse Button Click', False, 'Black')

cntrbutoton_text = pygame.font.Font('Font/Pixeltype.ttf', 65)
cntrbutton_text_surf = cntrbutoton_text.render('Controls', False, 'Black')

quitbutton_text = pygame.font.Font('Font/Pixeltype.ttf', 75)
quitbutton_text_surf = quitbutton_text.render('Quit', False, 'Black')

backbutton_text = pygame.font.Font('Font/Pixeltype.ttf', 75)
backbutton_text_surf = backbutton_text.render('Back', False, 'Black')

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

    for fish in fishes_left:
        fish_surf = pygame.Surface((fish.width, fish.height))
        window.blit(fish_surf, (fish.x, fish.y))
    for fish in fishes_right:
        fish_surf = pygame.Surface((fish.width, fish.height))
        window.blit(fish_surf, (fish.x, fish.y))

    for hostile_fish in hostile_fishes_left:
        hostile_fish_surf = shark_animations()
        window.blit(hostile_fish_surf, (hostile_fish.x, hostile_fish.y))
    for hostile_fish in hostile_fishes_right:
        hostile_fish_surf = shark_animations()
        hostile_fish_surf = pygame.transform.flip(hostile_fish_surf, 1, 0)
        window.blit(hostile_fish_surf, (hostile_fish.x, hostile_fish.y))

    for fish in special_fish_left:
        fish_surf = medusa_animations()
        window.blit(fish_surf, (fish.x, fish.y))
    for fish in special_fish_right:
        fish_surf = medusa_animations()
        window.blit(fish_surf, (fish.x, fish.y))

    cursor_rect = new_cursor.get_rect(center=pygame.mouse.get_pos())
    WINDOW.blit(new_cursor, cursor_rect)

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
    start_surf = pygame.Surface((200, 60))

    control_surf = pygame.Surface((200, 65))
    control_rect = control_surf.get_rect(topleft=(WIDTH / 2 - 200 / 2, HEIGHT - 240))
    control_surf.fill('white')

    quit_surf = pygame.Surface((200, 65))
    quit_rect = quit_surf.get_rect(topleft=(WIDTH / 2 - 200 / 2, HEIGHT - 130))
    quit_surf.fill('white')

    start_surf.fill('white')
    start_rect = start_surf.get_rect(topleft=(WIDTH / 2 - 200 / 2, HEIGHT - 340))

    start_screen_surf = pygame.Surface((WIDTH, HEIGHT))
    start_screen_surf.fill(BACKGROUND_COLOR)

    window.blit(start_screen_surf, (0, 0))
    window.blit(start_surf, start_rect)
    window.blit(control_surf, control_rect)
    window.blit(quit_surf, quit_rect)

    start_text_rect = start_text_surf.get_rect(topleft=(WIDTH / 2 - 65, HEIGHT - 327))

    window.blit(start_text_surf, start_text_rect)

    quitbutton_text_rect = quitbutton_text_surf.get_rect(topleft=(WIDTH/2 - 42, HEIGHT - 115))
    window.blit(quitbutton_text_surf,quitbutton_text_rect)

    cntrbutoton_text_rect = cntrbutton_text_surf.get_rect(topleft=(WIDTH/2 - 82, HEIGHT - 225))
    window.blit(cntrbutton_text_surf, cntrbutoton_text_rect)

    cursor_rect = new_cursor.get_rect(center=pygame.mouse.get_pos())
    window.blit(new_cursor, cursor_rect)

    pygame.display.update()

    ret = 0

    mouse_pos = pygame.mouse.get_pos()
    if start_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            ret = 1

    if control_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            ret = 2

    if quit_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            pygame.quit()
            exit()

    return ret


def controls_menu(window):
    window.blit(background_surf, (0, 0))

    controls_text_rect = controls_text_surf.get_rect(center=(WIDTH/2, HEIGHT - 350))
    window.blit(controls_text_surf, controls_text_rect)

    moving_text_rect = moving_text_surf.get_rect(center=(WIDTH/2, HEIGHT - 250))
    window.blit(moving_text_surf, moving_text_rect)

    photo_text_rect = photo_text_surf.get_rect(center = (WIDTH / 2, HEIGHT - 180))
    window.blit(photo_text_surf, photo_text_rect)

    back_surf = pygame.Surface((200, 65))
    back_rect = back_surf.get_rect(topleft=(WIDTH / 2 - 200 / 2, HEIGHT - 120))
    back_surf.fill('white')
    window.blit(back_surf, back_rect)

    backbutton_text_rect = backbutton_text_surf.get_rect(center = (WIDTH / 2, HEIGHT - 85))
    window.blit(backbutton_text_surf, backbutton_text_rect)

    ret = 0
    mouse_pos = pygame.mouse.get_pos()
    if back_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            pass

    pygame.display.update()

    return ret
