import unittest
from unittest.mock import patch
import main
from source.game import *

import io
import sys

class TestGame(unittest.TestCase):
    @staticmethod
    def helper_resetStringOutput(mock_stdout):
        mock_stdout.truncate(0)
        mock_stdout.seek(0)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_welcome(self, mock_stdout):
        welcome()
        self.assertEqual(mock_stdout.getvalue().strip(), "Welcome to the pokemon game!")

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_createNewPokemon_name(self, mock_stdout, mock_input):
        mock_input.return_value = None
        returnValue = createNewPokemon()
        self.assertEqual(returnValue, False)
        self.assertEqual(mock_stdout.getvalue().strip(), "Invalid name")

        self.helper_resetStringOutput(mock_stdout)

        mock_input.return_value = ""
        returnValue = createNewPokemon()
        self.assertEqual(returnValue, False)
        self.assertEqual(mock_stdout.getvalue().strip(), "Invalid name")
