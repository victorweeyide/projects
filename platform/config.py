import pygame
import random
SIZE = [900,600]
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface([35,35])
        self.surface.fill([random.randint(0,255), random.randint(0,255), random.randint(0,255)])
        self.rect = self.surface.get_rect()
        self.rect.x = 25
        self.rect.y = 575
        self.gravity = 10
        self.jump_counter = 999
        self.yspeed = 0
        self.supported = False
        self.xspeed = 0
    def jump(self):
        self.rect.y -= 45
    def update(self):
        self.rect.y += self.gravity + self.yspeed
        self.rect.x += self.xspeed
        if self.rect.bottom < SIZE[1]:
            self.gravity = 15
        elif self.rect.bottom >= SIZE[1]:
            self.rect.bottom = SIZE[1]
            self.gravity = 0
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, xspeed = 0, yspeed = 0):
        super().__init__() 
        self.image = pygame.Surface([random.randint(100,130),35])
        self.image.fill([random.randint(0,255), random.randint(0,255), random.randint(0,255)])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed     
    def support(self,player):
        player.yspeed = 0
        if pygame.sprite.collide_rect(self,player):
            if player.rect.bottom >= self.rect.top >= player.rect.top:
                player.rect.bottom = self.rect.top
                player.yspeed = -10
                player.supported = True
            elif player.rect.top <= self.rect.bottom <= player.rect.bottom:
                player.rect.top = self.rect.bottom
                player.yspeed = 20
            elif player.rect.right >= self.rect.left >= player.rect.left:
                player.rect.right = self.rect.left
                player.xspeed *= -1
            elif player.rect.left <= self.rect.right <= player.rect.right:
                player.rect.left = self.rect.right
                player.xspeed *= 1

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("portal.png")
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        