import numpy as py
import pygame
pygame.init()

BASE_COLOR = (200,200,200)
HIT_COLOR = (255,255,255)
SPEED = 5

class Ball(pygame.sprite.Sprite):
    def __init__(self, velocity, direction, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.direction = direction
        self.velocity = (SPEED, SPEED)
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
            dy *= -1
            (x, y) = (width//2, height//2)

        self.position = (x, y)
        self.direction = (dx, dy)
        self.velocity = (SPEED, SPEED)

    def update(self, dimensions, score):
        self.handleBoundry(dimensions, score)
        self.velocity = tuple([x*y for x,y in zip(self.direction, self.velocity)])
        self.position = tuple(py.add(self.position, self.velocity))
        self.rect.center = self.position

    def paddleHit(self, paddle):
        (dx, dy) = self.direction

        if self.rect.top < paddle.rect.top:
            dy = -1
        if self.rect.bottom > paddle.rect.bottom:
            dy = 1

        if self.rect.left < paddle.rect.left or self.rect.right > paddle.rect.right:
            dx *= -1

        self.direction = (dx, dy)
        self.velocity = tuple(py.add(self.velocity,paddle.velocity))
