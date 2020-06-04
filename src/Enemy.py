from pygame import *
import sys
from os.path import abspath, dirname, join
from random import choice, randint

sys.path.append(dirname(dirname(__file__)) + '/src/')

from Blocker import *
from Bullet import *
from EnemiesGroup import *
from EnemyExplosion import *
import Main
from Life import *
from Mystery import *
from MysteryExplosion import *
from Ship import *
from ShipExplosion import *
from Text import *

#Characteristics of non-mystery type enemies
class Enemy(sprite.Sprite):
    def __init__(self, row, column):
        sprite.Sprite.__init__(self)
        self.row = row
        self.column = column
        self.images = []
        self.hats = []
        self.load_images()
        self.index = 0
        self.hatNum = randint(0, 2)
        self.image = self.images[self.index]
        self.hat = self.hats[self.hatNum]
        self.rect = self.image.get_rect()
        self.hatRect = self.hat.get_rect()

    def toggle_image(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def update(self, *args): 
        Main.SCREEN.blit(self.image, self.rect)
        Main.SCREEN.blit(self.hat, self.hatRect)

    def load_images(self):
        images = {0: ['1_2', '1_1'],
                  1: ['2_2', '2_1'],
                  2: ['2_2', '2_1'],
                  3: ['3_1', '3_2'],
                  4: ['3_1', '3_2'],
                  }
        img1, img2 = (Main.IMAGES['enemy{}'.format(img_num)] for img_num in
                      images[self.row])
        self.images.append( transform.scale(img1, (40, 35)))
        self.images.append( transform.scale(img2, (40, 35)))
        self.hats.append(transform.scale(Main.IMAGES['hat1'], (45, 35)))
        self.hats.append(transform.scale(Main.IMAGES['hat2'], (45, 35)))
        self.hats.append(transform.scale(Main.IMAGES['hat3'], (45, 35)))