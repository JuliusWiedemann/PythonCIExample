from Pokemon import WaterPokemon, FirePokemon, PlantPokemon

def main():
    #Create pokemons
    shiggy = WaterPokemon("Shiggy", 7)
    bisasam = PlantPokemon("Bisasam", 2)

    #Level Up pokemons
    bisasam.earnXp(150)

    #Attack other pokemons
    shiggy.waterGun(bisasam)
    bisasam.appleAcid(shiggy)

    #Use health potion
    bisasam.useHealthPotion()

    #Print pokemon infos
    print(bisasam)
    print(shiggy)

if __name__ == "__main__":
    main()