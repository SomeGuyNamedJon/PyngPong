import random as r
from paddle import PaddlePlayer, PaddleAI
from ball import Ball
from scorecard import ScoreCard
import pygame
pygame.init()

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("assets")

BG_COLOR = (50, 50, 50)
TEXT_COLOR = (70, 70, 70)
SPEED_COLOR_1 = (165, 165, 80)
SPEED_COLOR_2 = (185, 125, 70)
SPEED_COLOR_3 = (205, 100, 60)
SPEED_COLOR_4 = (235, 80, 50)
SPEED_COLOR_MAX = (255, 50, 30)

PADDLE_A_SOUND = pygame.mixer.Sound("pongblipc5.wav")
PADDLE_B_SOUND = pygame.mixer.Sound("pongblipf5.wav")
BALL_SOUND = pygame.mixer.Sound("pongblipb3.wav")
GOAL_SOUND = pygame.mixer.Sound("goal.wav")

class GameManager():
    def __init__(self, settings, dimensions, font):
        self.font = font

        (self.width, self.height) = dimensions
        Player1_Paddle = PaddlePlayer(50, self.height//2, PADDLE_A_SOUND)
        Player2_Paddle = PaddlePlayer(self.width - 50, self.height//2, PADDLE_B_SOUND)
        CPU1_Paddle = PaddleAI(50, self.height//2, PADDLE_A_SOUND)
        CPU2_Paddle = PaddleAI(self.width - 50, self.height//2, PADDLE_B_SOUND)

        dx = r.uniform(-2.5, 2.5)
        dy = r.uniform(-1.0, 1.0)
        ball_direction = (1 if dx == 0 else dx, 1 if dy == 0 else dy)
        self.ball = Ball((0,0), ball_direction, self.width//2, self.height//2, BALL_SOUND)
        self.score = ScoreCard(font, GOAL_SOUND)
        self.paddle_a = CPU1_Paddle if settings.a == "cpu" else Player1_Paddle
        self.paddle_b = CPU2_Paddle if settings.b == "cpu" else Player2_Paddle

    def draw_divider(self, screen, color, dimensions, dot_size):
        (width, height) = dimensions
        for i in range(0, height, dot_size*2):
            rect = pygame.Rect(width//2, i, dot_size, dot_size)
            pygame.draw.rect(screen, color, rect)

    def draw_speed(self, screen, width):
        (text, rect) = self.get_speed(width)
        pygame.draw.rect(screen, BG_COLOR, rect.inflate(0,15))
        screen.blit(text, rect)


    def get_speed(self, width):
        string = '{0:.2f}'.format(self.ball.speed)
        color = TEXT_COLOR
        if(self.ball.speed > 9):
            color = SPEED_COLOR_1
        if(self.ball.speed > 12):
            color = SPEED_COLOR_2
        if(self.ball.speed > 18):
            color = SPEED_COLOR_3
        if(self.ball.speed > 24):
            color = SPEED_COLOR_4
        if(self.ball.speed >= 30):
            color = SPEED_COLOR_MAX
            string = "MAX"

        text = self.font.render(string, True, color)
        text = pygame.transform.scale(text, (90, 50))
        rect = text.get_rect()
        rect.center = (width // 2 + 5, 60)

        return (text,rect)
    
    def update(self, dimensions, screen):
        self.ball.update(dimensions, screen, self.score)
        self.paddle_a.update(self.ball, dimensions)
        self.paddle_b.update(self.ball, dimensions)
    
    def draw(self, screen, dimensions):
        self.score.draw(screen, dimensions)
        self.draw_divider(screen, TEXT_COLOR, dimensions, 7)
        self.draw_speed(screen, dimensions[0])
        self.ball.draw(screen)
        self.paddle_a.draw(screen)
        self.paddle_b.draw(screen)
