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

#Handles explosion animatiosn for default enemy types
class EnemyExplosion( sprite.Sprite):
    def __init__(self, enemy, *groups):
        super(EnemyExplosion, self).__init__(*groups)
        self.image =  transform.scale(self.get_image(enemy.row), (40, 35))
        self.image2 =  transform.scale(self.get_image(enemy.row), (50, 45))
        self.rect = self.image.get_rect(topleft=(enemy.rect.x, enemy.rect.y))
        self.timer = time.get_ticks()

    #Loads frames for explosion animation
    @staticmethod
    def get_image(row):
        img_colors = ['purple', 'blue', 'blue', 'green', 'green']
        return Main.IMAGES['explosion{}'.format(img_colors[row])]

    def update(self, current_time, *args):
        passed = current_time - self.timer
        if passed <= 100:
            Main.SCREEN.blit(self.image, self.rect)
        elif passed <= 200:
            Main.SCREEN.blit(self.image2, (self.rect.x - 6, self.rect.y - 6))
        elif 400 < passed:
            self.kill()