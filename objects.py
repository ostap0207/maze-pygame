__author__ = 'Ostap'
import pygame

class Human(pygame.sprite.Sprite):
    def __init__(self,image,speed,walls,end,display):
        pygame.sprite.Sprite.__init__(self)
        self.initSprites(image)
        self.image = self.sprites[0][1]
        self.speed = speed
        self.rect = self.image.get_rect()
        self.walls = walls
        self.end = end
        self.rect = self.rect.move(50,50)
        self.cursprite = 1;
        self.curway = 0;
        self.display = display

    def initSprites(self,image):
        self.sprites = [[],[],[],[]]
        for i in range(0,4):
            for j in range(0,3):
                sprite = image.subsurface(pygame.Rect(j * 32,i * 32,32,32))
                self.sprites[i].append(sprite)
    def move(self,x,y):
        self.cursprite = (self.cursprite + 1) % 3
        if (x == 0) and (y == 0):
            self.cursprite = 1
        elif (x != 0):
            if (x > 0):
                self.curway = 2
            else:
                self.curway = 1
            y = 0
        else:
            if (y > 0):
                self.curway = 0
            else:
                self.curway = 3
            x = 0
        self.rect = self.rect.move(x,y)
        self.image = self.sprites[self.curway][self.cursprite]

        if pygame.sprite.collide_rect(self,self.end):
            self.allsprites.update()

        for wall in self.walls:
            if pygame.sprite.collide_rect(self,wall) and wall != self.end:
                if x > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if x < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if y > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if y < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom





class Wall(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.subsurface(pygame.Rect(3 * 32,2 * 32,32,32))
        self.rect = self.image.get_rect().move(x,y)

class End(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image.subsurface(pygame.Rect(8 * 32,8 * 32,64,64))
        self.rect = self.image.get_rect().move(x,y)
