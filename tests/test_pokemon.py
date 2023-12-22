import unittest 
from source.pokemon import Pokemon

import io
import sys

class TestPokemon(unittest.TestCase):
    def setUp(self):
        self.pokemon1 = Pokemon("Jake", 54, "Fire")
        self.pokemon2 = Pokemon("Luca", 1, "Water")
        self.pokemon3 = Pokemon("Maria", 999, "Plant")
        self.pokemon4 = Pokemon("", -1, "Invalid")

        self.capturedOutput = io.StringIO()  
        sys.stdout = self.capturedOutput
  
    def tearDown(self):
        del self.pokemon1
        del self.pokemon2
        del self.pokemon3
        del self.pokemon4

        sys.stdout = sys.__stdout__ 

    def test_levelUp(self):
        self.assertEqual(self.pokemon1._level, 1, "Level of a new pokemon must be 1")
        self.assertEqual(self.pokemon1._maxHealth, 100, "MaxHealth of a new pokemon must be 100")
        self.assertEqual(self.pokemon1._health, 100, "Health of a new pokemon must be 100")

        self.pokemon1._levelUp()  
        self.assertEqual(self.capturedOutput.getvalue(), f"Pokemon Jake is now level 2!\n")

        self.assertEqual(self.pokemon1._level, 2)
        self.assertEqual(self.pokemon1._maxHealth, 110)
        self.assertEqual(self.pokemon1._health, 110)

        self.assertEqual(self.pokemon2._level, 1, "Level of a new pokemon must be 1")
        self.assertEqual(self.pokemon2._maxHealth, 100, "MaxHealth of a new pokemon must be 100")
        self.assertEqual(self.pokemon2._health, 100, "Health of a new pokemon must be 100")
