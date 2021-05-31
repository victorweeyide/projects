import pygame
SIZE = [700, 500]
class Character(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.surface1 = pygame.image.load("bo.png").convert()
        self.surface1 = pygame.transform.scale(self.surface1, [125, 125])
        self.surface2 = pygame.image.load("flatbo.png").convert()
        self.surface2 = pygame.transform.scale(self.surface2, [90, 90])
        self.surface = self.surface1
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.font = pygame.font.Font("Montserrat-Regular.ttf", 30)
        self.score = 0
        self.scorelabel = self.font.render("Score: " + str(self.score), True, [0,0,255])
        self.lives = 3
        self.liveslabel = self.font.render("Lives: " + str(self.lives), True, [0,0,255])
    def jump(self):
        self.rect.y -= 42
    def duck(self):
            self.surface = self.surface2
            self.rect.y += 35
    def stand(self):
            self.surface = self.surface1
            self.rect.y -= 35
class LandObstacle(pygame.sprite.Sprite):
    def __init__(self):
        self.surface = pygame.image.load("cube.png").convert()
        self.surface = pygame.transform.scale(self.surface, [55, 55])
        self.rect = self.surface.get_rect()
        self.rect.x = SIZE[0]
        self.rect.y = SIZE[1] - self.rect.height

        
class SkyObstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.image.load("crow.png").convert()
        self.surface = pygame.transform.scale(self.surface, [100, 100])
        self.surface = pygame.transform.flip(self.surface, True, False)
        self.rect = self.surface.get_rect()
        self.rect.x = SIZE[0]
        self.rect.y = SIZE[1] - self.rect.height - 110
         
        
class Boom(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.surface = pygame.image.load("boom.jpg").convert()
        self.surface = pygame.transform.scale(self.surface, (120,90))
        self.surface.set_colorkey([16, 16, 16])
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y