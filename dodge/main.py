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
SIZE = [1000,600]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("GAME")

# import pictures and convert pictures to pygame.Surface

# create game objects
player = config.Player()
screenimage = pygame.image.load("background.jpg").convert()
screenimage = pygame.transform.scale(screenimage, [1000, 600])
up_ball = config.UpBall()
down_ball = config.DownBall()
left_ball = config.LeftBall()
right_ball = config.RightBall()
bonus_ball = config.Bonus()
ball_list = [up_ball, down_ball, left_ball, right_ball, bonus_ball]
ball_group = pygame.sprite.Group()
for ball in ball_list:
    ball_group.add(ball)
score_counter = 0
COOLDOWN = 2000
CDstart = pygame.time.get_ticks() 
score_counter = 0
font = pygame.font.Font("KoHo-Medium.ttf", 25)
score_surface = font.render("Score:" + str(player.score), True, WHITE)
gameover_surface = font.render("GAME OVER! D=", True, RED)
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
    if not player.dead:
        if keys[pygame.K_SPACE] and CDnow - CDstart > COOLDOWN:
            CDstart = CDnow
            if keys[pygame.K_UP]:
                player.rect.y -= 150
            elif keys[pygame.K_DOWN]:
                player.rect.y += 150
            elif keys[pygame.K_LEFT]:
                player.rect.x -= 150
            elif keys[pygame.K_RIGHT]:
                player.rect.x += 150
        CDnow = pygame.time.get_ticks()
        cooldown_value = (CDnow - CDstart)/1000
        if CDnow - CDstart >= COOLDOWN:
            cooldown_value = "Dash is ready"
        dash_text = font.render(f"Dash cooldown: {cooldown_value}", True, BLUE)
    
        player.update(up_ball, down_ball, left_ball, right_ball, bonus_ball)
        ball_group.update()
        score_surface = font.render("Score:" + str(player.score), True, RED)
    score_counter += 1
    if score_counter % 25 == 0:
        player.score += 1
    #-----------#
    #STEP 3: DRAW
    #-----------#
    
    # First draw the background
    screen.fill(BLACK)
    
    # Next draw all game objects
    screen.blit(screenimage, [0, 0])
    screen.blit(player.image, [player.rect.x, player.rect.y])
    ball_group.draw(screen)
    screen.blit(score_surface, [0, 0])
    if player.dead == True:
        screen.blit(gameover_surface, [SIZE[0]//2 - gameover_surface.get_width()//2, SIZE[1]//2 - gameover_surface.get_height()//2])
    screen.blit(dash_text, [200, 0])
    # Lastly, update the display when you're done drawing
    pygame.display.update()

    # set the FPS here
    clock.tick(25)
