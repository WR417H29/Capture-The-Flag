import pygame.locals


class Arrow(pygame.sprite.Sprite):
    def __init__(self, direction):
        pygame.sprite.Sprite.__init__()
        self.image = pygame.image.load('Sprites/Extra/Arrow.png')
        self.rect = self.image.get_rect()
