from math import *
import pygame
from bullets import Bullets

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, speed, img, bulletImg):
        super().__init__()
        self.pos = pos
        self.speed = speed
        self.image = img
        self.rect = self.image.get_rect()
        self.originImage = self.image
        self.rotation = 0
        self.angleSpeed = 1
        self.bulletImg = bulletImg
        self.direction = pygame.math.Vector2(0,1)
        self.bulletSpeed = 5

    def update(self):
        self.image = pygame.transform.rotozoom(self.originImage,self.rotation,1)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    
    def move(self,x_axis, y_axis):
        delta_rotation = x_axis * self.angleSpeed
        self.rotation -= delta_rotation

        vec = pygame.math.Vector2(0, 1)
        vec.y = y_axis * self.speed
        vec.rotate_ip(-self.rotation)

        self.direction.rotate_ip(delta_rotation)
        self.direction.normalize_ip()

        self.pos = (self.pos[0] + vec.x, self.pos[1] + vec.y)
    
    def fire(self):
        return Bullets(self.pos, (self.direction.x,self.direction.y), self.bulletSpeed, self.bulletImg)