import time

import pygame
import pygame.locals
from Players import Player, BluePlayer, RedPlayer
from Flags import Flag, BlueFlag, RedFlag
from Homebase import HomeBase, BlueHomeBase, RedHomeBase

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
pygame.display.set_icon(pygame.image.load('Sprites/Flags/WhiteFlag.png'))
window.fill(colours['WHITE'])

bluePlayer = BluePlayer('Sprites/Players/BluePlayerRight.png', 0, 0, False, 1)
redPlayer = RedPlayer('Sprites/Players/RedPlayerLeft.png', 768, 768, False, 3)
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
            redPlayer = RedPlayer('Sprites/Players/RedPlayerBlueFlag.png', redPlayer.getRectX(), redPlayer.getRectY(), True, redPlayer.getDirection())

    redFlagGrab = pygame.sprite.spritecollide(redFlag, players, False)
    for item in redFlagGrab:
        if item == bluePlayer:
            redFlag.kill()
            bluePlayer = BluePlayer('Sprites/Players/BluePlayerRedFlag.png', bluePlayer.getRectX(), bluePlayer.getRectY(), True, bluePlayer.getDirection())



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

    if bluePlayer.getRectX() < redPlayer.getRectX():
        bluePlayer = BluePlayer('Sprites/Players/BluePlayerRight.png', bluePlayer.getRectX(), bluePlayer.getRectY(), False, bluePlayer.getDirection())
        redPlayer = RedPlayer('Sprites/Players/RedPlayerLeft.png', redPlayer.getRectX(), redPlayer.getRectY(), False, redPlayer.getDirection())

    if bluePlayer.getRectX() > redPlayer.getRectX():
        bluePlayer = BluePlayer('Sprites/Players/BluePlayerLeft.png', bluePlayer.getRectX(), bluePlayer.getRectY(), False, bluePlayer.getDirection())
        redPlayer = RedPlayer('Sprites/Players/RedPlayerRight.png', redPlayer.getRectX(), redPlayer.getRectY(), False, redPlayer.getDirection())


    players = pygame.sprite.Group([bluePlayer, redPlayer])
    players.update(keysPressed)
    window.fill(colours['WHITE'])

    print(bluePlayer.getDirection(), redPlayer.getDirection())

    homebases.draw(window)
    flags.draw(window)
    players.draw(window)

    pygame.display.flip()
