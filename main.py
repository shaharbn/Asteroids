import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    #delta time berwin drawing the last game state
    time = pygame.time.Clock()
    dt = 0
    # groups of objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    # the gui
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # player object
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    asteroid = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # game loop
    while True:
        # make the exit (X) btn on the gui working
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # step 1 user input
            
        # step 2 update world
        for up in updatable:
            up.update(dt)

        for aster in asteroids:
            if aster.collision(player):
                print("Game over!")
                exit()

        # step 3 Draw the game to the screen
        screen.fill("black")
        for dr in drawable:
            dr.draw(screen)

        # refrash the screen last comand of step 3
        pygame.display.flip()
        #make the loop w8 for 1/60 sec and return in seconds when the last time its have been called
        dt = time.tick(60) / 1000



if __name__ == "__main__":
    main()