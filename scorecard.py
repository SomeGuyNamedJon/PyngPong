import pygame
pygame.init()

GOAL_COLOR = (150, 255, 170)

def scaleText(text_surface, dimensions):
    (width, height) = dimensions
    if text_surface.get_width() < width:
        width = text_surface.get_width()
    text_surface = pygame.transform.scale(text_surface, (width, height))
    return text_surface

def centerRect(text, position):
    text_rect = text.get_rect()
    text_rect.center = position
    return text_rect

class ScoreCard():
    def __init__(self, color, font):
        self.a = Score(color, font, 'A')
        self.b = Score(color, font, 'B')

    def draw(self, screen, dimensions):
        self.a.draw(screen, dimensions)
        self.b.draw(screen, dimensions)

    def score(self, name):
        match(name):
            case 'A':
                self.a.goal()
            case 'B':
                self.b.goal()

class Score():
    def __init__(self, color, font, name):
        self.name = name
        self.font = font
        self.color = color
        self.base_color = color
        self.score = 0
        self.text = font.render(str(self.score), True, color)

    def draw(self, screen, dimensions):
        (width, height) = dimensions
        new_scale = (width // 3, height * 2 // 3)
        match(self.name):
            case 'A':
                new_center =  ((width // 4), (height // 2) + 50)
            case 'B':        
                new_center = (width - (width//4), (height // 2 + 50))
        
        self.text = scaleText(self.text, new_scale)
        rect = centerRect(self.text, new_center)
        screen.blit(self.text, rect)

    def goal(self):
        self.score += 1
        text = str(self.score)
        self.text = self.font.render(text, True, self.color)
        