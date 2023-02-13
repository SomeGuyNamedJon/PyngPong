import numpy as py
import pygame
pygame.init()

BASE_COLOR = (200,200,200)
HIT_COLOR = (255,255,255)

class Ball(pygame.sprite.Sprite):
    def __init__(self, velocity, direction, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.velocity = velocity
        self.direction = direction
        self.position = (pos_x,pos_y)

        self.image = pygame.Surface((30, 30))
        self.image.fill(BASE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handleBoundry(self, dimensions, score):
        (width, height) = dimensions
        (x, y) = self.position
        (dx, dy) = self.direction
        if y <= 0 or y >= height:
            dy *= -1
        if x <= 0 or x >= width:
            if(x <= 0):
                score.enemyPoint()
            else:
                score.playerPoint()

            dx *= -1
            (x, y) = (width//2, height//2)

        self.position = (x, y)
        self.direction = (dx, dy)

    def update(self, dimensions, score):
        self.handleBoundry(dimensions, score)
        vector = tuple([x*self.velocity for x in self.direction]) 
        self.position = tuple(py.add(self.position, vector))
        self.rect.center = self.position


    def paddleHit(self, paddle):
        (dx, dy) = self.direction

        if(self.rect.centery > paddle.rect.top and self.rect.centery < paddle.rect.bottom):
            dx *= -1

        if(self.rect.centery < paddle.rect.top):
            dy = -1
            self.rect.bottom = paddle.rect.top

        if(self.rect.centery > paddle.rect.bottom):
            dy = 1
            self.rect.top = paddle.rect.bottom

        self.direction = (dx, dy)
