from pygame import Surface
import pygame
import constants
from character import Character

# define player movement variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False


# helper function to scale images
def scale_img(image, scale) -> Surface:
    w = image.get_width()
    h = image.get_height()
    scaled_image = pygame.transform.scale(image, (w * scale, h * scale))
    return scaled_image

# start pygame
pygame.init()

# display the screen
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Crawler")

# clock for maintaining frame rate
clock = pygame.time.Clock()

# load images
animation_types = ["idle", "run"]
animation_list = {}
for animation in animation_types:
    intermediary_list = []
    for i in range(4):
        # converts the image to match the format of the screen and makes sure transparent pixels on the image remain transparent
        img = pygame.image.load(f"assets/images/characters/elf/{animation}/{i}.png").convert_alpha() # -> Surface
        img = scale_img(img, constants.SCALE)
        intermediary_list.append(img)
    animation_list[animation] = intermediary_list
print(animation_list)
# create player
player = Character(100, 100, animation_list)




# main game loop
running = True
while running:
    # control frame rate
    clock.tick(constants.FPS)
    
    # to fix the trails of the previous drawings when the player moves, otherwise leaves trail for every pixel
    screen.fill(constants.BG)
    
    # calculate player movement
    # top left corner is (0, 0)
    dx = 0
    dy = 0
    if moving_right:
        dx = constants.SPEED
    if moving_left:
        dx = -constants.SPEED
    if moving_up:
        dy = -constants.SPEED
    if moving_down:
        dy = constants.SPEED
    # move the player now
    player.move(dx, dy)
    
    # update the animation
    player.update()
    
    # draw the player on the screen
    player.draw(screen)
    
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # check if keys pressed    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True
                
        # check if keys released  
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_s:
                moving_down = False
            
    pygame.display.update()
            
pygame.quit()