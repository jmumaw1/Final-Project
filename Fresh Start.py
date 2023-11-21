import pygame
import sys
import math
from Parameters import *
from Player import *
from PROJECTILES import *

pygame.init()

# Timer properties
timer_value = TIMER_START * FPS  # Convert seconds to frames
font = pygame.font.Font(None, 36)

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity, Movement, Jumping, Timer, and Shooting in Pygame")
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            angle = math.atan2(mouse_y - player_y, mouse_x - player_x)

            if event.button == 1:  # Left mouse button
                projectiles.append(Projectile(player_x, player_y, angle, RED))
            elif event.button == 3:  # Right mouse button
                projectiles.append(Projectile(player_x, player_y, angle, GREEN))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping and player_y == HEIGHT - player_size:  # Jump if on the ground
        player_speed_y = -JUMP_HEIGHT
        is_jumping = True

    # Apply gravity
    player_speed_y += GRAVITY
    player_y += player_speed_y

    # Check if player is on the ground
    if player_y >= HEIGHT - player_size:
        player_y = HEIGHT - player_size
        is_jumping = False

    # Move player horizontally
    if keys[pygame.K_a]:
        player_x -= PLAYER_SPEED_X
    if keys[pygame.K_d]:
        player_x += PLAYER_SPEED_X

    # Keep player within screen bounds horizontally
    player_x = min(max(player_x, 0), WIDTH - player_size)

    # Update the timer
    timer_value -= 1

    # Move projectiles
    for projectile in projectiles:
        projectile.move()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.rect(screen, BLUE, (player_x, int(player_y), player_size, player_size))

    # Draw the timer in the top right corner
    timer_text = font.render(str(timer_value // FPS), True, BLACK)
    screen.blit(timer_text, (WIDTH - 50, 10))

    # Draw projectiles
    for projectile in projectiles:
        pygame.draw.circle(screen, projectile.color, (int(projectile.x), int(projectile.y)), 5)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
