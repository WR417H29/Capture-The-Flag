import time

import pygame
import pygame.locals

from Players import Player, BluePlayer, RedPlayer
from Flags import Flag, BlueFlag, RedFlag
from Homebase import HomeBase, BlueHomeBase, RedHomeBase

from Utils import LOAD_IMG

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
pygame.display.set_icon(pygame.image.load(LOAD_IMG('Flags/WhiteFlag.png')))
window.fill(colours['WHITE'])

bluePlayer = BluePlayer(LOAD_IMG('Players/BluePlayerRight.png'), 0, 0, False)
redPlayer = RedPlayer(LOAD_IMG('Players/RedPlayerLeft.png'), 768, 768, False)
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
            redPlayer = RedPlayer(LOAD_IMG('Players/RedPlayerBlueFlag.png'), redPlayer.getRectX(), redPlayer.getRectY(), True)

    redFlagGrab = pygame.sprite.spritecollide(redFlag, players, False)
    for item in redFlagGrab:
        if item == bluePlayer:
            redFlag.kill()
            bluePlayer = BluePlayer(LOAD_IMG('Players/BluePlayerRedFlag.png'), bluePlayer.getRectX(), bluePlayer.getRectY(), True)



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

    if bluePlayer.getRectX() >= 400:
        bluePlayer = BluePlayer(LOAD_IMG('Players/BluePlayerLeft.png'), bluePlayer.getRectX(), bluePlayer.getRectY(), False)
    if bluePlayer.getRectX() < 400:
        bluePlayer = BluePlayer(LOAD_IMG('Players/BluePlayerRight.png'), bluePlayer.getRectX(), bluePlayer.getRectY(), False)

    if redPlayer.getRectX() >= 400:
        redPlayer = RedPlayer(LOAD_IMG('Players/RedPlayerLeft.png'), redPlayer.getRectX(), redPlayer.getRectY(), False)
    if redPlayer.getRectX() < 400:
        redPlayer = RedPlayer(LOAD_IMG('Players/RedPlayerRight.png'), redPlayer.getRectX(), redPlayer.getRectX(), False)

    players = pygame.sprite.Group([bluePlayer, redPlayer])
    players.update(keysPressed)
    window.fill(colours['WHITE'])

    homebases.draw(window)
    flags.draw(window)
    players.draw(window)

    pygame.display.flip()
