import pygame
pygame.init()

START_SCORE = (0, 0)

class Score():
    def __init__(self):
        (self.player, self.enemy) = START_SCORE
        self.font = pygame.font.Font("BitPap.ttf", 500)

    def draw(self, screen, dimensions, color):
        (width, height) = dimensions
        playerScore = self.font.render(str(self.player), True, color)
        enemyScore = self.font.render(str(self.enemy), True, color)
        
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