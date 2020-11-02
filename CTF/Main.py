import pygame.locals
from Flags import BlueFlag, RedFlag
from Homebase import BlueHomeBase, RedHomeBase
from Players import BluePlayer, RedPlayer
from Bullet import BlueBullets, RedBullets

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

bluePlayer = BluePlayer('Sprites/Players/BluePlayerRight.png', 0, 0, False, 1, 3)  # declaring bluePlayer as a BluePlayer iteration
redPlayer = RedPlayer('Sprites/Players/RedPlayerLeft.png', 768, 768, False, 3, 3)  # declaring redPlayer as a RedPlayer iteration
players = pygame.sprite.Group([bluePlayer, redPlayer])  # creating a sprite group for the players

blueFlag = BlueFlag()  # declaring blueFlag as a BlueFlag iteration
redFlag = RedFlag()  # declaring redFlag as a RedFlag iteration
flags = pygame.sprite.Group([blueFlag, redFlag])  # creating a sprite group for the players

blueHomeBase = BlueHomeBase()  # declaring blueHomeBase as a BlueHomeBase iteration
redHomeBase = RedHomeBase()  # declaring redHomeBase as a RedHomeBase iteration
homebases = pygame.sprite.Group([blueHomeBase, redHomeBase])  # creating a sprite group for the players

blueGun = BlueBullets(bluePlayer.getRectX(), bluePlayer.getRectY(), bluePlayer.getDirection())
redGun = RedBullets(redPlayer.getRectX(), redPlayer.getRectY(), redPlayer.getDirection())
guns = pygame.sprite.Group([blueGun, redGun])

while True:  # running a game loop
    for event in pygame.event.get():  # checking every event happening in the loop
        if event.type == pygame.QUIT:  # checking if the event happening is to quit the game
            quit()  # quitting the game
        if event.type == pygame.KEYDOWN:  # checking if the event is that a key has been pressed
            if event.key == pygame.locals.K_ESCAPE:  # if the key is escape closing the game
                quit()  # quit

    keysPressed = pygame.key.get_pressed()  # creating a list of pressed keys

    '''
    if keysPressed == blueGun.getShootKey() or keysPressed == redGun.getShootKey():
        guns.update()
    '''

    blueFlagGrab = pygame.sprite.spritecollide(blueFlag, players, False)  # checking if the blueFlag has collided with any player Sprites
    for item in blueFlagGrab:  # iterating through the list of players touching it
        if item == redPlayer:  # if the player is the red player
            blueFlag.kill()  # deleting the blueFlag sprite iteration
            redPlayer = RedPlayer('Sprites/Players/RedPlayerBlueFlag.png', redPlayer.getRectX(), redPlayer.getRectY(), True, redPlayer.getDirection(), redPlayer.getLives())  # redeclaring the redPlayer with a new sprite of them with the flag, and setting the hasFlag value to true

    redFlagGrab = pygame.sprite.spritecollide(redFlag, players, False)  # checking if the redFlag has collided with any player sprites
    for item in redFlagGrab:  # iterating through the list of players touching it
        if item == bluePlayer:  # if the player is the blue player
            redFlag.kill()  # deleting the redFlag sprite iteration
            bluePlayer = BluePlayer('Sprites/Players/BluePlayerRedFlag.png', bluePlayer.getRectX(), bluePlayer.getRectY(), True, bluePlayer.getDirection(), bluePlayer.getLives())  # redeclaring the bluePlayer with a new sprite of them with the flag, and setting the hasFlag value to true

    bluePlayerWin = pygame.sprite.spritecollide(bluePlayer, homebases, False)  # checking if the bluePlayer collides with any homeBase items
    for item in bluePlayerWin:  # iterating through the list of homebases that it touches
        if item == blueHomeBase and bluePlayer.getHasflag():  # if the homeBase being touched is blue, and the value of the hasFlag value is true
            print('Blue Wins')  # declaring blue as the winner
            quit()  # ending the program

    redPlayerWin = pygame.sprite.spritecollide(redPlayer, homebases, False)  # checking if the redPlayer collides with any homeBase items
    for item in redPlayerWin:  # iterating through the list of homebases that it touches
        if item == redHomeBase and redPlayer.getHasflag():  # if the homeBase being touched is red, and the value of the hasFlag value is true
            print('Red Wins')  # declaring red as the winner
            quit()  # ending the program

    if bluePlayer.getRectX() < redPlayer.getRectX():  # if the blue player is on the left hand side of the red player, change the sprites to look at each other
        if not bluePlayer.getHasflag() or not redPlayer.getHasflag():
            bluePlayer = BluePlayer('Sprites/Players/BluePlayerRight.png', bluePlayer.getRectX(), bluePlayer.getRectY(), False, bluePlayer.getDirection(), bluePlayer.getLives())
            redPlayer = RedPlayer('Sprites/Players/RedPlayerLeft.png', redPlayer.getRectX(), redPlayer.getRectY(), False, redPlayer.getDirection(), redPlayer.getLives())
        if bluePlayer.getHasflag() or redPlayer.getHasflag():
            bluePlayer = BluePlayer('Sprites/Players/BluePlayerRedFlag.png', bluePlayer.getRectX(), bluePlayer.getRectY(), True, bluePlayer.getDirection(), bluePlayer.getLives())
            redPlayer = RedPlayer('Sprites/Players/RedPlayerBlueFlag.png', redPlayer.getRectX(), redPlayer.getRectY(), True, redPlayer.getDirection(), redPlayer.getLives())

    if bluePlayer.getRectX() > redPlayer.getRectX():  # if the red player is on the left hand side of the blue player, change the sprites to look at each other
        if not bluePlayer.getHasflag() or not redPlayer.getHasflag():
            bluePlayer = BluePlayer('Sprites/Players/BluePlayerLeft.png', bluePlayer.getRectX(), bluePlayer.getRectY(), False, bluePlayer.getDirection(), bluePlayer.getLives())
            redPlayer = RedPlayer('Sprites/Players/RedPlayerRight.png', redPlayer.getRectX(), redPlayer.getRectY(), False, redPlayer.getDirection(), redPlayer.getLives())
        if bluePlayer.getHasflag() or redPlayer.getHasflag():
            bluePlayer = BluePlayer('Sprites/Players/BluePlayerRedFlag.png', bluePlayer.getRectX(), bluePlayer.getRectY(), True, bluePlayer.getDirection(), bluePlayer.getLives())
            redPlayer = RedPlayer('Sprites/Players/RedPlayerBlueFlag.png', redPlayer.getRectX(), redPlayer.getRectY(), True, redPlayer.getDirection(), redPlayer.getLives())

    players = pygame.sprite.Group([bluePlayer, redPlayer])  # redeclaring the group of players to make sure they are up to date

    guns.update(keysPressed) # meant to update the locations of bullets when shot
    players.update(keysPressed)  # updating the locations of the players on screen
    window.fill(colours['WHITE'])  # refilling the background


    homebases.draw(window)  # drawing the home bases
    flags.draw(window)  # drawing the flags
    players.draw(window)  # drawing the players
    guns.draw(window) # meant to draw the bullets to the screen

    pygame.display.flip()  # redrawing the screen and iterating through
