import time
import pygame
from paddle import PlayerPaddle, EnemyPaddle
from ball import Ball

pygame.init()
pygame.display.set_caption("Pλng")

BG_COLOR = (50, 50, 50)
WIDTH, HEIGHT = 960, 540
DIMENSIONS = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(DIMENSIONS)
FPS = 60

playerPaddle = PlayerPaddle(50, HEIGHT//2)
enemyPaddle = EnemyPaddle(WIDTH - 50, HEIGHT//2)
ball = Ball(5, (-1,1), WIDTH//2, HEIGHT//2) 

def draw_background():
    SCREEN.fill(BG_COLOR)

def draw_board():
    playerPaddle.draw(SCREEN)
    enemyPaddle.draw(SCREEN)
    ball.draw(SCREEN)

def update_game():
    mouse_pos = pygame.mouse.get_pos()
    ball.update(DIMENSIONS)
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