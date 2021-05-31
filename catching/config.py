import pygame 
SIZE = [800, 600]
RED = [255, 0, 0]
class Character(pygame.sprite.Sprite):
    def __init__(self, picture, num, width, height) :
        self.surface = pygame.image.load(picture).convert()
        self.surface = pygame.transform.scale(self.surface, (width, height))
        self.faceright = self.surface
        self.faceleft = pygame.transform.flip(self.surface, True, False)
        self.rect = self.surface.get_rect()
        self.rect.x = SIZE[0] //2 - self.rect.w//2
        self.rect.y = SIZE[1] //2 - self.rect.h//2 
        self.score = 0
        self.num = num
        self.font = pygame.font.Font("font.ttf", 35)
        self.score_surface = self.font.render(f"P{self.num} Score: {self.score}", True, RED)
    def update(self, keys, up, down, left, right):
        if keys[up]:
            if self.rect.top > 0:
                self.rect.y -= 20
        if keys[down]:
            if self.rect.bottom < SIZE[1]:
                self.rect.y += 20
        if keys[left]:
            self.surface = self.faceleft
            if self.rect.left > 0:
                self.rect.x -= 20
        if keys[right]:
            self.surface = self.faceright
            if self.rect.right < SIZE[0]:
                self.rect.x += 20
                


class Cheese(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.surface = pygame.image.load("cheese.jpg").convert()
        self.surface = pygame.transform.scale(self.surface, (60,60))
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y