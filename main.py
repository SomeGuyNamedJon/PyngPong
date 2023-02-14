import time
import pygame
from paddle import PlayerPaddle, EnemyPaddle
from ball import Ball
from scorecard import Score
import os
os.chdir("assets")

pygame.init()
pygame.display.set_caption("Pλng")

BG_COLOR = (50, 50, 50)
BG_ELEM_COLOR = (70, 70, 70)
WIDTH, HEIGHT = 960, 540
DIMENSIONS = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(DIMENSIONS)
FPS = 60
PLAYER_SOUND = pygame.mixer.Sound("pongblipb3.wav")
ENEMY_SOUND = pygame.mixer.Sound("pongblipc5.wav")

playerPaddle = PlayerPaddle(50, HEIGHT//2, PLAYER_SOUND)
enemyPaddle = EnemyPaddle(WIDTH - 50, HEIGHT//2, ENEMY_SOUND)
ball = Ball((0,0), (-1,1), WIDTH//2, HEIGHT//2)
score = Score()

def draw_background():
    SCREEN.fill(BG_COLOR)

def draw_divider(color, dot_size):
    for i in range(0, HEIGHT, dot_size*2):
        rect = pygame.Rect(WIDTH//2, i, dot_size, dot_size)
        pygame.draw.rect(SCREEN, color, rect)

def draw_board():
    score.draw(SCREEN, DIMENSIONS)
    draw_divider(BG_ELEM_COLOR, 7)
    ball.draw(SCREEN)
    playerPaddle.draw(SCREEN)
    enemyPaddle.draw(SCREEN)

def update_game():
    mouse_pos = pygame.mouse.get_pos()
    ball.update(DIMENSIONS, score)
    playerPaddle.update(mouse_pos, ball)
    enemyPaddle.update(ball)

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        draw_background()
        update_game()        
        draw_board()

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    run = False
                    break

        pygame.display.update()

if __name__ == "__main__":
    main()