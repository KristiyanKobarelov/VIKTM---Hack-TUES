from draw_function import *


def player_movement():
    player_x = WIDTH // 2
    player_y = HEIGHT // 2
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        for fish in fishes_left:
            fish.y += PLAYER_SPEED
        for fish in fishes_right:
            fish.y += PLAYER_SPEED

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        for fish in fishes_left:
            fish.y -= PLAYER_SPEED
        for fish in fishes_right:
            fish.y -= PLAYER_SPEED

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        for fish in fishes_left:
            fish.x += PLAYER_SPEED
        for fish in fishes_right:
            fish.x += PLAYER_SPEED

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        for fish in fishes_left:
            fish.x -= PLAYER_SPEED
        for fish in fishes_right:
            fish.x -= PLAYER_SPEED
