import pygame
pygame.init()

START_SCORE = (0, 0)
GOAL_COLOR = (150, 255, 170)

def scaleText(text_surface, dimensions):
    (width, height) = dimensions
    print(text_surface)
    if text_surface.get_width() < width:
        width = text_surface.get_width()
    text_surface = pygame.transform.scale(text_surface, (width, height))
    return text_surface

def centerRect(text, position):
    text_rect = text.get_rect()
    text_rect.center = position
    return text_rect

class Score():
    def __init__(self, color, font):
        self.font = font
        self.color = color
        (self.a_score, self.b_score) = START_SCORE
        self.a_text = font.render(str(self.a_score), True, color)
        self.b_text = font.render(str(self.b_score), True, color)

    def draw(self, screen, dimensions):
        (width, height) = dimensions
        self.a_text = scaleText(self.a_text, (width // 3 , height * 2 // 3))
        self.b_text = scaleText(self.b_text, (width // 3, height * 2 // 3))
        a_rect = centerRect(self.a_text, ((width // 4), (height // 2) + 50))
        b_rect = centerRect(self.b_text, (width - (width//4), (height // 2 + 50)))
        screen.blit(self.a_text, a_rect)
        screen.blit(self.b_text, b_rect)

    def score(self, player):
        match(player):
            case 'A':
                self.a_score += 1
                text = str(self.a_score)
                self.a_text = self.font.render(text, True, self.color)
            case 'B':
                self.b_score += 1
                text = str(self.b_score)
                self.b_text = self.font.render(text, True, self.color)
        