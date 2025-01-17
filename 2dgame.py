import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions and setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Circle Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Player settings
player_pos = [WIDTH // 2, HEIGHT // 2]
player_radius = 30
player_speed = 5

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    dx, dy = mouse_x - player_pos[0], mouse_y - player_pos[1]
    angle = math.atan2(dy, dx)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keyboard input for movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # Move forward
        player_pos[0] += player_speed * math.cos(angle)
        player_pos[1] += player_speed * math.sin(angle)
    if keys[pygame.K_a]:  # Move left
        player_pos[0] -= player_speed
    if keys[pygame.K_d]:  # Move right
        player_pos[0] += player_speed

    # Draw player body (circle)
    pygame.draw.circle(screen, BLUE, (int(player_pos[0]), int(player_pos[1])), player_radius)

    # Calculate eye positions
    eye_distance = 10
    eye_offset = 10
    left_eye_x = player_pos[0] + eye_distance * math.cos(angle) - eye_offset * math.sin(angle)
    left_eye_y = player_pos[1] + eye_distance * math.sin(angle) + eye_offset * math.cos(angle)
    right_eye_x = player_pos[0] + eye_distance * math.cos(angle) + eye_offset * math.sin(angle)
    right_eye_y = player_pos[1] + eye_distance * math.sin(angle) - eye_offset * math.cos(angle)

    # Draw eyes
    pygame.draw.circle(screen, BLACK, (int(left_eye_x), int(left_eye_y)), 5)
    pygame.draw.circle(screen, BLACK, (int(right_eye_x), int(right_eye_y)), 5)

    # Update display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
