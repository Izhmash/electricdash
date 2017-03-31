import pygame
import os

WIDTH = 1024
HEIGHT = 600
size = (WIDTH, HEIGHT)

BACKGROUND = pygame.image.load('scarletbox.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND, size)
BACKGROUND_RECT = BACKGROUND.get_rect()


# Class for a simple electric car dashboard
class Dash(object):
    def __init__(self):
        self.screen = self.initPygame()
        self.screenRect = self.screen.get_rect()
        self.done = False

        self.speedSize = 200
        self.voltSize = 100
        self.speedFont = pygame.font.SysFont("Ubuntu Medium", self.speedSize)
        self.voltFont = pygame.font.SysFont("Ubuntu Medium", self.voltSize)

        self.fps = 60
        self.clock = pygame.time.Clock()
        self.keys = self.getUserInput()

    # Initializes Pygame
    def initPygame(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.set_caption('Dashboard Test')
        screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        return screen

    # Checks for exit, returns key presses
    def getUserInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
        keys = pygame.key.get_pressed()
        return keys

    # Updates all text rects
    def updateText(self):
            speed = self.speedFont.render("88 mph", 1, (255, 255, 255))
            speedRect = speed.get_rect()
            speedRect.centerx = WIDTH/2
            speedRect.centery = HEIGHT/3
            self.screen.blit(speed, speedRect)
            
            volt = self.voltFont.render("114.6 V", 1, (255, 255, 255))
            voltRect = speed.get_rect()
            voltRect.centerx = WIDTH/2 + (self.speedSize - self.voltSize)
            voltRect.centery = HEIGHT/4 * 2 + (self.speedSize - self.voltSize)
            self.screen.blit(volt, voltRect)

    # Update all Dash components and exit upon ESC press
    def update(self):
        while not self.done and not self.keys[pygame.K_ESCAPE]:
            self.keys = self.getUserInput()
            currentTime = pygame.time.get_ticks()
            self.screen.blit(BACKGROUND, BACKGROUND_RECT)
            
            self.updateText()

            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()

dash = Dash()
dash.update()
