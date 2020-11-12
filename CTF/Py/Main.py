# ~~~~~ IMPORTING PYGAME AND CLASSES ~~~~~ #

from Bullet import BlueBullets, RedBullets
from Flags import BlueFlag, RedFlag
from Homebase import BlueHomeBase, RedHomeBase
from Players import BluePlayer, RedPlayer
import pygame

colours = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'PURPLE': (255, 0, 255),
    'ORANGE': (255, 128, 0)
}  # DEFINING COLOURS FOR LATER USE

# ~~~~~ SETTING THE BASICS OF THE GAME WINDOW ~~~~~ #

window = pygame.display.set_mode([800, 800])
pygame.display.set_caption('Capture the Flag')
pygame.display.set_icon(pygame.image.load('CTF/Sprites/Flags/WhiteFlag.png'))
window.fill(colours['WHITE'])
FPS = 30
clock = pygame.time.Clock()

# ~~~~~ CREATING THE PLAYERS ~~~~~ #

bluePlayer = BluePlayer('CTF/Sprites/Players/BluePlayerRight.png', 0, 0, False, 1, 3)
redPlayer = RedPlayer('CTF/Sprites/Players/RedPlayerLeft.png', 768, 768, False, 3, 3)
players = pygame.sprite.Group([bluePlayer, redPlayer])

# ~~~~~ CREATING THE FLAGS ~~~~~ #

blueFlag = BlueFlag()
redFlag = RedFlag()
flags = pygame.sprite.Group([blueFlag, redFlag])

# ~~~~~ CREATING THE HOME BASES ~~~~~ #

blueHomeBase = BlueHomeBase()
redHomeBase = RedHomeBase()
homebases = pygame.sprite.Group([blueHomeBase, redHomeBase])

# ~~~~~ CREATING THE GUNS AND TIMERS ~~~~~ #

guns = pygame.sprite.Group()
blueShootTimer, redShootTimer = 0, 0

# ~~~~~ RUNNING THE GAME LOOP ~~~~~ #

while True:

    # ~~~~~ CHECKING IF THE PLAYER TRIES TO END THE GAME ~~~~~ #

    for event in pygame.event.get():  # CHECKING EVERY EVENT HAPPENING IN THE LOOP
        if event.type == pygame.QUIT:  # CHECKING IF THE EVENT HAPPENING IS TO QUIT THE GAME
            quit()  # QUITTING THE GAME
        if event.type == pygame.KEYDOWN:  # CHECKING IF THE EVENT IS THAT A KEY HAS BEEN PRESSED
            if event.key == pygame.locals.K_ESCAPE:  # IF THE KEY IS ESCAPE CLOSING THE GAME
                quit()  # QUIT

    keysPressed = pygame.key.get_pressed()  # CREATING A LIST OF PRESSED KEYS

    # ~~~~~ CHECKING IF EITHER PLAYER HAS SHOT ~~~~~ #

    if keysPressed[pygame.locals.K_q] and blueShootTimer >= 150:
        guns.add(BlueBullets(bluePlayer.getCenterX(), (bluePlayer.getCenterY() - 2), bluePlayer.getDirection()))
        blueShootTimer = 0

    if keysPressed[pygame.locals.K_u] and redShootTimer >= 150:
        guns.add(RedBullets(redPlayer.getCenterX(), (redPlayer.getCenterY() - 2), redPlayer.getDirection()))
        redShootTimer = 0

    # ~~~~~ CHECKING IF EITHER PLAY HAS TOUCHED THE ENEMY PLAYER'S FLAG ~~~~~ #

    blueFlagGrab = pygame.sprite.spritecollide(blueFlag, players, False)
    for item in blueFlagGrab:
        if item == redPlayer:
            blueFlag.kill()
            redPlayer.setImage('CTF/Sprites/Players/RedPlayerBlueFlag.png')

    redFlagGrab = pygame.sprite.spritecollide(redFlag, players, False)
    for item in redFlagGrab:
        if item == bluePlayer:
            redFlag.kill()
            bluePlayer.setImage('CTF/Sprites/Players/BluePlayerRedFlag.png')

    # ~~~~~ CHECKING IF EITHER PLAYER BEATS THE WIN CONDITIONS ~~~~~ #

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

    # ~~~~~ CHANGING PLAYER DIRECTION BASED ON THE LOCATION OF BOTH PLAYERS ~~~~~ #

    '''
    if bluePlayer.getRectX() < redPlayer.getRectX():
        if not bluePlayer.getHasflag() and not redPlayer.getHasflag():
            bluePlayer.setImage('CTF/Sprites/Players/BluePlayerRight.png')
            redPlayer.setImage('CTF/Sprites/Players/RedPlayerLeft.png')
        if not bluePlayer.getHasflag() and redPlayer.getHasflag():
            bluePlayer.setImage('CTF/Sprites/Players/BluePlayerRight.png')
            redPlayer.setImage('CTF/Sprites/Players/RedPlayerBlueFlag.png')
        if bluePlayer.getHasflag() and not redPlayer.getHasflag():
            bluePlayer.setImage('CTF/Sprites/Players/BluePlayerRedFlag.png')
            redPlayer.setImage('CTF/Sprites/Players/RedPlayerLeft.png')
        if bluePlayer.getHasflag() and redPlayer.getHasflag():
            bluePlayer.setImage('CTF/Sprites/Players/BluePlayerRedFlag.png')
            redPlayer.setImage('CTF/Sprites/Players/RedPlayerBlueFlag.png')

    if bluePlayer.getRectX() > redPlayer.getRectX():
        if not bluePlayer.getHasflag() and not redPlayer.getHasflag():
            bluePlayer.setImage('CTF/Sprites/Players/BluePlayerLeft.png')
            redPlayer.setImage('CTF/Sprites/Players/RedPlayerRight.png')
        if not bluePlayer.getHasflag() and redPlayer.getHasflag():
            bluePlayer.setImage('CTF/Sprites/Players/BluePlayerLeft.png')
            redPlayer.setImage('CTF/Sprites/Players/RedPlayerBlueFlag.png')
        if bluePlayer.getHasflag() and not redPlayer.getHasflag():
            bluePlayer.setImage('CTF/Sprites/Players/BluePlayerRedFlag.png')
            redPlayer.setImage('CTF/Sprites/Players/RedPlayerRight.png')
        if bluePlayer.getHasflag() and redPlayer.getHasflag():
            bluePlayer.setImage('CTF/Sprites/Players/BluePlayerRedFlag.png')
            redPlayer.setImage('CTF/Sprites/Players/RedPlayerBlueFlag.png')
    '''

    # ~~~~~ UPDATING MOVING SPRITES ~~~~~ #

    guns.update()
    players.update(keysPressed)

    # ~~~~~ DRAWING THE ASSETS TO THE SCREEN ~~~~~ #

    window.fill(colours['WHITE'])
    homebases.draw(window)
    guns.draw(window)
    flags.draw(window)
    players.draw(window)

    # ~~~~~ INCREMENTING THE GUN COOLDOWNS ~~~~~ #

    blueShootTimer += 10
    redShootTimer += 10

    # ~~~~~ SETTING FPS AND REFRESHING THE SCREEN ~~~~~ #

    clock.tick(FPS)
    pygame.display.flip()
