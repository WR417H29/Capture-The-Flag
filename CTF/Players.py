import time

import pygame.locals


class Player(pygame.sprite.Sprite):
    def __init__(self, img, fwd, bwd, cw, ccw, spawnX, spawnY, direction, hasFlag, lives):
        pygame.sprite.Sprite.__init__(self)  # INITIALISING PARENT CLASS
        self.image = pygame.image.load(img)  # LOADING SPRITE
        self.rect = self.image.get_rect()  # GETTING THE SIZE OF THE IMAGE
        self.direction = direction  # DECLARING THE DIRECTION OF THE PLAYER
        self.controls = {'forward': fwd, 'backward': bwd, 'clockwise': cw,'counterclockwise': ccw}  # DECLARING THE CONTROLS
        self.spawn = {'x': spawnX, 'y': spawnY}  # SETTING SPAWN VARIABLES
        self.rect.x, self.rect.y = spawnX, spawnY  # SETTING THE SPAWN
        self.hasFlag = hasFlag
        self.lives = lives

    def update(self, keysPressed):
        # ~ MOVEMENT ~ #
        self.rect.x += (keysPressed[self.controls['forward']]) * (8 if self.direction == 1 else (-8 if self.direction == 3 else 0))
        self.rect.x -= (keysPressed[self.controls['backward']]) * (8 if self.direction == 1 else (-8 if self.direction == 3 else 0))

        self.rect.y += (keysPressed[self.controls['forward']]) * (8 if self.direction == 2 else (-8 if self.direction == 0 else 0))
        self.rect.y -= (keysPressed[self.controls['backward']]) * (8 if self.direction == 2 else (-8 if self.direction == 0 else 0))

        # ~ DIRECTION CHANGING ~ #

        if keysPressed[self.controls['clockwise']]:
            self.direction += 1
            if self.direction > 3:
                self.direction = 0

        if keysPressed[self.controls['counterclockwise']]:
            self.direction -= 1
            if self.direction < 0:
                self.direction = 3

        # ~ BORDER CREATION ~ #
        self.rect.left = min(max(0, self.rect.left), 800)
        self.rect.right = min(max(0, self.rect.right), 800)
        self.rect.top = min(max(0, self.rect.top), 800)
        self.rect.bottom = min(max(0, self.rect.bottom), 800)

        time.sleep(0.05)

    def setImage(self, image):
        self.image = pygame.image.load(image)

    def getRectX(self):
        return self.rect.x

    def getCenterX(self):
        return self.rect.centerx

    def getRectY(self):
        return self.rect.y

    def getCenterY(self):
        return self.rect.centery

    def getHasflag(self):
        return self.hasFlag

    def getDirection(self):
        return self.direction

    def getLives(self):
        return self.lives

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # DRAWING THE PLAYERS TO THE SCREEN


class BluePlayer(Player):
    def __init__(self, img, spawnX, spawnY, hasFlag, direction, lives):
        Player.__init__(self, img, pygame.locals.K_w, pygame.locals.K_s, pygame.locals.K_d, pygame.locals.K_a, spawnX, spawnY, direction, hasFlag, lives)  # INITIALISING THE PARENT CLASS


class RedPlayer(Player):
    def __init__(self, img, spawnX, spawnY, hasFlag, direction, lives):
        Player.__init__(self, img, pygame.locals.K_i, pygame.locals.K_k, pygame.locals.K_l, pygame.locals.K_j, spawnX, spawnY, direction, hasFlag, lives)  # INITIALISING THE PARENT CLASS
