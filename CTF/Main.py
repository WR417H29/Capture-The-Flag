import pygame.locals
from Bullet import BlueBullets, RedBullets
from Flags import BlueFlag, RedFlag
from Homebase import BlueHomeBase, RedHomeBase
from Players import BluePlayer, RedPlayer

# importing all the necessary classes and behaviours

colours = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (255, 0, 0),
    'GREEN': (0, 255, 0),
    'BLUE': (0, 0, 255),
    'PURPLE': (255, 0, 255),
    'ORANGE': (255, 128, 0)
}  # defining colours for later use

window = pygame.display.set_mode([800, 800])  # setting the size of the window
pygame.display.set_caption('Capture the Flag')  # setting the name of the window
pygame.display.set_icon(pygame.image.load('Sprites/Flags/WhiteFlag.png'))  # setting the window icon
window.fill(colours['WHITE'])  # filling the base screen with white
FPS = 60
clock = pygame.time.Clock()

bluePlayer = BluePlayer('Sprites/Players/BluePlayerRight.png', 0, 0, False, 1,
                        3)  # declaring bluePlayer as a BluePlayer iteration
redPlayer = RedPlayer('Sprites/Players/RedPlayerLeft.png', 768, 768, False, 3,
                      3)  # declaring redPlayer as a RedPlayer iteration
players = pygame.sprite.Group([bluePlayer, redPlayer])  # creating a sprite group for the players

blueFlag = BlueFlag()  # declaring blueFlag as a BlueFlag iteration
redFlag = RedFlag()  # declaring redFlag as a RedFlag iteration
flags = pygame.sprite.Group([blueFlag, redFlag])  # creating a sprite group for the players

blueHomeBase = BlueHomeBase()  # declaring blueHomeBase as a BlueHomeBase iteration
redHomeBase = RedHomeBase()  # declaring redHomeBase as a RedHomeBase iteration
homebases = pygame.sprite.Group([blueHomeBase, redHomeBase])  # creating a sprite group for the players

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
    for item in blueFlagGrab:  # iterating through the list of players touching it
        if item == redPlayer:  # if the player is the red player
            blueFlag.kill()  # deleting the blueFlag sprite iteration
            redPlayer = RedPlayer('Sprites/Players/RedPlayerBlueFlag.png', redPlayer.getRectX(), redPlayer.getRectY(),
                                  True, redPlayer.getDirection(),
                                  redPlayer.getLives())  # redeclaring the redPlayer with a new sprite of them with the flag, and setting the hasFlag value to true

    redFlagGrab = pygame.sprite.spritecollide(redFlag, players, False)
    for item in redFlagGrab:  # iterating through the list of players touching it
        if item == bluePlayer:  # if the player is the blue player
            redFlag.kill()  # deleting the redFlag sprite iteration
            bluePlayer = BluePlayer('Sprites/Players/BluePlayerRedFlag.png', bluePlayer.getRectX(),
                                    bluePlayer.getRectY(), True, bluePlayer.getDirection(),
                                    bluePlayer.getLives())  # redeclaring the bluePlayer with a new sprite of them with the flag, and setting the hasFlag value to true

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

    if bluePlayer.getRectX() < redPlayer.getRectX():
        if not bluePlayer.getHasflag() and not redPlayer.getHasflag():
            bluePlayer.updateImage('Sprites/Players/BluePlayerRight.png')
            redPlayer.updateImage('Sprites/Players/RedPlayerLeft.png')
        if bluePlayer.getHasflag() or redPlayer.getHasflag():
            if bluePlayer.getHasflag():
                bluePlayer.updateImage('Sprites/Players/BluePlayerRedFlag.png')
                redPlayer.updateImage('Sprites/Players/RedPlayerLeft.png')
            if redPlayer.getHasflag():
                bluePlayer.updateImage('Sprites/Players/BluePlayerRight.png')
                redPlayer.updateImage('Sprites/Players/RedPlayerBlueFlag.png')

    if bluePlayer.getRectX() > redPlayer.getRectX():
        if not bluePlayer.getHasflag() and not redPlayer.getHasflag():
            bluePlayer.updateImage('Sprites/Players/BluePlayerLeft.png')
            redPlayer.updateImage('Sprites/Players/RedPlayerRight.png')
        if bluePlayer.getHasflag() or redPlayer.getHasflag():
            if bluePlayer.getHasflag():
                bluePlayer.updateImage('Sprites/Players/BluePlayerRedFlag.png')
                redPlayer.updateImage('Sprites/Players/RedPlayerRight.png')
            if redPlayer.getHasflag():
                bluePlayer.updateImage('Sprites/Players/BluePlayerLeft.png')
                redPlayer.updateImage('Sprites/Players/RedPlayerBlueFlag.png')

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
