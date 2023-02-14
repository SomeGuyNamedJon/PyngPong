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
        self.velocity = velocity
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

    def update(self, dimensions, score):
        self.handleBoundry(dimensions, score)
        self.velocity = tuple(py.multiply(self.direction, SPEED))
        self.position = tuple(py.add(self.position, self.velocity))
        self.rect.center = self.position

    def paddleHit(self, paddle):
        (dx, dy) = self.direction
        
        paddle_left = (self.rect.right > paddle.rect.left and self.rect.left < paddle.rect.left)
        paddle_right = (self.rect.left < paddle.rect.right and self.rect.right > paddle.rect.right)
        paddle_top = (self.rect.bottom > paddle.rect.top and self.rect.top < paddle.rect.top)
        paddle_bottom = (self.rect.top < paddle.rect.bottom and self.rect.bottom > paddle.rect.bottom)

        paddle_side = (paddle.rect.top < self.rect.centery < paddle.rect.bottom) 
        paddle_block = (paddle.rect.left < self.rect.centerx < paddle.rect.right)

        if(paddle_side and paddle_left):
            self.rect.right = paddle.rect.left
            dx = -1
        if(paddle_side and paddle_right):
            self.rect.left = paddle.rect.right
            dx = 1
        if(paddle_block and paddle_top):
            self.rect.bottom = paddle.rect.top
            dy = -1
        if(paddle_block and paddle_bottom):
            self.rect.top = paddle.rect.bottom
            dy = 1

        self.position = self.rect.center
        self.direction = (dx, dy)
