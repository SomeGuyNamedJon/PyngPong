from button import Button
from slider import Slider
import pygame
pygame.init()

class MenuManager():
    def __init__(self, dimensions, font, functions):
        (width, height) = dimensions
        button_size = (450, 125)
        center_x = width // 2
        center_y = height // 2
        button_top = (center_x, center_y - 140)
        button_mid = (center_x, center_y)
        button_bottom = (center_x, center_y + 140)

        # Menu buttons
        (start, settings, menu, back) = functions
        self.play_button = Button("Play", font, button_top, button_size, start)
        self.settings_button = Button("Settings",  font, button_mid, button_size, settings)
        self.menu_button = Button("Main", font, button_top, button_size, menu)
        self.back_button = Button("Back", font, button_bottom, button_size, back)
        self.quit_button = Button("Quit", font, button_bottom, button_size, quit)

        # Settings sliders
        self.test_slider = Slider(button_top, 400, 40, 1, 30)

        self.menu_buttons = [self.play_button, self.settings_button, self.quit_button]
        self.settings_buttons = [self.back_button, self.test_slider]
        self.pause_buttons = [self.menu_button, self.settings_button, self.quit_button]

    def update(self, dimensions):
        (width, height) = dimensions
        center_x = width // 2
        center_y = height // 2
        button_top = (center_x, center_y - 140)
        button_mid = (center_x, center_y)
        button_bottom = (center_x, center_y + 140)

        self.play_button.updatePosition(button_top)
        self.settings_button.updatePosition(button_mid)
        self.menu_button.updatePosition(button_top)
        self.back_button.updatePosition(button_bottom)
        self.quit_button.updatePosition(button_bottom)

        self.menu_buttons = [self.play_button, self.settings_button, self.quit_button]
        self.settings_buttons = [self.back_button, self.test_slider]
        self.pause_buttons = [self.menu_button, self.settings_button, self.quit_button]