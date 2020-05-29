from pygame import *
import sys
from os.path import abspath, dirname, join
from random import choice

sys.path.append(dirname(dirname(__file__)) + '/src/')

from Blocker import *
from Bullet import *
from Enemy import *
from EnemiesGroup import *
from EnemyExplosion import *
import Main
from Mystery import *
from MysteryExplosion import *
from Ship import *
from ShipExplosion import *
from Text import *

class Life(sprite.Sprite):
    def __init__(self, xpos, ypos):
        sprite.Sprite.__init__(self)
        self.image = Main.IMAGES['ship']
        self.image = transform.scale(self.image, (23, 23))
        self.rect = self.image.get_rect(topleft=(xpos, ypos))

    def update(self, *args):
        Main.SCREEN.blit(self.image, self.rect)