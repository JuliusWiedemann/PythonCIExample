"""
Main entry point of the pokemon game
Sets the correct path for the module and test suit
"""

import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sourcePath = os.path.join(path, "source")
sys.path.insert(0, sourcePath)

# pylint: disable=C0413 # Import must be placed after adding the correct path to sys.path
from source import game

if __name__ == "__main__":
    game.main()
