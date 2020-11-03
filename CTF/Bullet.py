import pygame
import pygame.locals
import time


class Bullets(pygame.sprite.Sprite):
    def __init__(self, SpawnX, SpawnY, Direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprites/Extra/Bullet.png')
        self.rect = self.image.get_rect()
        self.spawn = {'x': SpawnX, 'y': SpawnY}
        self.rect.x, self.rect.y = self.spawn['x'], self.spawn['y']
        self.direction = Direction

    def update(self):
        if self.direction == 0:
            self.rect.y -= 16
        elif self.direction == 1:
            self.rect.x += 16
        elif self.direction == 2:
            self.rect.y += 16
        elif self.direction == 3:
            self.rect.x -= 16

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class BlueBullets(Bullets):
    def __init__(self, SpawnX, SpawnY, Direction):
        Bullets.__init__(self, SpawnX, SpawnY, Direction)


class RedBullets(Bullets):
    def __init__(self, SpawnX, SpawnY, Direction):
        Bullets.__init__(self, SpawnX, SpawnY, Direction)
