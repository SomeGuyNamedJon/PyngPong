import pygame
from typing import List
from ui_object import Button, Slider, Dropdown

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
        self.settings_sliders = self.create_sliders([(0, 0), (0, 0)])
        self.settings_buttons = self.create_buttons(["Back"], [3])
        self.settings_dropdowns = self.create_dropdowns([(0, 0), (0, 0)], [("Hello", "World", ":^)"), ("Is", "This", "A", "Dream?")])

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
            sliders.append(Slider(position, 250, 50, 1, 30))
        return sliders
    
    def create_dropdowns(self, positions: List[tuple], options: List[tuple]):
        dropdowns = []
        for (position, option) in zip(positions, options):
            dropdowns.append(Dropdown(position, (250, 50), option))
        return dropdowns

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
            slider.updatePosition((center_x + self.padding if slider == self.settings_sliders[1] else center_x - self.padding, center_y - self.padding))

        for dropdown in self.settings_dropdowns:
            dropdown.updatePosition((center_x + self.padding if dropdown == self.settings_dropdowns[1] else center_x - self.padding, center_y - self.padding//2))