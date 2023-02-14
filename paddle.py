import time
import pygame
pygame.init()

PADDLE_DIMENSIONS = ((50, 175))
BASE_COLOR = (200,200,200)
HIT_COLOR = (255,255,255)
POINT_COLOR = (230, 255, 235)
LOSS_COLOR = (230, 180, 200)
BASE_SPEED = 3

class Paddle(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.position = (pos_x, pos_y)
        self.position_old = self.position 
        self.velocity = (0,0)
        self.image = pygame.Surface(PADDLE_DIMENSIONS)
        self.image.fill(BASE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = self.position


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handleBoundry(self, height):
        if(self.rect.top <= 0):
            self.rect.top = 0
        if(self.rect.bottom >= height):
            self.rect.bottom = height

    def handleCollision(self, ball):
        if(self.rect.colliderect(ball)):
            ball.paddleHit(self)

    def updateVelocity(self):
        vx = self.position[0] - self.position_old[0]
        vy = self.position[1] - self.position_old[1]
        self.velocity = (vx, vy)


    def update(self, ball):
        self.updateVelocity()
        self.handleCollision(ball)
        self.rect.center = self.position
        self.handleBoundry(540)

class PlayerPaddle(Paddle):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)

    def update(self, mouse_pos, ball):
        (_, mouse_y) = mouse_pos
        self.position_old = self.position
        self.position = (self.position[0], mouse_y)
        super().update(ball)

class EnemyPaddle(Paddle):
    
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y)
        self.speed = BASE_SPEED

    def update(self, ball):
        (ball_x, ball_y) = ball.position
        (x, y) = self.position
        distance = x - ball_x

        if(distance <= 0):
            step = 0
        else:
            step = (BASE_SPEED/(distance+1)) * 10

        if(self.rect.top < ball_y < self.rect.bottom):
            self.speed = BASE_SPEED
        if(y > ball_y):
            self.position = (x, y-self.speed)
            self.speed += step
        if(y < ball_y):
            self.position = (x, y+self.speed)
            self.speed += step

        self.position_old = (x, y)        
        super().update(ball)