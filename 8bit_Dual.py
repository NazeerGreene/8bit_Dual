# pygame demo 0 - window only

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import pygwidgets
from CharDesign import *
import pyghelpers
from random import randint

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 500
FRAMES_PER_SECOND = 30
DEBUG = True


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()
pygame.display.set_caption("ARE YOU READY PLAYER ONE?")

 
# 4 - Load assets: image(s), sounds,  etc.
background = pygwidgets.Image(window, (0,0), "pictures/8bit_background.jpg")
player = player(window, WINDOW_WIDTH/2 + 7)
enemy = Enemy(window, WINDOW_WIDTH/2 - 130)

# 5 - Initialize variables
state = 2

player.setZones([ [1, WINDOW_WIDTH * .5],       #player zone 1
                     [2, WINDOW_WIDTH * .75] ]) #player zone 2
enemy.setZones([ [1, WINDOW_WIDTH * .5],        #enemy zone 1
                 [2, WINDOW_WIDTH * .25] ])     #enemy zone 2

blackScreenTimer = pyghelpers.CountDownTimer(3)
timeToAnswer = pyghelpers.CountDownTimer(2)

playerZone = 0
enemyZone = 0

userAnswer = 0
enemyGuess = 0

# 6 - Loop forever - Main Game
while True:
    
    
   
    if state == 1:           #countdown screen
        pass


    
    if state == 2:          #Time for user to answer

        playerZone = player.randomZone()
        enemyZone = enemy.randomZone()
        
        timeToAnswer.start()
            
        while True:

            time = timeToAnswer.getTime()
            if time == 0:
                state += 1
                break

            # Check for and handle events
            for event in pygame.event.get():
                # If the event was a click on the close box, quit pygame and the program 
                if event.type == pygame.QUIT:        
                    pygame.quit()  
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP1:
                        userAnswer = 1
                    elif event.key == pygame.K_KP2:
                        userAnswer = 2
                        
                   

            # 10 - Draw all screen elements
            background.draw()
            enemy.draw()
            player.draw()

            # 11 - Update the screen
            pygame.display.update()
        
            # 12 - Slow things down a bit
            clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount



    if state == 3:          #Winner and animation
            
        enemyGuess = randint(1,2)

        if userAnswer == enemyZone:
            print("Player Shoots!")
            userAnswer = 0
        elif enemyGuess == playerZone:
            print("Enemy Shoots!")
        #It's a draw
        else:
            print("It's a draw!")

        state = 2
        
        # 10 - Draw all screen elements
        background.draw()
        enemy.draw()
        player.draw()

        # 11 - Update the screen
        pygame.display.update()
    
        # 12 - Slow things down a bit
        clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount

        if player.dead():
            state = 4


    if state == 4:
        break
