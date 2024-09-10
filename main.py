import sys
import pygame

# General setup

class Game:
    def __init__(self):

        # Initialize pygame, ALWAYS INCLUDE
        pygame.init()

        # Define the window size
        WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480

        # Screen / Display surface
        pygame.display.set_caption("Ninja Game")
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

        self.clock = pygame.time.Clock()

        # PNG is lossless, try not to use jpg
        self.img = pygame.image.load("data/images/clouds/cloud_1.png")
        self.img.set_colorkey((0, 0, 0))
        self.img_pos = [160, 260]
        self.movement = [False, False]

    def run(self):
        # Make sure the window is open every frame
        while True:

            # Blue sky
            self.screen.fill((14,219,248))

            self.img_pos[1] += self.movement[1] - self.movement[0] * 5
            self.screen.blit(self.img, self.img_pos)

            # event loop, check for timers, UI interactions, keyboard, etc.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.movement[0] = True
                    if event.key == pygame.K_s:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.movement[0] = False
                    if event.key == pygame.K_s:
                        self.movement[1] = False

            # draw the game
            pygame.display.update()
            self.clock.tick(60)

Game().run()