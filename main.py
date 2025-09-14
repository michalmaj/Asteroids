# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Create new window with given width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create clock and delta time
    clock = pygame.time.Clock()
    dt = 0

    # Create a Player container for two groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # Create an object of Player and set it position to center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create a Asteroid group
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    # Create Shoot group
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    # Main game loop
    while True:
        # Check if window is closed, if so, quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill window with black color
        screen.fill((0, 0, 0), rect=None, special_flags=0)
        
        # Draw player on the screen
        for obj in drawable:
            obj.draw(screen)

        # Update player position
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over")
                sys.exit()
            
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.kill()

        # Constantly refresh window
        pygame.display.flip()

        # Limit framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
