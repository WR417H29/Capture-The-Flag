# ~~~~~ Importing Pygame and Classes ~~~~~ #

import pygame.locals
from Bullet import BlueBullets, RedBullets
from Flags import BlueFlag, RedFlag
from Homebase import BlueHomeBase, RedHomeBase
from Players import BluePlayer, RedPlayer

colours = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'PURPLE': (255, 0, 255),
    'ORANGE': (255, 128, 0)
}  # Defining Colours for later use

# ~~~~~ Setting the basics of the game window ~~~~~ #

window = pygame.display.set_mode([800, 800])
pygame.display.set_caption('Capture the Flag')
pygame.display.set_icon(pygame.image.load('Sprites/Flags/WhiteFlag.png'))
window.fill(colours['WHITE'])
FPS = 60
clock = pygame.time.Clock()

# ~~~~~ Creating the Players ~~~~~ #

bluePlayer = BluePlayer('Sprites/Players/BluePlayerRight.png', 0, 0, False, 1, 3)
redPlayer = RedPlayer('Sprites/Players/RedPlayerLeft.png', 768, 768, False, 3, 3)
players = pygame.sprite.Group([bluePlayer, redPlayer])

# ~~~~~ Creating the Flags ~~~~~ #

blueFlag = BlueFlag()
redFlag = RedFlag()
flags = pygame.sprite.Group([blueFlag, redFlag])

# ~~~~~ Creating the Home Bases ~~~~~ #

blueHomeBase = BlueHomeBase()
redHomeBase = RedHomeBase()
homebases = pygame.sprite.Group([blueHomeBase, redHomeBase])

# ~~~~~ Creating the Guns and Timers ~~~~~ #

guns = pygame.sprite.Group()
blueShootTimer, redShootTimer = 0, 0

# ~~~~~ Running the Game Loop ~~~~~ #

while True:

    # ~~~~~ Checking if the player tries to end the game ~~~~~ #

    for event in pygame.event.get():  # checking every event happening in the loop
        if event.type == pygame.QUIT:  # checking if the event happening is to quit the game
            quit()  # quitting the game
        if event.type == pygame.KEYDOWN:  # checking if the event is that a key has been pressed
            if event.key == pygame.locals.K_ESCAPE:  # if the key is escape closing the game
                quit()  # quit

    keysPressed = pygame.key.get_pressed()  # creating a list of pressed keys

    # ~~~~~ Checking if either player has shot ~~~~~ #

    if keysPressed[pygame.locals.K_q] and blueShootTimer >= 150:
        guns.add(BlueBullets(bluePlayer.getCenterX(), (bluePlayer.getCenterY() - 2), bluePlayer.getDirection()))
        blueShootTimer = 0

    if keysPressed[pygame.locals.K_u] and redShootTimer >= 150:
        guns.add(RedBullets(redPlayer.getCenterX(), (redPlayer.getCenterY() - 2), redPlayer.getDirection()))
        redShootTimer = 0

    # ~~~~~ Checking if either play has touched the enemy player's flag ~~~~~ #

    blueFlagGrab = pygame.sprite.spritecollide(blueFlag, players, False)
    for item in blueFlagGrab:
        if item == redPlayer:
            blueFlag.kill()
            redPlayer.setImage('Sprites/Players/RedPlayerBlueFlag.png')

    redFlagGrab = pygame.sprite.spritecollide(redFlag, players, False)
    for item in redFlagGrab:
        if item == bluePlayer:
            redFlag.kill()
            bluePlayer.setImage('Sprites/Players/BluePlayerRedFlag.png')

    # ~~~~~ Checking if either player beats the win conditions ~~~~~ #

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

    # ~~~~~ Changing Player Direction Based on the Location of Both Players ~~~~~ #

    '''
    if bluePlayer.getRectX() < redPlayer.getRectX():
        if not bluePlayer.getHasflag() and not redPlayer.getHasflag():
            bluePlayer.setImage('Sprites/Players/BluePlayerRight.png')
            redPlayer.setImage('Sprites/Players/RedPlayerLeft.png')
        if not bluePlayer.getHasflag() and redPlayer.getHasflag():
            bluePlayer.setImage('Sprites/Players/BluePlayerRight.png')
            redPlayer.setImage('Sprites/Players/RedPlayerBlueFlag.png')
        if bluePlayer.getHasflag() and not redPlayer.getHasflag():
            bluePlayer.setImage('Sprites/Players/BluePlayerRedFlag.png')
            redPlayer.setImage('Sprites/Players/RedPlayerLeft.png')
        if bluePlayer.getHasflag() and redPlayer.getHasflag():
            bluePlayer.setImage('Sprites/Players/BluePlayerRedFlag.png')
            redPlayer.setImage('Sprites/Players/RedPlayerBlueFlag.png')

    if bluePlayer.getRectX() > redPlayer.getRectX():
        if not bluePlayer.getHasflag() and not redPlayer.getHasflag():
            bluePlayer.setImage('Sprites/Players/BluePlayerLeft.png')
            redPlayer.setImage('Sprites/Players/RedPlayerRight.png')
        if not bluePlayer.getHasflag() and redPlayer.getHasflag():
            bluePlayer.setImage('Sprites/Players/BluePlayerLeft.png')
            redPlayer.setImage('Sprites/Players/RedPlayerBlueFlag.png')
        if bluePlayer.getHasflag() and not redPlayer.getHasflag():
            bluePlayer.setImage('Sprites/Players/BluePlayerRedFlag.png')
            redPlayer.setImage('Sprites/Players/RedPlayerRight.png')
        if bluePlayer.getHasflag() and redPlayer.getHasflag():
            bluePlayer.setImage('Sprites/Players/BluePlayerRedFlag.png')
            redPlayer.setImage('Sprites/Players/RedPlayerBlueFlag.png')
    '''

    # ~~~~~ Updating Moving Sprites ~~~~~ #

    guns.update()
    players.update(keysPressed)

    # ~~~~~ Drawing the Assets to the Screen ~~~~~ #

    window.fill(colours['WHITE'])
    homebases.draw(window)
    guns.draw(window)
    flags.draw(window)
    players.draw(window)

    # ~~~~~ Incrementing the gun cooldowns ~~~~~ #

    blueShootTimer += 10
    redShootTimer += 10

    # ~~~~~ Setting FPS and Refreshing the Screen ~~~~~ #

    clock.tick(FPS)
    pygame.display.flip()
