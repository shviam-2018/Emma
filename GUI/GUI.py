import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Emma")

# Loading assets
emma_image = pygame.image.load("assets/Emma(idol).png")

# Get the rect of the image to get its width and height
emma_rect = emma_image.get_rect()

# Initial position to center the image
x_pos = (screen_width - emma_rect.width) // 2
y_pos = (screen_height - emma_rect.height) // 2

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Blit the image onto the screen
    screen.blit(emma_image, (x_pos, y_pos))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()
