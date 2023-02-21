import random as r
from paddle import PaddlePlayer, PaddleAI
from ball import Ball
from scorecard import ScoreCard
import pygame
pygame.init()

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("assets")

PADDLE_A_SOUND = pygame.mixer.Sound("pongblipc5.wav")
PADDLE_B_SOUND = pygame.mixer.Sound("pongblipf5.wav")
BALL_SOUND = pygame.mixer.Sound("pongblipb3.wav")
GOAL_SOUND = pygame.mixer.Sound("goal.wav")

class GameManager():
    def __init__(self, settings, dimensions, font):
        (width, height) = dimensions
        Player1_Paddle = PaddlePlayer(50, height//2, PADDLE_A_SOUND)
        Player2_Paddle = PaddlePlayer(width - 50, height//2, PADDLE_B_SOUND)
        CPU1_Paddle = PaddleAI(50, height//2, PADDLE_A_SOUND)
        CPU2_Paddle = PaddleAI(width - 50, height//2, PADDLE_B_SOUND)

        dx = r.uniform(-2.5, 2.5)
        dy = r.uniform(-1.0, 1.0)
        ball_direction = (1 if dx == 0 else dx, 1 if dy == 0 else dy)
        self.ball = Ball((0,0), ball_direction, width//2, height//2, BALL_SOUND)
        self.score = ScoreCard(font, GOAL_SOUND)
        self.paddle_a = CPU1_Paddle if settings.a == "cpu" else Player1_Paddle
        self.paddle_b = CPU2_Paddle if settings.b == "cpu" else Player2_Paddle
