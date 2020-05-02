import pygame
import math
import cmath
from random import randint
import random
BLACK=(0,0,0)

class Ball(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__() #calling parent class constructor, same as pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.ballSpeed = 5
        self.velocity = [self.ballSpeed*math.cos(math.pi/6), -self.ballSpeed*math.sin(math.pi/3)]

        self.rect = self.image.get_rect()
        self.sign = 1



    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def wallBounce(self):
        # Bouncing from vertical walls
        if self.rect.x >=700:
            self.velocity[0] = -self.velocity[0]
        if self.rect.x <= 0:
            self.velocity[0] = -self.velocity[0]
        # Bouncing from horizontal walls
        #if self.rect.y <= 0:
         #   self.velocity[1] = -self.velocity[1]
        #if self.rect.y >= 1000:
         #   self.velocity[1] = -self.velocity[1]

    def paddleBounce(self,interSection):
        normalizedInterSection = interSection/50
        angle = normalizedInterSection * (8*math.pi/12)
        #self.velocity[0] = self.ballSpeed*math.cos(angle)
        #self.velocity[1] = -self.ballSpeed*math.sin(angle)
        #print(self.velocity[1])

        self.velocity[0] = self.ballSpeed*math.cos(angle)
        self.velocity[1] = -self.velocity[1]*1.1


    def resetBall(self):
        if self.rect.y < 10:
            self.rect.x = 365
            self.rect.y = 495
            self.velocity = [self.ballSpeed*math.cos(math.pi/6), self.ballSpeed*math.sin(math.pi/2)]

        if self.rect.y > 990:
            self.rect.x = 365
            self.rect.y = 495
            self.velocity = [self.ballSpeed*math.cos(math.pi/6)*random.choice([-1, 1]), self.ballSpeed*math.sin(math.pi/2)*random.choice([-1,1])]













