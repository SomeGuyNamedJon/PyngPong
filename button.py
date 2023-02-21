import pygame
pygame.init()

class Button(pygame.sprite.Sprite):
    def __init__(self,string,font,font_color,color_on,color_off,position,size,function): #Add given properties as parameters
        pygame.sprite.Sprite.__init__(self)

        self.string = string
        self.color_on = color_on
        self.color_off = color_off
        self.position = position
        self.function = function

        self.image = pygame.Surface(size)
        self.image.fill(self.color_off)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.clicked = False

        self.text = font.render(string, True, font_color)

    def draw(self,screen):
        text_rect = self.rect.inflate(-50, -30)
        text_rect.center = self.rect.center
        screen.blit(self.image, self.rect)
        screen.blit(self.text, text_rect)

    def selected(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_pos)

    def update(self):
        self.rect.center = self.position
        if(self.selected()):
            self.image.fill(self.color_on)
        else:
            self.image.fill(self.color_off)

    def click(self):
        self.function()
