import pygame

class Slider:
    def __init__(self, position, width, height, min_value, max_value):
        self.position = position
        self.width = width
        self.height = height
        self.min_value = min_value
        self.max_value = max_value
        self.value = min_value
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = position
        self.color = pygame.Color('black')
        self.knob_rect = pygame.Rect(0, 0, height, height)
        self.knob_rect.centerx = self.rect.left
        self.knob_rect.centery = self.rect.centery
        self.knob_color = pygame.Color('grey')
        self.font = pygame.font.Font(None, height)
        self.dragging = False

    def selected(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, self.knob_color, self.knob_rect)

        label = self.font.render(str(self.value), True, pygame.Color('black'))
        label_rect = label.get_rect(center=self.knob_rect.center)
        surface.blit(label, label_rect)

    def update(self, mouse_pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.knob_rect.collidepoint(mouse_pos):
            self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.knob_rect.centerx = min(max(mouse_pos[0], self.rect.left), self.rect.right)
            percentage = (self.knob_rect.centerx - self.rect.left) / self.rect.width
            self.value = int(self.min_value + percentage * (self.max_value - self.min_value))