import pygame
from button import Button
from game_manager import GameManager
from settings import Settings
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

### FONTS
BUTTON_FONT = pygame.font.Font("PingPong.otf", 120)
FONT = pygame.font.Font("BitPap.ttf", 500)

### GAME AND SETTINGS
setting = Settings("cpu", "cpu")
game = GameManager(setting, DIMENSIONS, FONT)

### BUTTON FUNCTIONS
def menu():
    global game
    global scene
    global prev_scene
    prev_scene = scene 
    scene = "main"
    pygame.mouse.set_visible(True)

    game = GameManager(setting, DIMENSIONS, FONT)

def back():
    global scene
    scene = prev_scene

def start():
    global scene
    scene = "play"
    pygame.mouse.set_visible(False)

def settings():
    global scene
    global prev_scene
    prev_scene = scene
    scene = "settings"
    pygame.mouse.set_visible(True)

def pause():
    global scene
    global prev_scene
    prev_scene = scene 
    scene = "pause"
    pygame.mouse.set_visible(True)

### BUTTONS
play_button = Button("Play", BUTTON_FONT, BUTTON_FONT_COLOR, BUTTON_COLOR, BUTTON_SELECTED, (BUTTON_X, BUTTON_TOP), BUTTON_SIZE, start)
settings_button = Button("Settings",  BUTTON_FONT, BUTTON_FONT_COLOR, BUTTON_COLOR, BUTTON_SELECTED, (BUTTON_X, BUTTON_MID), BUTTON_SIZE, settings)
quit_button = Button("Quit", BUTTON_FONT, BUTTON_FONT_COLOR, BUTTON_COLOR, BUTTON_SELECTED, (BUTTON_X, BUTTON_BOTTOM), BUTTON_SIZE, quit)
menu_button = Button("Main", BUTTON_FONT, BUTTON_FONT_COLOR, BUTTON_COLOR, BUTTON_SELECTED, (BUTTON_X, BUTTON_TOP), BUTTON_SIZE, menu)
back_button = Button("Back", BUTTON_FONT, BUTTON_FONT_COLOR, BUTTON_COLOR, BUTTON_SELECTED, (BUTTON_X, BUTTON_MID), BUTTON_SIZE, back)

menu_buttons = [play_button, settings_button, quit_button]
settings_buttons = [back_button, quit_button]
pause_buttons = [menu_button, settings_button, quit_button]

### DEFAULT SCENE - main, play, settings, pause
scene = "main"
prev_scene = scene

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
    game.score.draw(SCREEN, dimensions)
    draw_divider(BG_ELEM_COLOR, dimensions, 7)
    draw_speed(game.ball)
    game.ball.draw(SCREEN)
    game.paddle_a.draw(SCREEN)
    game.paddle_b.draw(SCREEN)

### UPDATE FUNCTIONS
def update_game(dimensions):
    game.ball.update(dimensions, SCREEN, game.score)
    game.paddle_a.update(game.ball, dimensions)
    game.paddle_b.update(game.ball, dimensions)

def update_buttons(button_list):
    for button in button_list:
        button.update()

### SCENES
def play(dimensions):
    update_game(dimensions)        
    draw_board(dimensions)

def main_menu(dimensions):
    draw_buttons(menu_buttons)
    update_buttons(menu_buttons)

def settings_menu(dimensions):    
    draw_buttons(settings_buttons)
    update_buttons(settings_buttons)

def pause_menu(dimensions):
    draw_board(dimensions)
    draw_buttons(pause_buttons)
    update_buttons(pause_buttons)

### MAIN LOOP
def main():
    buttons = menu_buttons
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
                case pygame.MOUSEBUTTONUP:
                    for button in buttons:
                        if button.selected() and event.button == 1:
                            button.click()
                case pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                            if scene == "pause":
                                start()
                            else:
                                pause()
        
        match(scene):
            case "main":
                main_menu(dimensions)
                buttons = menu_buttons
            case "settings":
                settings_menu(dimensions)
                buttons = settings_buttons
            case "pause":
                pause_menu(dimensions)
                buttons = pause_buttons
            case "play":
                play(dimensions)
            case _:
                run = False

        pygame.display.flip()

if __name__ == "__main__":
    main()