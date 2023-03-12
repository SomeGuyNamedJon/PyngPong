import pygame

BASE_COLOR = (30, 30, 30)
FONT_COLOR = (255, 255, 255)
KNOB_COLOR = (60, 60, 60)

class Slider:
    def __init__(self, position, width, height, min_value, max_value):
        self.position = position
        self.width = width
        self.height = height
        self.min_value = min_value
        self.max_value = max_value
        self.value = min_value
        
        self.image = pygame.Surface((width, height))
        self.image.fill(BASE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = position
        
        self.knob_image = pygame.Surface((height, height))
        self.knob_image.fill(KNOB_COLOR)
        self.knob_rect = self.knob_image.get_rect()
        self.knob_rect.left = self.rect.left
        self.knob_rect.centery = self.rect.centery
        
        self.font = pygame.font.Font("BitPap.ttf", height - 10)
        self.dragging = False

    def draw(self, screen):
        # Update knob position based on current value
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

    def updatePosition(self, position):
        self.position = position

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