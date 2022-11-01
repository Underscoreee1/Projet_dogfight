import pygame
from player import Player

class Game:
    def __init__(self):
        self.playerImg = pygame.image.load("assets/avion.png")
        self.bulletImg = pygame.image.load("assets/bullet.png")
        self.bulletImg = pygame.transform.scale(self.bulletImg,(10,10))
        self.player = Player((200,200),1,self.playerImg,self.bulletImg)
        self.pressed = {}

        self.playerBulletGroup = pygame.sprite.Group()