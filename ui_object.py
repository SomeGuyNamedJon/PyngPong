import os
import pygame
pygame.init()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("assets")

BASE_COLOR = (30, 30, 30)
FONT_COLOR = (255, 255, 255)
SELECTED_COLOR = KNOB_COLOR = (60, 60, 60)

HOVER_SOUND = pygame.mixer.Sound("pongblipf5.wav")
CLICK_SOUND = pygame.mixer.Sound("pongblipb3.wav")

class UI_Object(pygame.sprite.Sprite):
    def __init__(self, position, size):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.image = pygame.Surface(size)
        self.image.fill(BASE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def updatePosition(self, position):
        self.position = position

class Button(UI_Object):
    def __init__(self, label, font, position, size, function):
        UI_Object.__init__(self, position, size)
        self.label = label
        self.function = function
        self.clicked = False
        self.hover = False
        self.text = font.render(label, True, FONT_COLOR)

    def draw(self, screen):
        text_rect = self.rect.inflate(-50, -30)
        text_rect.center = self.rect.center
        screen.blit(self.image, self.rect)
        screen.blit(self.text, text_rect)

    def selected(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)

    def update(self):
        self.rect.center = self.position
        if(self.selected()):
            self.image.fill(SELECTED_COLOR)
            if not self.hover:
                HOVER_SOUND.play()
                self.hover = True
        else:
            self.image.fill(BASE_COLOR)
            self.hover = False
            self.clicked = False

    def click(self):
        CLICK_SOUND.play()
        self.function()

class Slider(UI_Object):
    def __init__(self, position, width, height, min_value, max_value):
        UI_Object.__init__(self, position, (width, height))
        self.min_value = min_value
        self.max_value = max_value
        self.value = min_value
        self.knob_image = pygame.Surface((height, height))
        self.knob_image.fill(KNOB_COLOR)
        self.knob_rect = self.knob_image.get_rect()
        self.knob_rect.left = self.rect.left
        self.knob_rect.centery = self.rect.centery
        self.font = pygame.font.Font("BitPap.ttf", height - 10)
        self.dragging = False

    def draw(self, screen):
        percentage = (self.value - self.min_value) / (self.max_value - self.min_value)
        knob_pos = (self.rect.left + int(percentage * self.rect.width), self.rect.centery)
        self.knob_rect.left = knob_pos[0]
        self.knob_rect.centery = knob_pos[1]
        self.knob_rect.clamp_ip(self.rect)

        screen.blit(self.image, self.rect)
        screen.blit(self.knob_image, self.knob_rect)

        label = self.font.render(str(self.value), True, FONT_COLOR)
        label_rect = label.get_rect(center=self.knob_rect.center)
        screen.blit(label, label_rect)

    def update(self, mouse_pos, event):
        self.rect.center = self.position
        if event.type == pygame.MOUSEBUTTONDOWN and self.knob_rect.collidepoint(mouse_pos):
            self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.knob_rect.centerx = min(max(mouse_pos[0], self.rect.left), self.rect.right)
            percentage = (self.knob_rect.centerx - self.rect.left) / self.rect.width
            self.value = int(self.min_value + percentage * (self.max_value - self.min_value))