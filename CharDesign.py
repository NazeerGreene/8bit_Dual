from time import time
from pygwidgets import *
import random

Y_MIN = 350

X_MIN = 20
X_MAX = 750

class Character:

    def __init__(self):
        pass

    def draw(self):
        self.image.draw()

    def setZones(self, zoneList):
        """Sets the zone attribute for the object;
           enter a nested list of [zone, Zone_starting_location]"""
        
        if zoneDict == []:
            return -1
        self.zones = zoneList

    
    def randomZone(self):
        """Gets a random zone from the user defined list, so that the object may randomly
            place itself."""
        
        if self.zones == []:
            return -1
        
        zone, zoneStart = random.choice(zones)
        self.advance(zoneStart)
        return zone
        

class Enemy(Character):

    def __init__(self, window, x):
        #self.health = 5
        self.picture = "pictures/8bit_enemy.png"
        self.x = x
        self.y = Y_MIN
        self.zones = []
        self.window = window
        self.image = Image(self.window, (self.x, self.y), self.picture)
        

    def advance(self, x, adjust = 130):
        """To move the Enemy object to the new location;
            adjust is used to fit the entire picture into the zone."""
        
        self.x = x - adjust
        if self.x < X_MIN:
            self.x = X_MIN

        self.image.setLoc((self.x, self.y))

        

class player(Character):


    def __init__(self, window, x):
        self.health = 50
        self.picture = "pictures/8bit_player.png"
        self.x = x
        self.y = Y_MIN
        self.__zones = []
        self.window = window
        self.image = Image(self.window, (self.x, self.y), self.picture)

    def advance(self, x, adjust = 7):
        """To move the Player object to the new location;
            adjust is used to fit the entire picture into the zone."""
        
        self.x = x + adjust
        if self.x > X_MAX:
            self.x = X_MAX
                            
        self.image.setLoc((self.x, self.y))


    def attacked(self):
        self.health -= 5



class Bullet(Character):

    def __init__(self, window, x):
        self.picture = "pictures/8bit_bullet.png"
        self.window = window
        self.x = x
        self.y = Y_MIN + 30
        self.startLoc = (self.x, self.y)
        self.image = Image(self.window, self.startLoc, self.picture)

    def update(self, x):
        self.image.setLoc((self.x,self.y))
        
    @property
    def offScreen(self):
        return self.x < X_MIN or self.x > X_MAX
