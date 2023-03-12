from button import Button
from slider import Slider
import pygame
pygame.init()

class MenuManager():
    def __init__(self, dimensions, font, functions):
        self.padding = 140
        button_size = (450, 125)
        
        (width, height) = dimensions
        center_x = width // 2
        center_y = height // 2
        button_top = (center_x, center_y - self.padding)
        button_mid = (center_x, center_y)
        button_bottom = (center_x, center_y + self.padding)
        slider_top_left = (center_x - self.padding, center_y - self.padding)
        slider_top_right = (center_x + self.padding, center_y - self.padding)

        # Menu buttons
        (start, settings, menu, back) = functions
        self.play_button = Button("Play", font, button_top, button_size, start)
        self.settings_button = Button("Settings",  font, button_mid, button_size, settings)
        self.menu_button = Button("Main", font, button_top, button_size, menu)
        self.back_button = Button("Back", font, button_bottom, button_size, back)
        self.quit_button = Button("Quit", font, button_bottom, button_size, quit)

        # Settings sliders
        self.test_slider = Slider(slider_top_right, 250, 50, 1, 30)
        self.test_slider2 = Slider(slider_top_left, 250, 50, 1, 30)

        self.menu_buttons = [self.play_button, self.settings_button, self.quit_button]
        self.settings_buttons = [self.back_button]
        self.settings_sliders = [self.test_slider, self.test_slider2]
        self.pause_buttons = [self.menu_button, self.settings_button, self.quit_button]

    def update(self, dimensions):
        (width, height) = dimensions
        center_x = width // 2
        center_y = height // 2
        button_top = (center_x, center_y - self.padding)
        button_mid = (center_x, center_y)
        button_bottom = (center_x, center_y + self.padding)
        slider_top_left = (center_x - self.padding, center_y - self.padding)
        slider_top_right = (center_x + self.padding, center_y - self.padding)

        self.play_button.updatePosition(button_top)
        self.settings_button.updatePosition(button_mid)
        self.menu_button.updatePosition(button_top)
        self.back_button.updatePosition(button_bottom)
        self.quit_button.updatePosition(button_bottom)

        self.test_slider.updatePosition(slider_top_right)
        self.test_slider2.updatePosition(slider_top_left)