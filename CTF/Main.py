import time

import pygame
import pygame.locals


class Player(pygame.sprite.Sprite):
    def __init__(self, img, fwd, bwd, cw, ccw, spawnX, spawnY, direction, hasFlag):
        pygame.sprite.Sprite.__init__(self)  # initialising parent class
        self.image = pygame.image.load(img)  # loading sprite
        self.rect = self.image.get_rect()  # getting the size of the image
        self.direction = direction  # declaring the direction of the player
        self.controls = {'forward': fwd, 'backward': bwd, 'clockwise': cw,
                         'counterclockwise': ccw}  # declaring the controls
        self.spawn = {'x': spawnX, 'y': spawnY}  # setting spawn variables
        self.rect.x, self.rect.y = self.spawn['x'], self.spawn['y']  # setting the spawn
        self.hasFlag = hasFlag

    def update(self):
        # ~ Movement ~ #
        self.rect.x += (keysPressed[self.controls['forward']]) * (
            8 if self.direction == 1 else (-8 if self.direction == 3 else 0))
        self.rect.x -= (keysPressed[self.controls['backward']]) * (
            8 if self.direction == 1 else (-8 if self.direction == 3 else 0))

        self.rect.y += (keysPressed[self.controls['forward']]) * (
            8 if self.direction == 2 else (-8 if self.direction == 0 else 0))
        self.rect.y -= (keysPressed[self.controls['backward']]) * (
            8 if self.direction == 2 else (-8 if self.direction == 0 else 0))

        # ~ Direction Changing ~ #

        if keysPressed[self.controls['clockwise']]:
            self.direction += 1
            if self.direction > 3:
                self.direction = 0

        if keysPressed[self.controls['counterclockwise']]:
            self.direction -= 1
            if self.direction < 0:
                self.direction = 3

        # ~ Border Creation ~ #
        self.rect.left = min(max(0, self.rect.left), 800)
        self.rect.right = min(max(0, self.rect.right), 800)
        self.rect.top = min(max(0, self.rect.top), 800)
        self.rect.bottom = min(max(0, self.rect.bottom), 800)

        time.sleep(0.05)

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # drawing the players to the screen

    def getRectX(self):
        return self.rect.x

    def getRectY(self):
        return self.rect.y

    def getHasflag(self):
        return self.hasFlag


class BluePlayer(Player):
    def __init__(self, img, spawnX, spawnY, hasFlag):
        Player.__init__(self, img,
                        pygame.locals.K_w, pygame.locals.K_s,
                        pygame.locals.K_d, pygame.locals.K_a, spawnX, spawnY, 1,
                        hasFlag)  # initialising the parent class


class RedPlayer(Player):
    def __init__(self, img, spawnX, spawnY, hasFlag):
        Player.__init__(self, img,
                        pygame.locals.K_UP, pygame.locals.K_DOWN,
                        pygame.locals.K_RIGHT, pygame.locals.K_LEFT, spawnX, spawnY, 3,
                        hasFlag)  # initialising the parent class


class Flag(pygame.sprite.Sprite):
    def __init__(self, img, spawnX, spawnY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.spawn = {'x': spawnX, 'y': spawnY}
        self.rect.x, self.rect.y = self.spawn['x'], self.spawn['y']  # setting the spawn

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # drawing the flags to the screen


class BlueFlag(Flag):
    def __init__(self):
        Flag.__init__(self, 'Sprites/BlueFlag.png', 0, 0)


class RedFlag(Flag):
    def __init__(self):
        Flag.__init__(self, 'Sprites/RedFlag.png', 768, 768)


class HomeBase(pygame.sprite.Sprite):
    def __init__(self, spawnX, spawnY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprites/HomeBase.png')
        self.rect = self.image.get_rect()
        self.spawn = {'x': spawnX, 'y': spawnY}
        self.rect.x, self.rect.y = self.spawn['x'], self.spawn['y']  # setting the spawn

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # drawing the homebases to the screen


class BlueHomeBase(HomeBase):
    def __init__(self):
        HomeBase.__init__(self, 0, 0)


class RedHomeBase(HomeBase):
    def __init__(self):
        HomeBase.__init__(self, 736, 736)


colours = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'PURPLE': (255, 0, 255),
    'ORANGE': (255, 128, 0)
}

window = pygame.display.set_mode([800, 800])
pygame.display.set_caption('Capture the Flag')
pygame.display.set_icon(pygame.image.load('Sprites/WhiteFlag.png'))
window.fill(colours['WHITE'])

bluePlayer = BluePlayer('Sprites/BluePlayer.png', 0, 0, False)
redPlayer = RedPlayer('Sprites/RedPlayer.png', 768, 768, False)
players = pygame.sprite.Group([bluePlayer, redPlayer])

blueFlag = BlueFlag()
redFlag = RedFlag()
flags = pygame.sprite.Group([blueFlag, redFlag])

blueHomeBase = BlueHomeBase()
redHomeBase = RedHomeBase()
homebases = pygame.sprite.Group([blueHomeBase, redHomeBase])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.locals.K_ESCAPE:
                quit() # quit

    keysPressed = pygame.key.get_pressed()

    blueFlagGrab = pygame.sprite.spritecollide(blueFlag, players, False)
    for item in blueFlagGrab:
        if item == redPlayer:
            blueFlag.kill()
            redPlayer = RedPlayer('Sprites/RedPlayerBlueFlag.png', redPlayer.getRectX(), redPlayer.getRectY(), True)

    redFlagGrab = pygame.sprite.spritecollide(redFlag, players, False)
    for item in redFlagGrab:
        if item == bluePlayer:
            redFlag.kill()
            bluePlayer = BluePlayer('Sprites/BluePlayerRedFlag.png', bluePlayer.getRectX(), bluePlayer.getRectY(), True)

    players = pygame.sprite.Group([bluePlayer, redPlayer])

    bluePlayerWin = pygame.sprite.spritecollide(bluePlayer, homebases, False)
    for item in bluePlayerWin:
        if item == blueHomeBase and bluePlayer.getHasflag():
            print('Blue Wins')
            quit()

    redPlayerWin = pygame.sprite.spritecollide(redPlayer, homebases, False)
    for item in redPlayerWin:
        if item == redHomeBase and redPlayer.getHasflag():
            print('Red Wins')
            quit()

    players.update()
    window.fill(colours['WHITE'])

    homebases.draw(window)
    flags.draw(window)
    players.draw(window)

    pygame.display.flip()
