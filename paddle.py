import numpy as np
from custom_math import normalizeVector, smoothMap
import pygame
pygame.init()

PADDLE_DIMENSIONS = ((50, 175))
BASE_COLOR = (200,200,200)
HIT_COLOR = (255,255,255)
POINT_COLOR = (230, 255, 235)
LOSS_COLOR = (230, 180, 200)
BASE_SPEED = 10
BASE_FOLLOW = 150

class Paddle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, sound):
        pygame.sprite.Sprite.__init__(self)
        
        self.sound = sound
        self.position = (pos_x, pos_y)
        self.image = pygame.Surface(PADDLE_DIMENSIONS)
        self.image.fill(BASE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.react_duration = 300
        self.react_start_time = 0
        self.reacted = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)


    def handleBoundry(self, dimensions):
        (_, height) = dimensions
        if(self.rect.top <= 0):
            self.rect.top = 0
        if(self.rect.bottom >= height):
            self.rect.bottom = height

    def clearHit(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.react_start_time

        if self.reacted and elapsed_time >= self.react_duration:
            self.image.fill(BASE_COLOR)
            self.reacted = False

    def reactHit(self):
        current_time = pygame.time.get_ticks()
        if not self.reacted:
            self.sound.play()
            self.image.fill(HIT_COLOR)
            self.react_start_time = current_time
            self.reacted = True

    def handleCollision(self, ball):
        if(self.rect.colliderect(ball)):
            self.reactHit()
            ball.paddleHit(self)

    def update(self, ball, dimensions):
        self.handleCollision(ball)
        self.clearHit()
        self.rect.center = self.position
        self.handleBoundry(dimensions)

class PlayerPaddle(Paddle):
    def update(self, mouse_pos, ball, dimensions):
        (_, mouse_y) = mouse_pos
        self.position = (self.position[0], mouse_y)
        super().update(ball, dimensions)

class EnemyPaddle(Paddle):
    def __init__(self, pos_x, pos_y, sound):
        super().__init__(pos_x, pos_y, sound)
        self.speed = BASE_SPEED
        self.follow_gap = BASE_FOLLOW

    def updateXPOS(self, width):
        self.position = (width - 50, self.position[1])

    def update(self, ball, dimensions):
        (width, height) = dimensions
        self.updateXPOS(width)

        distance = np.array(np.subtract(self.position, ball.position))
        direction = 0
        ball_angle = normalizeVector(tuple(distance))
        self.speed = BASE_SPEED * abs(ball_angle[1]) + smoothMap(abs(distance[1]), height, BASE_SPEED) 
        self.follow_gap = smoothMap(distance[0], width//2, BASE_FOLLOW * smoothMap(height, 540, 1))

        if(self.rect.centery - self.follow_gap < ball.rect.centery < self.rect.centery + self.follow_gap):
            direction = 0
        elif(self.rect.centery > ball.rect.centery):
            direction = -1
        elif(self.rect.centery < ball.rect.centery):
            direction = 1

        if(ball.direction[0] > 0):
            self.position = (self.position[0], self.position[1]+(self.speed*direction))

        super().update(ball, dimensions)