import pygame
from button import Button
from slider import Slider
from game_manager import GameManager
from menu_manager import MenuManager
from settings import Settings
import os

# start in assets folder and initialize pygame
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("assets")
pygame.init()
pygame.display.set_caption("PλngPong")

### DEFAULT WINDOW
BG_COLOR = (50, 50, 50)
WIDTH, HEIGHT = 960, 540
DIMENSIONS = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(DIMENSIONS)
FPS = 60

### FONTS
BUTTON_FONT = pygame.font.Font("PingPong.otf", 120)
FONT = pygame.font.Font("BitPap.ttf", 500)

### GAME AND SETTINGS
setting = Settings("player", "cpu")
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

### MENUS
menus = MenuManager(DIMENSIONS, BUTTON_FONT, (start, settings, menu, back))

### DEFAULT SCENE - main, play, settings, pause
scene = "main"
prev_scene = scene

### DRAW FUNCTIONS
def draw_background():
    SCREEN.fill(BG_COLOR)

def draw_game(dimensions):
    game.draw(SCREEN, dimensions)

def draw_buttons(button_list):
    for button in button_list:
        button.draw(SCREEN)

### UPDATE FUNCTIONS
def update_game(dimensions):
    game.update(dimensions, SCREEN)

def update_buttons(button_list, dimensions, mouse_pos=0, event=0):
    menus.update(dimensions)
    for button in button_list:
        if isinstance(button, Slider):
            button.update(mouse_pos, event)
        else:
            button.update()

### SCENES
def play(dimensions):
    update_game(dimensions)        
    draw_game(dimensions)

def main_menu(dimensions):
    draw_buttons(menus.menu_buttons)
    update_buttons(menus.menu_buttons, dimensions)

def settings_menu(dimensions, mouse_pos, event):    
    draw_buttons(menus.settings_buttons)
    update_buttons(menus.settings_buttons, dimensions, mouse_pos, event)

def pause_menu(dimensions):
    draw_game(dimensions)
    draw_buttons(menus.pause_buttons)
    update_buttons(menus.pause_buttons, dimensions)

### MAIN LOOP
def main():
    buttons = menus.menu_buttons
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
                        if isinstance(button, Button):
                            if button.selected() and event.button == 1:
                                button.click()
                case pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                            if scene == "pause":
                                start()
                            elif scene == "play":
                                pause()
        
            match(scene):
                case "main":
                    main_menu(dimensions)
                    buttons = menus.menu_buttons
                case "settings":
                    settings_menu(dimensions, pygame.mouse.get_pos(), event)
                    buttons = menus.settings_buttons
                case "pause":
                    pause_menu(dimensions)
                    buttons = menus.pause_buttons
                case "play":
                    play(dimensions)
                case _:
                    run = False

            pygame.display.flip()

if __name__ == "__main__":
    main()