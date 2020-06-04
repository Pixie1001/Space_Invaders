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

#Handles UFO enemy type's explosion animation
class MysteryExplosion( sprite.Sprite):
    def __init__(self, mystery, score, *groups):
        super(MysteryExplosion, self).__init__(*groups)
        self.text = Text(Main.FONT, 20, str(score), Main.WHITE,
                         mystery.rect.x + 20, mystery.rect.y + 6)
        self.timer = time.get_ticks()

    def update(self, current_time, *args):
        passed = current_time - self.timer
        if passed <= 200 or 400 < passed <= 600:
            self.text.draw(Main.SCREEN)
        elif 600 < passed:
            self.kill()