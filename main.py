# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    #delta time berwin drawing the last game state
    time = pygame.time.Clock()
    dt = 0
    # the gui
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # game loop
    while True:
        # make the exit (X) btn on the gui working
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # step 3 Draw the game to the screen
        screen.fill("black")

        # refrash the screen last comand of step 3
        pygame.display.flip()
        #make the loop w8 for 1/60 sec and return in seconds when the last time its have been called
        dt = time.tick(60) / 1000



if __name__ == "__main__":
    main()