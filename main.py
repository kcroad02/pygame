import pygame

# General setup

# Initialize pygame, ALWAYS INCLUDE
pygame.init()

# Define the window size
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

# Screen / Display surface
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


# By default it's true
running = True

# Make sure the window is open every frame
while running:
    # event loop, check for timers, UI interactions, keyboard, etc.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill(('red'))
    pygame.display.update()
    

    # pygame.display.flip() is part of the window
    # most of the time you don't want to do it

# Uninitialize pygame, can cause issues, make sure to include
pygame.quit()
