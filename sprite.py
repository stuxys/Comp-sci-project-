import pygame 

class Tile(pygame.sprite.sprite):
    def __init_(self,pos,size):
        super().__init__.()
        self.image = pygame.Surface((size,size))
        self.rect = self.image.get.rect(topleft = pos)
        