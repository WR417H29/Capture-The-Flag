import pygame.locals


class HomeBase(pygame.sprite.Sprite):
    def __init__(self, img, spawnX, spawnY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.spawn = {'x': spawnX, 'y': spawnY}
        self.rect.x, self.rect.y = self.spawn['x'], self.spawn['y']  # SETTING THE SPAWN

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # DRAWING THE HOMEBASES TO THE SCREEN


class BlueHomeBase(HomeBase):
    def __init__(self):
        HomeBase.__init__(self, 'CTF/Sprites/HomeBases/BlueHomeBase.png', 0, 0)


class RedHomeBase(HomeBase):
    def __init__(self):
        HomeBase.__init__(self, 'CTF/Sprites/HomeBases/RedHomeBase.png', 736, 736)
