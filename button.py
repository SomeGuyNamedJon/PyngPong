import os
import pygame
pygame.init()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir("assets")

BASE_COLOR = (30, 30, 30)
FONT_COLOR = (255, 255, 255)
SELECTED_COLOR = (60, 60, 60)

HOVER_SOUND = pygame.mixer.Sound("pongblipf5.wav")
CLICK_SOUND = pygame.mixer.Sound("pongblipb3.wav")

class Button(pygame.sprite.Sprite):
    def __init__(self,string,font,position,size,function): #Add given properties as parameters
        pygame.sprite.Sprite.__init__(self)

        self.string = string
        self.position = position
        self.function = function

        self.image = pygame.Surface(size)
        self.image.fill(BASE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.clicked = False
        self.hover = False

        self.text = font.render(string, True, FONT_COLOR)

    def draw(self,screen):
        text_rect = self.rect.inflate(-50, -30)
        text_rect.center = self.rect.center
        screen.blit(self.image, self.rect)
        screen.blit(self.text, text_rect)

    def selected(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)

    def updatePosition(self, position):
        self.position = position

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
