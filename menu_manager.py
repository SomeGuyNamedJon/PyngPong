import pygame
from typing import List
from ui_object import Button, Slider

pygame.init()

class MenuManager():
    def __init__(self, font, functions):
        self.font = font
        self.functions = functions
        self.padding = 140
        self.button_size = (450, 125)
        self.origin = (0, 0)

        self.menu_buttons = self.create_buttons(["Play", "Settings", "Quit"], [0, 1, 4])
        self.pause_buttons = self.create_buttons(["Main", "Settings", "Quit"], [2, 1, 4])
        self.settings_sliders = self.create_sliders([(self.padding, -self.padding), (-self.padding, -self.padding)])
        self.settings_buttons = self.create_buttons(["Back"], [3])

    def create_buttons(self, labels: List[str], actions: List[int]):
        buttons = []
        center_x = pygame.display.Info().current_w // 2
        center_y = pygame.display.Info().current_h // 2
        button_top = (center_x, center_y - self.padding)
        button_mid = (center_x, center_y)
        button_bottom = (center_x, center_y + self.padding)

        for label, action in zip(labels, actions):
            if action == 0:
                position = button_top
            elif action == 1:
                position = button_mid
            else:
                position = button_bottom
            buttons.append(Button(label, self.font, self.origin, self.button_size, self.functions[action]))
            buttons[-1].updatePosition(position)
        return buttons

    def create_sliders(self, positions: List[tuple]):
        sliders = []
        for position in positions:
            sliders.append(Slider((0, 0), 250, 50, 1, 30))
            sliders[-1].updatePosition((pygame.display.Info().current_w // 2 + position[0], pygame.display.Info().current_h // 2 + position[1]))
        return sliders

    def update(self):
        center_x = pygame.display.Info().current_w // 2
        center_y = pygame.display.Info().current_h // 2
        button_top = (center_x, center_y - self.padding)
        button_mid = (center_x, center_y)
        button_bottom = (center_x, center_y + self.padding)

        for button in (self.menu_buttons + self.pause_buttons + self.settings_buttons):
            if(button.label == "Main" or button.label == "Play"):
                button.updatePosition(button_top)
            elif(button.label == "Settings"):
                button.updatePosition(button_mid)
            else:
                button.updatePosition(button_bottom)

        for slider in self.settings_sliders:
            slider.updatePosition((center_x + self.padding if slider == self.settings_sliders[0] else center_x - self.padding, center_y - self.padding))
