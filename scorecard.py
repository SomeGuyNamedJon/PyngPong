import pygame
pygame.init()

FLASH_RATE = 100
FLASH_TIME = 500
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
        self.last_flash = 0
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
        screen.blit(self.text, rect)
        self.flashGoal()

    def goal(self):
        self.goal_time = pygame.time.get_ticks()
        self.goal_scored = True
        self.score += 1
        self.text = self.font.render(str(self.score), True, GOAL_COLOR)
        
    def flashGoal(self):
        current_time = pygame.time.get_ticks()
        elasped_time = current_time - self.goal_time
        flash_time = current_time - self.last_flash

        if(elasped_time >= FLASH_TIME):
            self.text = self.font.render(str(self.score), True, self.color)
            self.goal_scored = False
        elif(self.goal_scored and flash_time < FLASH_RATE):
            self.text = self.font.render(str(self.score), True, self.color)
        elif(self.goal_scored):
            self.text = self.font.render(str(self.score), True, GOAL_COLOR)
            self.last_flash = current_time



