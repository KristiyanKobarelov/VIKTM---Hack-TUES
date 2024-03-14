from constants import *
import pygame
from fish import *
from random import randint
import keyboard
import Key

def move_cam():
    player_x = WIDTH // 2
    player_y = HEIGHT // 2

    while True:
        if keyboard.read_key() == 'w' or keyboard.read_key() == Key.up:
            for fish in fishes_left:
                fish.y -= PLAYER_SPEED
            for fish in fishes_right:
                fish.y -= PLAYER_SPEED

        if keyboard.read_key() == 's' or keyboard.read_key() == Key.down:
            for fish in fishes_left:
                fish.y += PLAYER_SPEED
            for fish in fishes_right:
                fish.y += PLAYER_SPEED

        if keyboard.read_key() == 'a' or keyboard.read_key() == Key.left:
            for fish in fishes_left:
                fish.x += PLAYER_SPEED
            for fish in fishes_right:
                fish.x += PLAYER_SPEED

        if keyboard.read_key() == 'd' or keyboard.read_key() == Key.right:
            for fish in fishes_left:
                fish.x -= PLAYER_SPEED
            for fish in fishes_right:
                fish.x -= PLAYER_SPEED
