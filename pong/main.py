import sys
import pygame
import config
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
SIZE = [800,600]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("GAME")

# import pictures and convert pictures to pygame.Surface

# create game objects
paddle = config.Paddle("paddle.png", 1, 50, SIZE[1]//2 - 50)
paddle2 = config.Paddle("paddle2.png", 2, SIZE[0] - 50 - 30, SIZE[1]//2 - 50)
ball = config.Ball(350,250)
font = pygame.font.Font("font.ttf", 35)
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
    


    #------------------------#
    # STEP 2: UPDATE GAME DATA
    #------------------------#
    paddle.update(pygame.K_w, pygame.K_s)
    paddle2.update(pygame.K_UP, pygame.K_DOWN)
    ball.update(paddle, paddle2)
    if ball.rect.left <= 0 or ball.rect.right >= SIZE[0]:
      if ball.rect.left <= 0:
        paddle2.score += 1
        paddle2.score_surface = font.render(f"P{paddle2.num} Score: {paddle2.score}", True, BLUE)
      elif ball.rect.right >= SIZE[0]:
        paddle.score += 1
        paddle.score_surface = font.render(f"P{paddle.num} Score: {paddle.score}", True, BLUE)
      ball.rect.x = 350
      ball.rect.y = 250
      score = pygame.mixer.Sound("sfx_score.wav")
      score.play()
    

    #-----------#
    #STEP 3: DRAW
    #-----------#
    
    # First draw the background
    screen.fill(BLACK)
    
    # Next draw all game objects
    screen.blit(paddle.surface, [paddle.rect.x, paddle.rect.y])
    screen.blit(paddle2.surface, [paddle2.rect.x, paddle2.rect.y])
    screen.blit(ball.surface, [ball.rect.x,ball.rect.y])
    screen.blit(paddle.score_surface, [0, 0])
    screen.blit(paddle2.score_surface, [0, paddle.score_surface.get_rect().height])
    



    # Lastly, update the display when you're done drawing
    pygame.display.update()

    # set the FPS here
    clock.tick(25)
    