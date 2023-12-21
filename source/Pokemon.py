class Pokemon:
    def __init__(self, name, number, pokeType):
        self._name = name
        self._number = number
        self._pokeType = pokeType
        self._health = 100
        self._maxHealth = 100
        self._level = 1
        self._levelProgress = 0
        self._isAlive = True

    def __eq__(self, other):
        return self.__name == other.__name

    def __str__(self):
        return f"Hi, my name is {self._name}. I am a {self._pokeType} Pokemon!\nLevel: {self._level}\nMax health: {self._maxHealth}\nCurrent health: {self._health}"

    def _receiveDamage(self, damage):
        print(f"{self._name} looses {damage} health!")
        self._health -= damage
        if self._health <= 0:
            self._isAlive = False
            print(f"Pokemon {self.__name} is dead!")

    def _attack(self, opponent, damage):
        if self._isAlive == False:
            print("Pokemon is dead already!")
        elif opponent.getIsAlive() == False:
            print("Opponent is dead already!")
        else:
            print(f"{self._name} attacks {opponent.getName()}!")
            attackFactor = self.getAttackFactor(self._pokeType, opponent.getPokeType())
            attackDamage = damage * attackFactor
            if attackFactor == 1:
                print("Effective")
            elif attackFactor == 0.5:
                print("Not very effective")
            elif attackFactor == 2:
                print("Very effective")
            opponent._receiveDamage(attackDamage)
            self.earnXp(attackDamage)

    def _levelUp(self):
        self._level += 1
        print(f"Pokemon {self._name} is now level {self._level}!")
        self._maxHealth += 10
        self._health += 10

    def earnXp(self, xp):
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

    @staticmethod
    def getAttackFactor(attackType, defendType):
        attackTypes = {
            ("Water", "Fire"): 2,
            ("Fire", "Water"): 0.5,
            ("Plant", "Water"): 2,
            ("Water", "Plant"): 0.5,
            ("Fire", "Plant"): 2,
            ("Plant", "Fire"): 0.5,
        }
        return attackTypes.get((attackType, defendType), 1)


class FirePokemon(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number, "Fire")

    def inferno(self, opponent):
        self._attack(opponent, 15)

class WaterPokemon(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number, "Water")

    def waterGun(self, opponent):
        self._attack(opponent, 20)

class PlantPokemon(Pokemon):
    def __init__(self, name, number):
        super().__init__(name, number, "Plant")

    def appleAcid(self, opponent):
        self._attack(opponent, 10)

