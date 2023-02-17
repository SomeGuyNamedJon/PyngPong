import random as r
import pygame
from paddle import PaddlePlayer, PaddleAI
from ball import Ball
from scorecard import ScoreCard
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("assets")

pygame.init()
pygame.display.set_caption("PλngPong")

SPEED_COLOR_1 = (200, 175, 70)
SPEED_COLOR_2 = (222, 204, 51)
SPEED_COLOR_3 = (233, 124, 92)
SPEED_COLOR_4 = (244, 87, 68)
SPEED_COLOR_MAX = (255, 31, 31)
BG_COLOR = (50, 50, 50)
BG_ELEM_COLOR = (70, 70, 70)
WIDTH, HEIGHT = 960, 540
DIMENSIONS = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(DIMENSIONS)
FPS = 60
PADDLE_A_SOUND = pygame.mixer.Sound("pongblipc5.wav")
PADDLE_B_SOUND = pygame.mixer.Sound("pongblipf5.wav")
BALL_SOUND = pygame.mixer.Sound("pongblipb3.wav")
FONT = pygame.font.Font("BitPap.ttf", 500)
BX = r.uniform(-1.0, 1.0)
BY = r.uniform(-1.0, 1.0)
BALL_DIRECTION = (BX, BY)

playerPaddle = PaddlePlayer(50, HEIGHT//2, PADDLE_A_SOUND)
AI_Paddle = PaddleAI(50, HEIGHT//2, PADDLE_A_SOUND)
enemyPaddle = PaddleAI(WIDTH - 50, HEIGHT//2, PADDLE_B_SOUND)
ball = Ball((0,0), BALL_DIRECTION, WIDTH//2, HEIGHT//2, BALL_SOUND)
score = ScoreCard(BG_ELEM_COLOR, FONT)

def draw_background():
    SCREEN.fill(BG_COLOR)

def draw_divider(color, dimensions, dot_size):
    (width, height) = dimensions
    for i in range(0, height, dot_size*2):
        rect = pygame.Rect(width//2, i, dot_size, dot_size)
        pygame.draw.rect(SCREEN, color, rect)

def draw_speed(ball):
    string = '{0:.2f}'.format(ball.speed)
    color = BG_ELEM_COLOR
    if(ball.speed > 10):
        color = SPEED_COLOR_1
    if(ball.speed > 15):
        color = SPEED_COLOR_2
    if(ball.speed > 20):
        color = SPEED_COLOR_3
    if(ball.speed > 25):
        color = SPEED_COLOR_4
    if(ball.speed >= 30):
        color = SPEED_COLOR_MAX
        string = "MAX"

    width = SCREEN.get_width()
    text = FONT.render(string, True, color)
    text = pygame.transform.scale(text, (90, 50))
    rect = text.get_rect()
    rect.center = (width // 2 + 5, 60)
    pygame.draw.rect(SCREEN, BG_COLOR, rect.inflate(0,15))
    SCREEN.blit(text, rect)

def draw_board(dimensions):
    score.draw(SCREEN, dimensions)
    draw_divider(BG_ELEM_COLOR, dimensions, 7)
    draw_speed(ball)
    ball.draw(SCREEN)
    AI_Paddle.draw(SCREEN)
    enemyPaddle.draw(SCREEN)

def update_game(dimensions):
    ball.update(dimensions, SCREEN, score)
    AI_Paddle.update(ball, dimensions)
    enemyPaddle.update(ball, dimensions)

def main():
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        dimensions = (SCREEN.get_width(), SCREEN.get_height())

        draw_background()
        update_game(dimensions)        
        draw_board(dimensions)

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    run = False
                    break

        pygame.display.update()

if __name__ == "__main__":
    main()