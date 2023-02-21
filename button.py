import pygame
pygame.init()

class Button(pygame.sprite.Sprite):
    def __init__(self,color_on,color_off,sound,x,y,size,function): #Add given properties as parameters
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface(size)
        self.image.fill(self.color_off)
        
        self.color_on = color_on
        self.color_off = color_off
        self.position = (x,y)
        self.sound = sound
        self.function = function

        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.clicked = False

    def draw(self,screen):
        pygame.draw.rect(screen, self.color_off, self.rect)
        screen.blit(self.image, self.rect)

    def selected(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def update(self, screen):
        self.rect.center = self.position

    def click(self):
        self.function()
