import time
import pygame
import pygame.locals


class Player(pygame.sprite.Sprite):
    def __init__(self, img, fwd, bwd, cw, ccw, spawnX, spawnY):
        pygame.sprite.Sprite.__init__(self)  # initialising parent class
        self.image = pygame.image.load(img)  # loading sprite
        self.rect = self.image.get_rect()  # getting the size of the image
        self.direction = 0  # declaring the direction of the player
        self.controls = {'forward': fwd, 'backward': bwd, 'clockwise': cw,
                         'counterclockwise': ccw}  # declaring the controls
        self.spawn = {'x': spawnX, 'y': spawnY}  # setting spawn variables
        self.rect.x = self.spawn['x']  # setting the spawn
        self.rect.y = self.spawn['y']  # setting the spawn

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

        time.sleep(0.1)

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # drawing the players to the screen


class BluePlayer(Player):
    def __init__(self):
        Player.__init__(self, 'Sprites/BluePlayer.png',
                        pygame.locals.K_w, pygame.locals.K_s,
                        pygame.locals.K_d, pygame.locals.K_a, 0, 0)  # initialising the parent class


class RedPlayer(Player):
    def __init__(self):
        Player.__init__(self, 'Sprites/RedPlayer.png',
                        pygame.locals.K_UP, pygame.locals.K_DOWN,
                        pygame.locals.K_RIGHT, pygame.locals.K_LEFT, 768, 768)  # initialising the parent class


window = pygame.display.set_mode([800, 800])
pygame.display.set_caption('Capture the Flag')
WHITE, BLACK, RED, GREEN, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)
window.fill(WHITE)

bluePlayer = BluePlayer()
redPlayer = RedPlayer()
players = pygame.sprite.Group([bluePlayer, redPlayer])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.locals.K_ESCAPE:
                quit()

    keysPressed = pygame.key.get_pressed()

    players.update()
    window.fill(WHITE)
    players.draw(window)
    pygame.display.flip()
