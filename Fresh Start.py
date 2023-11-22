import pygame
import sys
import math
from Parameters import *
from Player import *
from PROJECTILES import *
from Background import *

pygame.init()

# Timer properties
timer_value = TIMER_START * FPS  # Convert seconds to frames
font = pygame.font.Font(None, 36)

# Platform properties
platforms = [
    pygame.Rect(0, HEIGHT - 20, WIDTH, 20),
    pygame.Rect(WIDTH // 4, HEIGHT // 1.5, WIDTH // 2, 10),
    pygame.Rect(WIDTH // 2, HEIGHT // 2, WIDTH // 4, 10),
    pygame.Rect(WIDTH // 8, HEIGHT // 3, WIDTH // 4, 10)
]

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Background")
clock = pygame.time.Clock()
background = screen.copy()
draw_background(background)
player = Player(50, HEIGHT-player_size)

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

        if event.type == pygame.KEYUP:
            player.stop()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player.jump()


    # Check if player is on the ground
    if player_y >= HEIGHT - player_size:
        player_y = HEIGHT - player_size
        is_jumping = False

    # Move player horizontally
    if keys[pygame.K_a]:
        player.move_left()
    if keys[pygame.K_d]:
        player.move_right()

    player_speed_y += GRAVITY
    player_y += player_speed_y

    # Keep player within screen bounds horizontally
    player_x = min(max(player_x, 0), WIDTH - player_size)

    # Update the timer
    timer_value -= 1

    # Move projectiles
    for projectile in projectiles:
        projectile.move()

    # Checking for collision with platforms
    for platform in platforms:
        if pygame.Rect(player_x, player_y, player_size, player_size).colliderect(platform):
            player_speed_y = 0
            player_y = platform.y - player_size

    # Bliting the background
    screen.blit(background, (0, 0))

    # Draw the timer in the top right corner
    timer_text = font.render(str(timer_value // FPS), True, BLACK)
    screen.blit(timer_text, (WIDTH - 50, 10))

    # Draw projectiles
    for projectile in projectiles:
        pygame.draw.circle(screen, projectile.color, (int(projectile.x), int(projectile.y)), 5)

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, GRAY, platform)

    player.update()

    # draw the player
    player.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
