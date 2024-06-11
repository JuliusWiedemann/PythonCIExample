"""
Module to control pokemon and different poke types.
"""
import random

class Pokemon:
    """
    Class with all relevant data for a Pokemon.
    Functions to attack another Pokemon.
    """
    def __init__(self, name: str, number: int, pokeType: str):
        self._name = name
        self._number = number
        self._pokeType = pokeType
        self._health: int = 100
        self._maxHealth: int = 100
        self._level: int = 1
        self._levelProgress: int = 0
        self._isAlive: bool = True
        self._strength: int = random.randint(1, 30)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pokemon):
            return NotImplemented
        return self._name == other.getName()

    def __str__(self) -> str:
        return f"Name: {self._name}\nType: {self._pokeType}\nLevel: {self._level}\nHealth: {self._health}\nStrength: {self._strength}"

    def _levelUp(self) -> None:
        self._level += 1
        print(f"Pokemon {self._name} is now level {self._level}!")
        self._maxHealth += 10
        self._health += 10

    def attack(self, opponent: "Pokemon") -> None:
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
            attackFactor: int = self.getAttackFactor(self._pokeType, opponent.getPokeType())
            attackDamage: int = self._strength * attackFactor
            if attackFactor == 2:
                print("Effective")
            elif attackFactor == 1:
                print("Not very effective")
            elif attackFactor == 4:
                print("Very effective")
            opponent.receiveDamage(attackDamage)
            self.earnXp(attackDamage)

    def receiveDamage(self, damage: int) -> None:
        """
        Reduces the health of a pokemon by amount of damage.
        and checks if the pokemon is dead.
        """
        print(f"{self._name} looses {damage} health!")
        self._health -= damage
        if self._health <= 0:
            #Intentional Bug
            #self._isAlive = False
            print(f"Pokemon {self._name} is dead!")

    def earnXp(self, xp: int) -> None:
        """
        Training of a pokemon.
        Earns XP and increases the level of a pokemon.
        """
        self._levelProgress += xp

        while self._levelProgress >= 100:
            self._levelProgress -= 100
            self._levelUp()

    def useHealthPotion(self) -> None:
        self._health = self._maxHealth
        print(f"Pokemon {self._name} was healed.")

    def getName(self) -> str:
        return self._name

    def getPokeType(self) -> str:
        return self._pokeType

    def getHealth(self) -> int:
        return self._health

    def getLevel(self) -> int:
        return self._level

    def getIsAlive(self) -> bool:
        return self._isAlive

    def getStrength(self) -> int:
        return self._strength

    @staticmethod
    def getAttackFactor(attackType: str, defendType: str) -> int:
        """
        Return the attack factor for a combination of types.
        Returns 1 if no special combination is available.
        """
        attackTypes = {
            ("Water", "Fire"): 4,
            ("Fire", "Water"): 1,
            ("Plant", "Water"): 4,
            ("Water", "Plant"): 1,
            ("Fire", "Plant"): 4,
            ("Plant", "Fire"): 1,
        }
        return attackTypes.get((attackType, defendType), 2)
