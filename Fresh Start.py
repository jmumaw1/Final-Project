import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5
PLAYER_SPEED_X = 5
JUMP_HEIGHT = 12
TIMER_START = 99  # Starting time in seconds

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Player properties
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT // 2 - player_size // 2
player_speed_y = 0
is_jumping = False

# Timer properties
timer_value = TIMER_START * FPS  # Convert seconds to frames
font = pygame.font.Font(None, 36)

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity, Movement, Jumping, and Timer in Pygame")
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

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
    if keys[pygame.K_LEFT]:
        player_x -= PLAYER_SPEED_X
    if keys[pygame.K_RIGHT]:
        player_x += PLAYER_SPEED_X

    # Keep player within screen bounds horizontally
    player_x = min(max(player_x, 0), WIDTH - player_size)

    # Update the timer
    timer_value -= 1

    # Clear the screen
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.rect(screen, BLUE, (player_x, int(player_y), player_size, player_size))

    # Draw the timer in the top right corner
    timer_text = font.render(str(timer_value // FPS), True, BLACK)
    screen.blit(timer_text, (WIDTH - 50, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
