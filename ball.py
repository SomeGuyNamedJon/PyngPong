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

        self.react_duration = 450
        self.react_start_time = 0
        self.reacted = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def resetBall(self, width, height):
        self.position = (width//2, height//2)
        self.direction = (-self.direction[0], -self.direction[1])

    def handleBoundry(self, dimensions, screen, score):
        (width, height) = dimensions
        self.rect.clamp_ip(screen.get_rect())
        if self.rect.top == 0 or self.rect.bottom == height:
            self.direction = (self.direction[0], -self.direction[1])
        if self.rect.left <= 0 or self.rect.right >= width:
            if(self.rect.left <= 0):
                score.enemyPoint()
            else:
                score.playerPoint()
            self.resetBall(width, height)

        #if the ball somehow ends up outside the top or bottom bounds, just reset 
        if self.rect.bottom > height or self.rect.top < 0:
            self.resetBall(width, height)

    def update(self, dimensions, screen, score):
        self.handleBoundry(dimensions, screen, score)
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
        collision_rect = self.rect.clip(paddle.rect)

        if collision_rect.width < collision_rect.height:
            self.direction = (-self.direction[0], self.direction[1])
            if self.rect.centerx < paddle.rect.centerx:
                self.rect.right = paddle.rect.left
            else:
                self.rect.left = paddle.rect.right
        else:
            self.direction = (self.direction[0], -self.direction[1])
            if self.rect.centery < paddle.rect.centery:
                self.rect.bottom = paddle.rect.top
            else:
                self.rect.top = paddle.rect.bottom

        self.position = self.rect.center