from pygame import *
import sys
from os.path import abspath, dirname, join
from random import choice

sys.path.append(dirname(dirname(__file__)) + '/src/')

from Blocker import *
from Bullet import *
from EnemiesGroup import *
from Enemy import *
from EnemyExplosion import *
import Main
from Mystery import *
from MysteryExplosion import *
from Ship import *
from ShipExplosion import *
from Text import *

class Blocker( sprite.Sprite):
    def __init__(self, size, color, row, column):
        sprite.Sprite.__init__(self)
        self.height = size
        self.width = size
        self.color = color
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.row = row
        self.column = column

    def update(self, keys, *args):
        Main.SCREEN.blit(self.image, self.rect)