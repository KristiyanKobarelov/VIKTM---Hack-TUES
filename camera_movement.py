import pygame
from random import randint
import keyboard
import Key

def move_cam():
    player_x = WIDTH // 2
    player_y = HEIGHT // 2

    # 1 is up, 2 is down, 3 is left, 4 is right
    direction = 0

    while True:
        if keyboard.read_key() == 'w' or keyboard.read_key() == Key.up:
            direction = 1
            break

        if keyboard.read_key() == 's' or keyboard.read_key() == Key.down:
            direction = 2
            break

        if keyboard.read_key() == 'a' or keyboard.read_key() == Key.left:
            direction = 3
            break

        if keyboard.read_key() == 'd' or keyboard.read_key() == Key.right:
            direction = 4
            break

    if direction == 1:
        