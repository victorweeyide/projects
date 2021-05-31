import sys
import pygame
import config
import random 

#####################
# Part A: GAME SETUP:
#####################
# define classes, constants, initialize & import game assets below

# Color lists. Check out http://www.colorpicker.com/
BLACK = [0,0,0]
WHITE = [255,255,255]
RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]

# Start pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode(config.SIZE)
pygame.display.set_caption("GAME")

# import pictures and convert pictures to pygame.Surface

# create game objects
player = config.Character("mrcheese.png", 1, 100, 140)
player2 = config.Character("Spike_Dark_Lord.png", 2, 130, 100)
score = 0
timer = 30
timer_counter = 0
font = pygame.font.Font("fony.ttf", 35)
timer_surface = font.render(f"Time:) {timer}", True, BLUE)
gameover_surface = font.render("GAME OVER!", True, GREEN)
cheese_list = []



# clock for setting FPS
clock = pygame.time.Clock()

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
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            print("key pressed")
            print(event.key)
            if timer > 0:
                player.update(keys, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
                player2.update(keys, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    #------------------------#
    # STEP 2: UPDATE GAME DATA
    #------------------------#
    timer_counter += 1
    if timer > 0:
        if timer_counter % 25 == 0:
            timer -= 1
            timer_surface = font.render(f"Time: {timer}", True, BLUE)
        if timer_counter % 50 == 0:
            x = random.randint(0, config.SIZE[0] - 60)
            y = random.randint(0, config.SIZE[1] - 60)
            cheese_list.append(config.Cheese(x,y))      
        collided_list = []
        for i in range(len(cheese_list)):
            if pygame.sprite.collide_rect(player, cheese_list[i]):
                player.score += 1
                player.score_surface = font.render(f"P{player.num} Score: {player.score}", True, RED)
                collided_list.append(i)
            if pygame.sprite.collide_rect(player2, cheese_list[i]):
                player2.score += 1
                player2.score_surface = font.render(f"P{player2.num} Score: {player2.score}", True, RED)
                collided_list.append(i)
        for i in collided_list:
            cheese_list.pop(i)
            
    #-----------#
    #STEP 3: DRAW
    #-----------#
    
    # First draw the background
    screen.fill(BLACK)
    
    # Next draw all game objects
    screen.blit(player.surface, [player.rect.x, player.rect.y])
    screen.blit(player2.surface, [player2.rect.x, player2.rect.y])
    screen.blit(player.score_surface, [0, 0])
    screen.blit(player2.score_surface, [0, player.score_surface.get_rect().height])
    screen.blit(timer_surface, [config.SIZE[0]-timer_surface.get_rect().w,0])
    for i in range(len(cheese_list)):
        screen.blit(cheese_list[i].surface, [cheese_list[i].rect.x, cheese_list[i].rect.y])
    if timer == 0:
        screen.blit(gameover_surface, [config.SIZE[0]//2- gameover_surface.get_rect().w//2, config.SIZE[1]//2-gameover_surface.get_rect().h//2])


    # Lastly, update the display when you're done drawing
    pygame.display.update()

    # set the FPS here
    clock.tick(25)
