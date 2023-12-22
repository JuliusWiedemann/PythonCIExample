"""
Module to control pokemon and different poke types.
"""

import random

class Pokemon:
    """
    Class with all relevant data for a Pokemon.
    Functions to attack another Pokemon.
    """
    def __init__(self, name, number, pokeType):
        self._name = name
        self._number = number
        self._pokeType = pokeType
        self._health = 100
        self._maxHealth = 100
        self._level = 1
        self._levelProgress = 0
        self._isAlive = True
        self._strength = random.randint(1, 30)

    def __eq__(self, other):
        return self._name == other.getName()

    def __str__(self):
        return f"Name: {self._name}\nType: {self._pokeType}\nLevel: {self._level}\nHealth: {self._health}\nStrength: {self._strength}"

    def _levelUp(self):
        self._level += 1
        print(f"Pokemon {self._name} is now level {self._level}!")
        self._maxHealth += 10
        self._health += 10

    def attack(self, opponent):
        """
        Attacks another pokemon by calculating the attack factor.
        After the fight, the attacking pokemon receives XP.
        """
        if not self._isAlive:
            print("Pokemon is dead already!")
        elif not opponent.getIsAlive():
            print("Opponent is dead already!")
        else:
            print(f"{self._name} attacks {opponent.getName()}!")
            attackFactor = self.getAttackFactor(self._pokeType, opponent.getPokeType())
            attackDamage = self._strength * attackFactor
            if attackFactor == 1:
                print("Effective")
            elif attackFactor == 0.5:
                print("Not very effective")
            elif attackFactor == 2:
                print("Very effective")
            opponent.receiveDamage(attackDamage)
            self.earnXp(attackDamage)

    def receiveDamage(self, damage):
        """
        Reduces the health of a pokemon by amount of damage.
        and checks if the pokemon is dead.
        """
        print(f"{self._name} looses {damage} health!")
        self._health -= damage
        if self._health <= 0:
            self._isAlive = False
            print(f"Pokemon {self._name} is dead!")

    def earnXp(self, xp):
        """
        Training of a pokemon.
        Earns XP and increases the level of a pokemon.
        """
        self._levelProgress += xp

        while self._levelProgress >= 100:
            self._levelProgress -= 100
            self._levelUp()

    def useHealthPotion(self):
        self._health = self._maxHealth
        print(f"Pokemon {self._name} was healed.")

    def getName(self):
        return self._name

    def getPokeType(self):
        return self._pokeType

    def getHealth(self):
        return self._health

    def getLevel(self):
        return self._level

    def getIsAlive(self):
        return self._isAlive

    def getStrength(self):
        return self._strength

    @staticmethod
    def getAttackFactor(attackType, defendType):
        """
        RReturn the attack factor for a combination of types.
        Returns 1 if no special combination is available.
        """
        attackTypes = {
            ("Water", "Fire"): 2,
            ("Fire", "Water"): 0.5,
            ("Plant", "Water"): 2,
            ("Water", "Plant"): 0.5,
            ("Fire", "Plant"): 2,
            ("Plant", "Fire"): 0.5,
        }
        return attackTypes.get((attackType, defendType), 1)
