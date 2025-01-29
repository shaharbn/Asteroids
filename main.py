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

        # refrash the screen last comand
        pygame.display.flip()



if __name__ == "__main__":
    main()