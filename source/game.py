"""
The Pokemon Game
"""

import time
# pylint: disable=E0401 # False positive
from pokemon import Pokemon

def welcome():
    """
    Prints the welcome message
    """
    print("Welcome to the pokemon game!")

def createNewPokemon():
    """
    Lets the user create a new pokemon via text input
    Returns the new pokemon
    """
    name = input("Please enter the name of your pokemon: ")
    if name is None or name == "":
        print("Invalid name")
        return False

    try:
        number = int(input("Please enter the number of your pokemon: "))
    except ValueError:
        print("Invalid number")
        return False

    pokeType = input("Please enter the type of your pokemon: ")

    newPokemon = Pokemon(name, number, pokeType)
    print(f"Your created the following pokemon: {newPokemon}")
    return newPokemon

def attackPokemon(pokemonStorage):
    """
    Allows the user to attack a pokemon
    """
    if (len(pokemonStorage.keys())) < 2:
        print("You need at least 2 pokemon to fight.")
        return False

    name1 = input("Enter the name of your pokemon: ")
    pokemon1 = getPokemon(pokemonStorage, name1)
    if not pokemon1:
        return False

    name2 = input("Enter the name of the pokemon to attack: ")
    pokemon2 = getPokemon(pokemonStorage, name2)
    if not pokemon2:
        return False

    pokemon1.attack(pokemon2)
    return True

def viewPokemonStats(pokemonStorage):
    """
    Allows the user to view stats of one pokemon he created
    """
    name = input("Enter the name of your pokemon: ")

    pokemon = getPokemon(pokemonStorage, name)
    if pokemon:
        print(pokemon)

def getPokemon(pokemonStorage, name):
    """
    Searches a pokemon by name from the pokemon storage and returns it
    Returns false if pokemon does not exist
    """
    pokemon = pokemonStorage.get(name)
    if pokemon is None:
        print(f"Sorry. The pokemon {name} does not exist.")
        return False
    return pokemon

def main():
    """
    Creates while loop which lets the user create and fight pokemon via text input
    """
    game = True
    pokemonStorage = {}

    welcome()
    while game:
        print("\n\n--------------------------------\n\n")

        choice = input("What to you want to do?\n1: Create new pokemon\n2: Attack a pokemon\n3: View Stats\nQ: Quit Game\n")

        if choice == "1":
            newPokemon = createNewPokemon()
            if newPokemon:
                pokemonStorage[newPokemon.getName()] = newPokemon
        elif choice == "2":
            attackPokemon(pokemonStorage)
        elif choice == "3":
            viewPokemonStats(pokemonStorage)
        elif choice in ("q", "Q"):
            game = False
            print("Bye")
        else:
            print("Invalid option.")

        time.sleep(1)

if __name__ == "__main__":
    main()
