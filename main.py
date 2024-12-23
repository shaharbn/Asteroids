import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from shot import *

def main():
    pygame.init()
    #responsible for the GUI
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    #contain the delta time -> the time from the last frame draw
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    astroid_field = AsteroidField()

    while True:
        #Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #Logic Updates
        for update in updatable:
            update.update(dt)

        for asteroid in asteroids:
            if player.collisions(asteroid):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collisions(asteroid):
                    shot.kill()
                    asteroid.split()

        #Rendering
        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()

        # Time Management
        dt = time.tick(60) / 1000

if __name__ == "__main__":
    main()