import numpy as py
import pygame
pygame.init()

BASE_COLOR = (200,200,200)
HIT_COLOR = (255,255,255)
SPEED = 1

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

        self.react_duration = 450
        self.react_start_time = 0
        self.reacted = False

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
        self.clearHit()

    def clearHit(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.react_start_time

        if self.reacted and elapsed_time >= self.react_duration:
            self.image.fill(BASE_COLOR)
            self.reacted = False

    def reactHit(self):
        current_time = pygame.time.get_ticks()
        if not self.reacted:
            self.image.fill(HIT_COLOR)
            self.react_start_time = current_time
            self.reacted = True

    def paddleHit(self, paddle):
        self.reactHit()
        (dx, dy) = self.direction
        collision_rect = self.rect.clip(paddle.rect)

        if collision_rect.width < collision_rect.height:
            dx *= -1
            if self.rect.centerx < paddle.rect.centerx:
                self.rect.right = paddle.rect.left
            else:
                self.rect.left = paddle.rect.right
        else:
            dy *= -1
            if self.rect.centery < paddle.rect.centery:
                self.rect.bottom = paddle.rect.top
            else:
                self.rect.top = paddle.rect.bottom

        self.direction = (dx, dy)
        self.position = self.rect.center