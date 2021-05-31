import pygame
import random
SIZE = [1000,600]
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./DodgeAssets/Gawain.png")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-40, -40)
        self.score = 0
        self.rect.x = 400
        self.rect.y = 200
        self.score = 0
        self.dead = False
    def update(self, up_ball, down_ball, left_ball, right_ball, bonus_ball):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if self.rect.top > 0:
                self.rect.y -= 15
        if keys[pygame.K_DOWN]:
            if self.rect.bottom < SIZE[1]:
                self.rect.y += 15
        if keys[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.x -= 15
        if keys[pygame.K_RIGHT]:
            if self.rect.right < SIZE[0]:
                self.rect.x += 15
        for ball in [up_ball, down_ball, left_ball, right_ball]:
            if pygame.sprite.collide_rect(self, ball):
                self.dead = True
        if pygame.sprite.collide_rect(self, bonus_ball):
            bonus_ball.respawn()
            self.score += 5


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./DodgeAssets/boolet_25x25.png")
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-40, -40)
        self.directions = ["up", "down", "left", "right"]
        self.direction = random.choice(self.directions)
        self.difficulty = 8
        self.special = False
        if self.direction == "up":
            self.rect.y = SIZE[1]
            self.rect.x = random.randint(0, SIZE[0] - self.rect.width)  
        elif self.direction == "down":
            self.rect.bottom = 0
            self.rect.x = random.randint(0, SIZE[0] - self.rect.width)
        elif self.direction == "left":
            self.rect.x = SIZE[0]
            self.rect.y = random.randint(0, SIZE[1] - self.rect.height)
        elif self.direction == "right":
            self.rect.right = 0
            self.rect.y = random.randint(0, SIZE[1] - self.rect.height)
    def update(self):
        if self.direction == "up":
            self.rect.y -= self.difficulty
            if self.rect.bottom <= 0:
                self.rect.y = SIZE[1]
                self.rect.x = random.randint(0, SIZE[0] - self.rect.width)
        if self.direction == "down":
            self.rect.y += self.difficulty
            if self.rect.top >= SIZE[1]:
                self.rect.bottom = 0
                self.rect.x = random.randint(0, SIZE[0] - self.rect.width)
        if self.direction == "left":
            self.rect.x -= self.difficulty
            if self.rect.left <= 0:
                self.rect.x = SIZE[0]
                self.rect.y = random.randint(0, SIZE[1] - self.rect.height)
        if self.direction == "right":
            self.rect.x += self.difficulty
            if self.rect.right >= SIZE[0]:
                self.rect.right = 0
                self.rect.y = random.randint(0, SIZE[1] - self.rect.height)
class UpBall(Obstacle):
    def __init__(self):
        super().__init__()
        self.direction = "up"
        self.rect.y = SIZE[1]
        self.rect.x = random.randint(0, SIZE[0] - self.rect.width)
class DownBall(Obstacle):
    def __init__(self):
        super().__init__()
        self.direction = "down"
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SIZE[0] - self.rect.width)
class LeftBall(Obstacle):
    def __init__(self):
        super().__init__()
        self.direction = "left"
        self.rect.x = SIZE[0]        
        self.rect.y = random.randint(0, SIZE[1] - self.rect.height)
class RightBall(Obstacle):
    def __init__(self):
        super().__init__()
        self.direction = "right"
        self.rect.right = 0
        self.rect.y = random.randint(0, SIZE[1] - self.rect.height)
class Bonus(Obstacle):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./DodgeAssets/candy.png")
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-30, -30)
    def respawn(self):
        self.direction = random.choice(self.directions)
        if self.direction == "up":
            self.rect.y = SIZE[1]
            self.rect.x = random.randint(0, SIZE[0] - self.rect.width)  
        elif self.direction == "down":
            self.rect.bottom = 0
            self.rect.x = random.randint(0, SIZE[0] - self.rect.width)
        elif self.direction == "left":
            self.rect.x = SIZE[0]
            self.rect.y = random.randint(0, SIZE[1] - self.rect.height)
        elif self.direction == "right":
            self.rect.right = 0
            self.rect.y = random.randint(0, SIZE[1] - self.rect.height)
        