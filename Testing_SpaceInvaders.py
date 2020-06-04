import unittest
from pygame import *
import sys
from os.path import abspath, dirname, join
from random import choice

sys.path.append(dirname(dirname(__file__)))

from src import Main
from src import Blocker
from src import Bullet
from src import Enemy
from src import EnemiesGroup
from src import EnemyExplosion
from src import Life
from src import Mystery
from src import MysteryExplosion
from src import Ship
from src import ShipExplosion
from src import Text

class Test_Testing_SpaceInvaders(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game = Main.SpaceInvaders()
        Main.SpaceInvaders.reset(self.game, 0)

    def test_calculate_score_0(self):
        input = 0
        expected = 30
        actual = Main.SpaceInvaders.calculate_score(self.game, input)
        self.assertEqual(actual, expected)
    
    def test_calculate_score_1(self):
        input = 1
        expected = 20
        actual = Main.SpaceInvaders.calculate_score(self.game, input)
        self.assertEqual(actual, expected)

    def test_calculate_score_2(self):
        input = 2
        expected = 20
        actual = Main.SpaceInvaders.calculate_score(self.game, input)
        self.assertEqual(actual, expected)

    def test_calculate_score_3(self):
        input = 3
        expected = 10
        actual = Main.SpaceInvaders.calculate_score(self.game, input)
        self.assertEqual(actual, expected)

    def test_calculate_score_4(self):
        input = 4
        expected = 10
        actual = Main.SpaceInvaders.calculate_score(self.game, input)
        self.assertEqual(actual, expected)

    def test_calculate_score_5(self):
        input = 5
        expected = 10
        actual = Main.SpaceInvaders.calculate_score(self.game, input)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
