

import math
import pygame
import constants


class Character():
    def __init__(self, x, y, mob_animations, char_type) -> None:
        self.char_type = char_type
        self.animation_list = mob_animations[char_type]
        # handles flipping the character image
        self.flip = False
        # starting animation frame
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        # start with idle
        self.running = False
        self.action = 0
        self.image = self.animation_list[self.action][self.frame_index]
        # create a rectangle for the character model
        self.rect = pygame.Rect(0, 0, 40, 40)
        # position the rectangle onto the coordinates that this character will be initialized with
        self.rect.center = (x, y)
        
    def draw(self, surface):
        # this will flip the character if self.flip is True and then draw blit it onto the Rect of the character
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        if self.char_type == 0:
            surface.blit(flipped_image, (self.rect.x, self.rect.y - constants.SCALE * constants.OFFSET))
        else:
            surface.blit(flipped_image, self.rect)
        pygame.draw.rect(surface, constants.RED, self.rect, 1)
        
    def update(self):
        # check what action the character is performing
        if self.running == True:
            self.update_action(1)
        else:
            self.update_action(0)
        
        
        animation_cooldown = 70
        # handle the animation
        # update the image
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        # if all animations are shown, start from the beginning
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
        
    def update_action(self, new_action):
        # check if the new action is different than the previous one, change the action if so
        if new_action != self.action:
            self.action = new_action
        
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
        
    # move the player by the amount of difference of x and y
    # handled by the x and y variables of the Rect object
    def move(self, dx, dy):
        self.running = False
        
        # if there's any difference, the player is running
        if dx != 0 or dy != 0:
            self.running = True
        
        if dx < 0:
            self.flip = True
        if dx > 0:
            self.flip = False
        # normalize diagonal speeding to be the same as vertical or horizontal speeding
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2)/2)
            dy = dy * (math.sqrt(2)/2)
    
        
        self.rect.x += dx
        self.rect.y += dy