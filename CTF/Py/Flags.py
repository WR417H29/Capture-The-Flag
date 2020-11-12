import pygame.locals


class Flag(pygame.sprite.Sprite):
    def __init__(self, img, spawnX, spawnY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.spawn = {'x': spawnX, 'y': spawnY}
        self.rect.x, self.rect.y = self.spawn['x'], self.spawn['y']  # SETTING THE SPAWN

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # DRAWING THE FLAGS TO THE SCREEN


class BlueFlag(Flag):
    def __init__(self):
        Flag.__init__(self, 'CTF/Sprites/Flags/BlueFlag.png', 0, 0)


class RedFlag(Flag):
    def __init__(self):
        Flag.__init__(self, 'CTF/Sprites/Flags/RedFlag.png', 768, 768)
