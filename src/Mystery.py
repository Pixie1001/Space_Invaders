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

class Mystery( sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        self.image = Main.IMAGES['mystery']
        self.image =  transform.scale(self.image, (75, 35))
        self.rect = self.image.get_rect(topleft=(-80, 45))
        self.row = 5
        self.moveTime = 25000
        self.direction = 1
        self.timer = time.get_ticks()
        self.mysteryEntered = mixer.Sound(Main.SOUND_PATH + 'mysteryentered.wav')
        self.mysteryEntered.set_volume(0.3)
        self.playSound = True

    def update(self, keys, currentTime, *args):
        resetTimer = False
        passed = currentTime - self.timer
        if passed > self.moveTime:
            if (self.rect.x < 0 or self.rect.x > 800) and self.playSound:
                self.mysteryEntered.play()
                self.playSound = False
            if self.rect.x < 840 and self.direction == 1:
                self.mysteryEntered.fadeout(4000)
                self.rect.x += 2
                Main.SCREEN.blit(self.image, self.rect)
            if self.rect.x > -100 and self.direction == -1:
                self.mysteryEntered.fadeout(4000)
                self.rect.x -= 2
                Main.SCREEN.blit(self.image, self.rect)

        if self.rect.x > 830:
            self.playSound = True
            self.direction = -1
            resetTimer = True
        if self.rect.x < -90:
            self.playSound = True
            self.direction = 1
            resetTimer = True
        if passed > self.moveTime and resetTimer:
            self.timer = currentTime