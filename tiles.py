import pygame 

class Tile(pygame.sprite.Sprite):
    def __init_(self,pos,size):
        super().__init__.()
        self.image = pygame.Surface((size,size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)
        