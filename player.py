import random
import sys

import pygame


class Player:
    def __init__(self):
        id = ['unremarkable ex-company employee',
            'devastated computer students',
            'fiction writers who run out of inspiration',
            'romantic artist by nature',
            'hired assassin']
        self.id = random.choice(id)

    def ID(self):
        font = pygame.font.Font("FORESTER.ttf",20)
        your_id = font.render("You are a " + self.id + ".",True,(255,255,255))

    def Coin(self):
        coin_start = [50000,10000,100000,20000,66666]
        for i in range(len(id)):
            if self.id == id[i]:
                self.coin = coin_start[i]