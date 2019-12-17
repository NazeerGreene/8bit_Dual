# pygame demo 0 - window only

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import pygwidgets
from CharDesign import *
import pyghelpers


# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 500
FRAMES_PER_SECOND = 30
ENEMY_MAX = 5
DEBUG = True



# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()
pygame.display.set_caption("ARE YOU READY PLAYER ONE?")

 
# 4 - Load assets: image(s), sounds,  etc.
background = pygwidgets.Image(window, (0,0), "pictures/8bit_background.jpg")
playerOne = player(window, WINDOW_WIDTH/2 + 7)
enemy = Enemy(window, WINDOW_WIDTH/2 - 130)

# 5 - Initialize variables

playerOne.setZones([1, WINDOW_WIDTH * .5], [2, WINDOW_WIDTH * .75])
enemy.setZones([1, WINDOW_WIDTH * .5], [2, WINDOW_WIDTH * .25])

blackScreen = pyghelpers.CountDownTimer(3)
timeToAnswer = pyghelpers.CountDownTimer(2)

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # If the event was a click on the close box, quit pygame and the program 
        if event.type == pygame.QUIT:        
            pygame.quit()  
            sys.exit()



     # 8 - Do any "per frame" actions
    
        
    # 9 - Clear the screen
    
    # 10 - Draw all screen elements
    background.draw()
    eneny.draw()
    playerOne.draw()
    
    
    # 11 - Update the screen
    pygame.display.update()
    
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount




