import pygame
import pygame.locals


class Bullets(pygame.sprite.Sprite):
    def __init__(self, Shoot, SpawnX, SpawnY, Direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprites/Extra/Bullet.png')
        self.rect = self.image.get_rect()
        self.shootKey = Shoot
        self.spawn = {'x': SpawnX, 'y': SpawnY}
        self.rect.x, self.rect.y = self.spawn['x'], self.spawn['y']
        self.direction = Direction

    def update(self, keysPressed):
        self.rect.x = self.spawn['x']
        self.rect.y = self.spawn['y']
        if keysPressed == pygame.locals.K_j:
            self.rect.x, self.rect.y = 400, 400

    def getShootKey(self):
        return self.shootKey

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class BlueBullets(Bullets):
    def __init__(self, SpawnX, SpawnY, Direction):
        Bullets.__init__(self, pygame.locals.K_q, SpawnX, SpawnY, Direction)


class RedBullets(Bullets):
    def __init__(self, SpawnX, SpawnY, Direction):
        Bullets.__init__(self, pygame.locals.K_BACKSLASH, SpawnX, SpawnY, Direction)
