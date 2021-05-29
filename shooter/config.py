import pygame
import random
BLACK = [0,0,0]
BLUE = [0,0,255]
SIZE = [800, 600]
class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.surface = pygame.image.load("player.png").convert()
    self.surface = pygame.transform.scale(self.surface,[40,70])
    self.rect = self.surface.get_rect()
    self.rect.x = SIZE[0]//2 - 20
    self.rect.y = 490
    font = pygame.font.Font("bit5x3.ttf", 30)
    self.score = 0
    self.score_surface = font.render(f"Score: {self.score}", True, BLUE)
    self.hp = 3
    self.hp_surface = font.render(f"Hp: {self.hp}", True, BLUE)
  def update(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      if self.rect.left > 0:
        self.rect.x -= 20
    if keys[pygame.K_RIGHT]:
      if self.rect.right < SIZE[0]:
        self.rect.x += 20
class Enemy(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    costumes = ["enemy1.png", "enemy2.png", "enemy3.png"]
    self.surface = pygame.image.load(random.choice(costumes)).convert()
    self.surface = pygame.transform.scale(self.surface,[50, 50])
    self.rect = self.surface.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.yspeed = 8
  def update(self):
    self.rect.y += self.yspeed
  def respawn(self):
      self.rect.x = random.randint(0, SIZE[0] - 50)
      self.rect.bottom = 0
class Bullet(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.surface = pygame.image.load("bullet.png").convert()
    self.surface = pygame.transform.scale(self.surface,[10, 40])
    self.rect = self.surface.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.yspeed = 20
  def update(self):
    self.rect.y -= self.yspeed
