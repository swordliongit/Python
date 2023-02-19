

import math
import pygame
import constants


class Character():
    def __init__(self, x, y) -> None:
        # create a rectangle for the player model
        self.rect = pygame.Rect(0, 0, 40, 40)
        # position the rectangle onto the coordinates that this player will be initialized with
        self.rect.center = (x, y)
        
    def draw(self, surface):
        pygame.draw.rect(surface, constants.RED, self.rect)
        
    # move the player by the amount of difference of x and y
    # handled by the x and y variables of the Rect object
    def move(self, dx, dy):
        
        # normalize diagonal speeding to be the same as vertical or horizontal speeding
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2)/2)
            dy = dy * (math.sqrt(2)/2)
        
        self.rect.x += dx
        self.rect.y += dy