import random as r
import pygame
from paddle import PaddlePlayer, PaddleAI
from ball import Ball
from scorecard import ScoreCard
from button import Button
import os

# start in assets folder and initialize pygame
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("assets")
pygame.init()
pygame.display.set_caption("PλngPong")

### COLORS
SPEED_COLOR_1 = (165, 165, 80)
SPEED_COLOR_2 = (185, 125, 70)
SPEED_COLOR_3 = (205, 100, 60)
SPEED_COLOR_4 = (235, 80, 50)
SPEED_COLOR_MAX = (255, 50, 30)
BG_COLOR = (50, 50, 50)
BG_ELEM_COLOR = (70, 70, 70)
BUTTON_COLOR = (30, 30, 30)
BUTTON_FONT_COLOR = (255, 255, 255)
BUTTON_SELECTED = (60, 60, 60)

### DEFAULT WINDOW
WIDTH, HEIGHT = 960, 540
DIMENSIONS = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(DIMENSIONS)
FPS = 60

### BUTTON SIZE AND POSITION
BUTTON_SIZE = (450,125)
BUTTON_TOP = HEIGHT // 4
BUTTON_MID = HEIGHT // 2
BUTTON_BOTTOM = HEIGHT * 3 // 4
BUTTON_X = WIDTH // 2

### SOUNDS AND FONTS
PADDLE_A_SOUND = pygame.mixer.Sound("pongblipc5.wav")
PADDLE_B_SOUND = pygame.mixer.Sound("pongblipf5.wav")
BALL_SOUND = pygame.mixer.Sound("pongblipb3.wav")
GOAL_SOUND = pygame.mixer.Sound("goal.wav")
FONT = pygame.font.Font("BitPap.ttf", 500)
BUTTON_FONT = pygame.font.Font("PingPong.otf", 120)

### BALL START
BX = r.uniform(-2.5, 2.5)
BY = r.uniform(-1.0, 1.0)
BALL_DIRECTION = (1 if BX == 0 else BX, 1 if BY == 0 else BY)

### GAME OBJECTS
Player1_Paddle = PaddlePlayer(50, HEIGHT//2, PADDLE_A_SOUND)
Player2_Paddle = PaddlePlayer(WIDTH - 50, HEIGHT//2, PADDLE_B_SOUND)
CPU1_Paddle = PaddleAI(50, HEIGHT//2, PADDLE_A_SOUND)
CPU2_Paddle = PaddleAI(WIDTH - 50, HEIGHT//2, PADDLE_B_SOUND)
ball = Ball((0,0), BALL_DIRECTION, WIDTH//2, HEIGHT//2, BALL_SOUND)
score = ScoreCard(BG_ELEM_COLOR, FONT, GOAL_SOUND)

### BUTTON FUNCTIONS
def menu():
    global scene
    scene = "main"

def play():
    global scene 
    scene = "play"

def settings():
    global scene
    scene = "settings"

### BUTTONS
play_button = Button("Play", BUTTON_FONT, BUTTON_FONT_COLOR, BUTTON_COLOR, BUTTON_SELECTED, (BUTTON_X, BUTTON_TOP), BUTTON_SIZE, play)
settings_button = Button("Settings",  BUTTON_FONT, BUTTON_FONT_COLOR, BUTTON_COLOR, BUTTON_SELECTED, (BUTTON_X, BUTTON_MID), BUTTON_SIZE, settings)
quit_button = Button("Quit", BUTTON_FONT, BUTTON_FONT_COLOR, BUTTON_COLOR, BUTTON_SELECTED, (BUTTON_X, BUTTON_BOTTOM), BUTTON_SIZE, quit)
menu_buttons = [play_button, settings_button, quit_button]

### DEFAULT SCENE - main, play, settings, pause
scene = "main"

### DRAW FUNCTIONS
def draw_background():
    SCREEN.fill(BG_COLOR)

def draw_buttons(button_list):
    for button in button_list:
        button.draw(SCREEN)

def draw_divider(color, dimensions, dot_size):
    (width, height) = dimensions
    for i in range(0, height, dot_size*2):
        rect = pygame.Rect(width//2, i, dot_size, dot_size)
        pygame.draw.rect(SCREEN, color, rect)

def draw_speed(ball):
    string = '{0:.2f}'.format(ball.speed)
    color = BG_ELEM_COLOR
    if(ball.speed > 9):
        color = SPEED_COLOR_1
    if(ball.speed > 12):
        color = SPEED_COLOR_2
    if(ball.speed > 18):
        color = SPEED_COLOR_3
    if(ball.speed > 24):
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
    Player1_Paddle.draw(SCREEN)
    CPU2_Paddle.draw(SCREEN)

### UPDATE FUNCTIONS
def update_game(dimensions):
    ball.update(dimensions, SCREEN, score)
    Player1_Paddle.update(ball, dimensions)
    CPU2_Paddle.update(ball, dimensions)

def update_buttons(button_list):
    for button in button_list:
        button.update()

### SCENES
def play(dimensions):
    pygame.mouse.set_visible(False)
    update_game(dimensions)        
    draw_board(dimensions)

def main_menu(dimensions):
    draw_buttons(menu_buttons)
    update_buttons(menu_buttons)

def settings(dimensions):
    pass

def pause(dimensions):
    pass

### MAIN LOOP
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        draw_background()
        dimensions = (SCREEN.get_width(), SCREEN.get_height())

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    run = False
                    break
                case pygame.MOUSEBUTTONUP:
                    for button in menu_buttons:
                        if button.selected():
                            button.click()
        
        match(scene):
            case "main":
                main_menu(dimensions)
            case "settings":
                settings(dimensions)
            case "pause":
                pause(dimensions)
            case "play":
                play(dimensions)
            case _:
                run = False

        pygame.display.flip()

if __name__ == "__main__":
    main()