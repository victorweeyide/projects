#####################
# Part A: GAME SETUP:
#####################
# define classes, constants, initialize & import game assets below
import config
import sys
import pygame
import random

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
player = config.Player()
enemies = []
bullets = []
timer_counter = 0
font = pygame.font.Font("bit5x3.ttf", 30)
shot_list = []
used_bullets = []
collided_list = []
gameover_surface = font.render("GAME OVER!", True, GREEN)
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
            if keys[pygame.K_SPACE]:
                bullet = config.Bullet(player.rect.centerx, player.rect.top)
                bullets.append(bullet)
                print(len(bullets)) 


    #------------------------#
    # STEP 2: UPDATE GAME DATA
    #------------------------#
    timer_counter += 1
    
    if player.hp > 0:
        player.update()
        
        for i in range(len(bullets)):
            if bullets[i].rect.y <= 0:
                used_bullets.append(i)
        used_bullets = []
        for i in range(-1, -len(used_bullets)-1, -1):
            bullets.pop(used_bullets[i])

        for i in range(len(enemies)):
            enemies[i].update()
        for n in range(len(bullets)):
            bullets[n].update()
        if timer_counter % 75 == 0:
            ex = random.randint(0, SIZE[0] - 50)
            ey = 0
            enemy = config.Enemy(ex, ey)
            enemies.append(enemy)
        shot_list = []
        used_bullets = []
        for a in range(len(enemies)):
            for b in range(len(bullets)):
                if pygame.sprite.collide_rect(enemies[a], bullets[b]) == True:
                    player.score += 1
                    player.score_surface = font.render(f"Score: {player.score}", True, BLUE)
                    shot = pygame.mixer.Sound("shot.wav")
                    shot.play()
                    shot_list.append(a)
                    used_bullets.append(b)
        for i in shot_list:
            enemies.pop(i)
        for i in used_bullets:
            bullets.pop(i)
        
        collided_list = []
        for c in range(len(enemies)):
            if pygame.sprite.collide_rect(enemies[c], player) == True:
                player.hp -= 1
                player.hp_surface = font.render(f"Hp: {player.hp}", True, BLUE)
                boom = pygame.mixer.Sound("boom.wav")
                boom.play()
                collided_list.append(c)
            if enemies[c].rect.y >= SIZE[1]:
                enemies[c].respawn()
        
        for i in collided_list:
            enemies.pop(i)
        
        

    #-----------#
    #STEP 3: DRAW
    #-----------#
    
    # First draw the background
    screen.fill(BLACK)
    
    # Next draw all game objects
    screen.blit(player.surface, [player.rect.x, player.rect.y])
    screen.blit(player.score_surface, [0, 0])
    screen.blit(player.hp_surface, [0, player.score_surface.get_rect().height])
    for i in range(len(enemies)):    
        screen.blit(enemies[i].surface, [enemies[i].rect.x, enemies[i].rect.y])
    for i in range(len(bullets)):    
        screen.blit(bullets[i].surface, [bullets[i].rect.x, bullets[i].rect.y])
    if player.hp == 0:
        screen.blit(gameover_surface, [SIZE[0]//2- gameover_surface.get_rect().w//2, SIZE[1]//2-gameover_surface.get_rect().h//2])
    # Lastly, update the display when you're done drawing
    pygame.display.update()

    # set the FPS here
    clock.tick(25)