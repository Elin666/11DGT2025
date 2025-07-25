import pygame
import time
import random

#Set up the display (I need to specify width and height)
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Sun Chaser")

def main(): #define the functicon 
    run = True
# The window need loops through each event in the list
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
                    # Call the function to start the game
                    break
    # A list of all pending events(eg. keyboared presses, mouse clicks, window close actions)
    # The programe it's not automatic
    # Without this, game wouldn't respond to user input or window controls
        screen.fill((255,255,255)) 
        #Fill the background color
        pygame.display.flip()
        #update the display
    pygame.quit()

if __name__ == "__main__":
    main() # run the code inside 'def main()'