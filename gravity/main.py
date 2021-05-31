#####################
# Part A: GAME SETUP:
#####################
# define classes, constants, initialize & import game assets below
import sys
import pygame
import config
import random
# Color lists. Check out http://www.colorpicker.com/
BLACK = [0,0,0]
WHITE = [255,255,255]
RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]
gravity = 14
jump_counter = 5
obstacle_list = []
# Start pygame
pygame.init()

# create the screen
SIZE = [700,500]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("GAME")

# import pictures and convert pictures to pygame.Surface

# create game objects
bo = config.Character(0, SIZE[1]-125)
obstacle_counter = 0
next_obstacle = random.randint(25*3, 25*5)
obstacle_types = [config.LandObstacle, config.SkyObstacle]
obstacle_list = []
has_collided = False
boom_counter = 0
fonty = pygame.font.Font("Montserrat-Regular.ttf", 50)
texty = fonty.render("GAME OVER", True, [0,0,255])
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

        if event.type == pygame.KEYDOWN:
            print("key pressed")
            print(event.key)
           
            print(bo.rect.bottom, SIZE[1])
            
            if keys[pygame.K_UP]and bo.rect.bottom >= SIZE[1]:
                jump_counter = 0

                keys = pygame.key.get_pressed()
    
            if keys[pygame.K_DOWN]:
                bo.duck()
            
        if event.type == pygame.KEYUP:    
            if keys[pygame.K_DOWN] == 0:
                bo.stand()


    #------------------------#
    # STEP 2: UPDATE GAME DATA
    #------------------------#
    
    if bo.lives > 0:
        if bo.rect.y < SIZE[1] - bo.rect.height:
            bo.rect.y += gravity
        if jump_counter < 5:
            bo.jump()
            jump_counter += 1
        obstacle_counter += 1
        if obstacle_counter == next_obstacle:
            obstacle_type = random.choice(obstacle_types)
            obstacle = obstacle_type()
            obstacle_list.append(obstacle)
            next_obstacle += random.randint(25*3, 25*5)
        for element in obstacle_list:
            element.rect.x -= 21
        bo.score += 1
        bo.scorelabel = bo.font.render("Score: " + str(bo.score), True, [0,0,255])
        for i in range(len(obstacle_list)):
            if pygame.sprite.collide_rect(bo, obstacle_list[i]):
                has_collided = True
                bo.lives -= 1
                bo.liveslabel = bo.font.render("Lives: " + str(bo.lives), True, [0,0,255])
                boom = config.Boom(obstacle_list[i].rect.x, obstacle_list[i].rect.y)
                obstacle_list[i].rect.y = 10000
            if has_collided:
                boom_counter += 1
                if boom_counter == 25:
                    has_collided = False
                    boom_counter = 0

    #-----------#
    #STEP 3: DRAW
    #-----------#

    # First draw the background
    screen.fill(BLACK)
        
    # Next draw all game objects
    screen.blit(bo.surface, [bo.rect.x ,bo.rect.y])
    screen.blit(bo.scorelabel, [0, 0])
    screen.blit(bo.liveslabel, [0, bo.scorelabel.get_rect().h])
    if has_collided:
        screen.blit(boom.surface, [boom.rect.x, boom.rect.y])

    for element in obstacle_list:
        screen.blit(element.surface, [element.rect.x, element.rect.y])

    if bo.lives == 0:
        screen.blit(texty, [SIZE[0]//2 - texty.get_rect().w//2, SIZE[1]//2 - texty.get_rect().h//2])
        

    # Lastly, update the display when you're done drawing
    pygame.display.update()

    # set the FPS here
    clock.tick(25)
