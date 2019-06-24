__author__ = 'Ostap'
import pygame
import sys
from pygame.locals import *
from objects import Human
from objects import Wall
from objects import End
pygame.init()


class MazeGame:
    def __init__(self):
        self.width = 900
        self.height = 768
        self.color = 0, 0, 0
        self.key = None
        self.init()
        self.walls = []
        self.map = [
            "WWWWWWWWWWWWWWWWWWWW",
            "W           WW     W",
            "W         WWWWWW   W",
            "W   WWWW       W   W",
            "W   W        WWWW  W",
            "W WWW  WWWW       E ",
            "W   W     W W       ",
            "W   W     W   WWW  W",
            "W   WWW WWW   W W  W",
            "W     W   W   W W  W",
            "WWW   W   WWWWW W  W",
            "W W      WW        W",
            "W W   WWWW   WWW   W",
            "W     W        W   W",
            "WWWWWWWWWWWWWWWWWWWW",
            ]
        self.generateMap()
        self.human = Human(self.loadImage("mansprites.png"),[1,1],self.walls,self.end,self.screen)
        self.allsprites.add(self.human)


    def init(self):
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.allsprites = pygame.sprite.RenderPlain()
        self.clock = pygame.time.Clock()

    def keyevent(self,key):

        if key[pygame.K_RIGHT]: self.human.move(5,0)
        if key[pygame.K_LEFT]: self.human.move(-5,0)
        if key[pygame.K_UP]: self.human.move(0,-5)
        if key[pygame.K_DOWN]: self.human.move(0,5)


    def start(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYUP:
                    self.human.move(0,0);
            self.keyevent(pygame.key.get_pressed())
            self.update()
            self.clock.tick(15)

    def generateMap(self):
        image = self.loadImage("sprites.png")
        i = 0
        j = 0
        for line in self.map:
            for w in line:
                if (w == 'W'):
                    wall = Wall(image,j,i)
                    self.allsprites.add(wall)
                    self.walls.append(wall)
                if (w == 'E'):
                    self.end = End(image,j,i)
                    self.allsprites.add(self.end)
                    self.walls.append(self.end)
                j += 32
            i += 32
            j = 0



    def update(self):
        self.screen.fill(self.color)
        self.allsprites.draw(self.screen)
        self.allsprites.update()
        pygame.display.flip()

    def loadImage(self,name):
        image = pygame.image.load(name)
        return image

game = MazeGame()
game.start()
