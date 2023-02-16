import pygame
pygame.init()

START_SCORE = (0, 0)

class Score():
    def __init__(self):
        (self.player, self.enemy) = START_SCORE
        self.font = pygame.font.Font("BitPap.ttf", 500)

    def scaledText(self, text, color, dimensions):
        (width, height) = dimensions
        text_surface = self.font.render(str(text), True, color)
        if text_surface.get_width() < width:
            width = text_surface.get_width()
        text_surface = pygame.transform.scale(text_surface, (width, height))
        return text_surface


    def draw(self, screen, dimensions, color):
        (width, height) = dimensions
        playerScore = self.scaledText(self.player, color, (width // 3 , height * 2 // 3))
        enemyScore = self.scaledText(self.enemy, color, (width // 3, height * 2 // 3))
        
        p_text = playerScore.get_rect()
        e_text = enemyScore.get_rect()
        p_text.center = ((width // 4), (height // 2) + 50)
        e_text.center = (width - (width//4), (height // 2) + 50)

        screen.blit(playerScore, p_text)
        screen.blit(enemyScore, e_text)

    def playerPoint(self):
        self.player += 1

    def enemyPoint(self):
        self.enemy += 1