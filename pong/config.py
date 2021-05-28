import pygame
SIZE = [800,600]
BLACK = [0,0,0]
BLUE = [0, 0, 255]
class Paddle(pygame.sprite.Sprite):
  def __init__(self, picture, num, x, y):
    super().__init__()
    self.surface = pygame.image.load(picture).convert()
    self.surface = pygame.transform.scale(self.surface,[30,100])
    self.faceup = self.surface
    self.facedown = pygame.transform.flip(self.surface, False, True)
    self.rect = self.surface.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.font = pygame.font.Font("font.ttf", 35)
    self.score = 0
    self.num = num
    self.score_surface = self.font.render(f"P{self.num} Score: {self.score}", True, BLUE)
  def update(self, up, down):
    keys = pygame.key.get_pressed()
    if keys[up]:
      self.surface = self.faceup
      if self.rect.top > 0:
        self.rect.y -= 20
    if keys[down]:
      self.surface = self.facedown
      if self.rect.bottom < SIZE[1]:
        self.rect.y += 20
class Ball(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.surface = pygame.image.load("hud_p1.png").convert()
    self.surface = pygame.transform.scale(self.surface,[30,30])
    self.rect = self.surface.get_rect()
    self.rect.x = SIZE[0]//2
    self.rect.y = SIZE[1]//2
    self.xspeed = 10
    self.yspeed = 10
  def update(self, paddle1, paddle2):
    self.rect.x += self.xspeed
    self.rect.y += self.yspeed
    if self.rect.top <= 0 or self.rect.bottom >= 600:
      print(self.rect.bottom)
      self.yspeed *= -1
      wall = pygame.mixer.Sound("sfx_wall.wav")
      wall.play()
    
    if pygame.sprite.collide_rect(self, paddle1) or pygame.sprite.collide_rect(self, paddle2):
      self.xspeed *= -1
      bounce = pygame.mixer.Sound("saucerSmall.wav")
      bounce.play()
 