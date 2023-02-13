import pygame
pygame.init()

START_SCORE = (0, 0)
TEXT_COLOR = (255, 255, 255)

class Score():
    def __init__(self):
        (self.player, self.enemy) = START_SCORE
        self.font = pygame.font.SysFont('freesanbold.ttf', 100)
    
    def draw(self, screen, dimensions):
        (width, _) = dimensions
        playerScore = self.font.render(str(self.player), True, TEXT_COLOR)
        enemyScore = self.font.render(str(self.enemy), True, TEXT_COLOR)
        screen.blit(playerScore, ((width // 4) - 25, 50))
        screen.blit(enemyScore, ((width - (width // 4)) - 25, 50))

    def playerPoint(self):
        self.player += 1

    def enemyPoint(self):
        self.enemy += 1