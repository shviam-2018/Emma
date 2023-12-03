import pygame
from pygame.locals import *
import pygame_verm

# Initialize Pygame and pygame-verm
pygame.init()
pygame_verm.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Eva: Your Personal Assistant")

# Load Eva's VERM model
eva_model = pygame_verm.load("Eva.vrm")

# Convert the VERM model to a Pygame Surface
eva_surface = pygame_verm.to_pygame_surface(eva_model)

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Fill the screen with white
    screen.fill(white)

    # Draw Eva's image
    screen.blit(eva_surface, (100, 100))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame_verm.quit()
pygame.quit()
