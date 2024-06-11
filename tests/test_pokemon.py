# pylint: disable=C,protected-access,unused-argument,too-many-public-methods,wildcard-import,unused-wildcard-import

import unittest 
from unittest.mock import patch
from source.pokemon import Pokemon

import io

class TestPokemon(unittest.TestCase):
    def setUp(self):
        self.pokemon1 = Pokemon("Jake", 54, "Fire")
        self.pokemon2 = Pokemon("Luca", 1, "Water")
        self.pokemon3 = Pokemon("Maria", 999, "Plant")
        self.pokemon4 = Pokemon("", -1, "Invalid")
  
    def tearDown(self):
        del self.pokemon1
        del self.pokemon2
        del self.pokemon3
        del self.pokemon4

    def test_init(self):
        self.assertEqual(self.pokemon1._name, "Jake")
        self.assertEqual(self.pokemon1._number, 54)
        self.assertEqual(self.pokemon1._pokeType, "Fire")
        self.assertEqual(self.pokemon1._health, 100)
        self.assertEqual(self.pokemon1._maxHealth, 100)
        self.assertEqual(self.pokemon1._level, 1)
        self.assertEqual(self.pokemon1._levelProgress, 0)
        self.assertGreaterEqual(self.pokemon1._strength, 1)
        self.assertLessEqual(self.pokemon1._strength, 30)

    def test_eq(self):
        self.assertEqual(self.pokemon1 == self.pokemon2, False)
        self.pokemon2._name = self.pokemon1._name
        self.assertEqual(self.pokemon1 == self.pokemon2, True)

        self.assertEqual(self.pokemon3 == self.pokemon4, False)
        self.assertEqual(self.pokemon3 == self.pokemon3, True)

    def test_str(self):
        self.pokemon1._strength = 20

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            print(self.pokemon1)
            self.assertEqual(mock_stdout.getvalue().strip(), "Name: Jake\nType: Fire\nLevel: 1\nHealth: 100\nStrength: 20")

    def test_levelUp(self):
        self.assertEqual(self.pokemon1._level, 1, "Level of a new pokemon must be 1")
        self.assertEqual(self.pokemon1._maxHealth, 100, "MaxHealth of a new pokemon must be 100")
        self.assertEqual(self.pokemon1._health, 100, "Health of a new pokemon must be 100")

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.pokemon1._levelUp()  
            self.assertEqual(mock_stdout.getvalue().strip(), "Pokemon Jake is now level 2!")

        self.assertEqual(self.pokemon1._level, 2)
        self.assertEqual(self.pokemon1._maxHealth, 110)
        self.assertEqual(self.pokemon1._health, 110)

        self.assertEqual(self.pokemon2._level, 1, "Level of a new pokemon must be 1")
        self.assertEqual(self.pokemon2._maxHealth, 100, "MaxHealth of a new pokemon must be 100")
        self.assertEqual(self.pokemon2._health, 100, "Health of a new pokemon must be 100")

    def test_attack_attackerDead(self):
        self.pokemon1._isAlive = False

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.pokemon1.attack(self.pokemon2)
            self.assertEqual(mock_stdout.getvalue().strip(), "Pokemon is dead already!")

    def test_attack_opponentDead(self):
        self.pokemon1._isAlive = False

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.pokemon2.attack(self.pokemon1)
            self.assertEqual(mock_stdout.getvalue().strip(), "Opponent is dead already!")
    
    @patch("source.pokemon.Pokemon.getAttackFactor", return_value = 0)
    @patch("source.pokemon.Pokemon.receiveDamage")
    def test_attack_printAttackMessage(self, mock_receiveDamage, mock_getAttackFactor):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.pokemon1.attack(self.pokemon2)
            self.assertEqual(mock_stdout.getvalue().strip(), "Jake attacks Luca!")

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.pokemon2.attack(self.pokemon1)
            self.assertEqual(mock_stdout.getvalue().strip(), "Luca attacks Jake!")

    @patch("source.pokemon.Pokemon.getAttackFactor", side_effect = [2, 1, 4])
    @patch("source.pokemon.Pokemon.receiveDamage")
    @patch("source.pokemon.Pokemon.earnXp")
    def test_attack_printAttackFactor(self, mock_earnXp, mock_receiveDamage, mock_getAttackFactor):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.pokemon1.attack(self.pokemon2)
            self.assertEqual(mock_stdout.getvalue().strip(), "Jake attacks Luca!\nEffective")

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.pokemon1.attack(self.pokemon2)
            self.assertEqual(mock_stdout.getvalue().strip(), "Jake attacks Luca!\nNot very effective")

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.pokemon1.attack(self.pokemon2)
            self.assertEqual(mock_stdout.getvalue().strip(), "Jake attacks Luca!\nVery effective")

    @patch("source.pokemon.Pokemon.getAttackFactor", return_value = 2)
    @patch("source.pokemon.Pokemon.receiveDamage")
    @patch("source.pokemon.Pokemon.earnXp")
    def test_attack_calculateAttackDamage(self, mock_earnXp, mock_receiveDamage, mock_getAttackFactor):
        self.pokemon1._strength = 10

        self.pokemon1.attack(self.pokemon2)
        mock_getAttackFactor.assert_called_once()
        mock_receiveDamage.assert_called_with(20)
        mock_earnXp.assert_called_with(20)

    def test_receiveDamage_alive(self):
        self.assertEqual(self.pokemon1._health, 100)

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.pokemon1.receiveDamage(10)
            self.assertEqual(mock_stdout.getvalue().strip(), "Jake looses 10 health!")
            self.assertEqual(self.pokemon1._health, 90)
            self.assertEqual(self.pokemon1._isAlive, True)  

    def test_receiveDamage_dead(self):
        self.assertEqual(self.pokemon1._health, 100)

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.pokemon1.receiveDamage(100)
            self.assertEqual(mock_stdout.getvalue().strip(), "Jake looses 100 health!\nPokemon Jake is dead!")
            self.assertEqual(self.pokemon1._health, 0)  
            self.assertEqual(self.pokemon1._isAlive, False)    

    @patch("source.pokemon.Pokemon._levelUp")
    def test_earnXp(self, mock_levelUp):
        self.assertEqual(self.pokemon1._levelProgress, 0)
        self.pokemon1.earnXp(90)
        self.assertEqual(self.pokemon1._levelProgress, 90)
        mock_levelUp.assert_not_called()

        mock_levelUp.reset_mock()

        self.assertEqual(self.pokemon2._levelProgress, 0)
        self.pokemon2.earnXp(100)
        self.assertEqual(self.pokemon2._levelProgress, 0)
        mock_levelUp.assert_called_once()

        mock_levelUp.reset_mock()

        self.assertEqual(self.pokemon3._levelProgress, 0)
        self.pokemon3.earnXp(330)
        self.assertEqual(self.pokemon3._levelProgress, 30)
        self.assertEqual(mock_levelUp.call_count, 3)

    def test_useHealthPotion(self):
        self.pokemon1._health = 0

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.pokemon1.useHealthPotion()
            self.assertEqual(self.pokemon1._health, 100)
            self.assertEqual(mock_stdout.getvalue().strip(), "Pokemon Jake was healed.")

        self.pokemon2._health = 10
        self.pokemon2._maxHealth = 42

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.pokemon2.useHealthPotion()
            self.assertEqual(self.pokemon2._health, 42)
            self.assertEqual(mock_stdout.getvalue().strip(), "Pokemon Luca was healed.")

    def test_getName(self):
        self.assertEqual(self.pokemon1.getName(), "Jake")
        self.assertEqual(self.pokemon4.getName(), "")

    def test_getPokeType(self):
        self.assertEqual(self.pokemon1.getPokeType(), "Fire")
        self.assertEqual(self.pokemon4.getPokeType(), "Invalid")

    def test_getHealth(self):
        self.assertEqual(self.pokemon1.getHealth(), 100)

        self.pokemon4._health = 42
        self.assertEqual(self.pokemon4.getHealth(), 42)

    def test_getLevel(self):
        self.assertEqual(self.pokemon1.getLevel(), 1)

        self.pokemon4._level = 42
        self.assertEqual(self.pokemon4.getLevel(), 42)

    def test_getIsAlive(self):
        self.assertEqual(self.pokemon1.getIsAlive(), True)

        self.pokemon4._isAlive = False
        self.assertEqual(self.pokemon4.getIsAlive(), False)

    def test_getStrength(self):
        self.pokemon4._strength = 42
        self.assertEqual(self.pokemon4.getStrength(), 42)

    def test_getAttackFactor(self):
        self.assertEqual(Pokemon.getAttackFactor("", "Hi"), 2)
        self.assertEqual(Pokemon.getAttackFactor("water", "fire"), 2)
        self.assertEqual(Pokemon.getAttackFactor("20", "Plant"), 2)
        self.assertEqual(Pokemon.getAttackFactor("\n", "?"), 2)

        self.assertEqual(Pokemon.getAttackFactor("Water", "Fire"), 4)
        self.assertEqual(Pokemon.getAttackFactor("Plant", "Water"), 4)
        self.assertEqual(Pokemon.getAttackFactor("Fire", "Plant"), 4)

        self.assertEqual(Pokemon.getAttackFactor("Fire", "Water"), 1)
        self.assertEqual(Pokemon.getAttackFactor("Water", "Plant"), 1)
        self.assertEqual(Pokemon.getAttackFactor("Plant", "Fire"), 1)
