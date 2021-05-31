#####################
# Part A: GAME SETUP:
#####################
# define classes, constants, initialize & import game assets below
import sys
import pygame
import config

# Color lists. Check out http://www.colorpicker.com/
BLACK = [0,0,0]
WHITE = [255,255,255]
RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]

# Start pygame
pygame.init()

# create the screen
SIZE = [900,600]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("GAME")

# import pictures and convert pictures to pygame.Surface

# create game objects
player = config.Player()
platform1 = config.Platform(100,500)
platform2 = config.Platform(250,400, xspeed=9)
platform3 = config.Platform(450,300, yspeed=-7)
platform4 = config.Platform(700,200)
platform5 = config.Platform(0,250)
platform_list = pygame.sprite.Group()
platform_list.add(platform1, platform2, platform3, platform4, platform5)
portal1 = config.Portal(760,130)
portal2 = config.Portal(10,80)
font = pygame.font.Font("ZenDots-Regular.ttf", 50)
text_surface = font.render("YOU WON!:D", True, BLUE)
game_over = False
# clock for setting FPS
clock = pygame.time.Clock()
# music
pygame.mixer.init()
pygame.mixer.music.load("music.ogg")
pygame.mixer.music.play(-1)
###################
# Part B: GAME LOOP
###################

while True:
    #----------------------#
    # STEP 1: GET USER INPUT
    #----------------------#
    event_list = pygame.event.get()
    keys = pygame.key.get_pressed()
    for event in event_list:
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if not game_over:
            if event.type == pygame.KEYDOWN:
                print("key pressed")
                print(event.key)
            
            if keys[pygame.K_UP] and (player.rect.bottom == SIZE[1] or player.supported):
                player.jump_counter = 0

            if keys[pygame.K_LEFT]:
                player.xspeed = -15
            if keys[pygame.K_RIGHT]:
                player.xspeed = 15
        if event.type == pygame.KEYUP:
            player.xspeed = 0

    #------------------------#
    # STEP 2: UPDATE GAME DATA
    #------------------------#
    

    if player.jump_counter < 7:
        player.jump()
        player.jump_counter += 1
    player.update()
    if platform2.rect.x <= 100 or platform2.rect.x >= 700:
        platform2.xspeed *= -1
    if platform3.rect.y <= 100 or platform3.rect.y >= 400:
        platform3.yspeed *= -1
    player.supported = False
    for platform in platform_list:
        platform.update()
        platform.support(player)
    if player.supported:
        if player.rect.bottom == platform2.rect.top:
            player.rect.x += platform2.xspeed
        if player.rect.bottom == platform3.rect.top:
            player.rect.bottom = platform3.rect.top
    
    if pygame.sprite.collide_rect(player,portal1):
        player.rect.centerx = portal2.rect.centerx
        player.rect.centery = portal2.rect.centery
    if player.rect.bottom == platform5.rect.top and platform5.rect.left <= player.rect.centerx <= platform5.rect.right:
        platform2.xspeed = 0
        platform3.yspeed = 0
        game_over = True
    #-----------#
    #STEP 3: DRAW
    #-----------#
    
    # First draw the background
    screen.fill(BLACK)
    
    # Next draw all game objects
    screen.blit(player.surface, [player.rect.x, player.rect.y])
    platform_list.draw(screen)
    screen.blit(portal1.image, [portal1.rect.x, portal1.rect.y])
    screen.blit(portal2.image, [portal2.rect.x, portal2.rect.y])
    if player.rect.bottom == platform5.rect.top and platform.rect.left <= player.rect.centerx <= platform.rect.right:
        screen.blit(text_surface, [screen.get_rect().centerx - text_surface.get_width()//2, screen.get_rect().centery - text_surface.get_height()//2])


    # Lastly, update the display when you're done drawing
    pygame.display.update()

    # set the FPS here
    clock.tick(25)
