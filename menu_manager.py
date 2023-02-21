from button import Button
import pygame
pygame.init()

class MenuManager():
    def __init__(self, dimensions, font, functions):
        (width, height) = dimensions

        button_size = (450,125)
        button_top = height // 4
        button_mid = height // 2
        button_bottom = height * 3 // 4
        button_x = width // 2
        
        (start, settings, menu, back) = functions
        play_button = Button("Play", font, (button_x, button_top), button_size, start)
        settings_button = Button("Settings",  font, (button_x, button_mid), button_size, settings)
        menu_button = Button("Main", font, (button_x, button_top), button_size, menu)
        back_button = Button("Back", font, (button_x, button_mid), button_size, back)
        quit_button = Button("Quit", font, (button_x, button_bottom), button_size, quit)

        self.menu_buttons = [play_button, settings_button, quit_button]
        self.settings_buttons = [back_button, quit_button]
        self.pause_buttons = [menu_button, settings_button, quit_button]