import math
import pygame
pygame.init()

FLASH_RATE = 200
FLASH_TIME = 1000
GOAL_COLOR = (100, 155, 100)

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
        self.score = 0
        self.goal_time = 0
        self.goal_scored = False
        self.name = name
        self.font = font
        self.color = color
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
        self.flashGoal()
        screen.blit(self.text, rect)

    def goal(self):
        self.goal_time = pygame.time.get_ticks()
        self.goal_scored = True
        self.score += 1
        self.text = self.font.render(str(self.score), True, GOAL_COLOR)
        
    def flashGoal(self):
        current_time = pygame.time.get_ticks()
        elasped_time = current_time - self.goal_time
        (width, height) = text_size = self.text.get_size()

        if(self.goal_scored and elasped_time < FLASH_TIME):
            if(math.ceil(elasped_time/FLASH_RATE) % 2 == 1):
                self.text = self.font.render(str(self.score), True, GOAL_COLOR)
                text_size = (width + 50, height + 50)
            else:
                self.text = self.font.render(str(self.score), True, self.color)
        else:
            self.text = self.font.render(str(self.score), True, self.color)
            self.goal_scored = False

        self.text = scaleText(self.text, text_size)



