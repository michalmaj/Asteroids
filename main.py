# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    # Create new window with given width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create clock and delta time
    clock = pygame.time.Clock()
    dt = 0

    # Create an object of Player and set it position to center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main game loop
    while True:
        # Check if window is closed, if so, quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill window with black color
        screen.fill((0, 0, 0), rect=None, special_flags=0)
        
        # Draw player on the screen
        player.draw(screen)

        # Constantly refresh window
        pygame.display.flip()

        # Limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
