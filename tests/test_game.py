# pylint: disable=C,protected-access,unused-argument,too-many-public-methods,wildcard-import,unused-wildcard-import

import unittest
from unittest.mock import patch, call
import main
from source.game import *

import io

class TestGame(unittest.TestCase):
    def setUp(self):
        self.pokemonStorage0 = {}
        self.pokemonStorage1 = {"a": 1}
        self.pokemonStorage2 = {"a": 1, "b": 2}

        self.pokemon1 = Pokemon("1", 1, "Type 1")
        self.pokemon2 = Pokemon("2", 2, "Type 2")
  
    def tearDown(self):
        del self.pokemonStorage0
        del self.pokemonStorage1
        del self.pokemonStorage2

        del self.pokemon1
        del self.pokemon2

    def test_welcome(self):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            welcome()
            self.assertEqual(mock_stdout.getvalue().strip(), "Welcome to the pokemon game!")

    @patch("builtins.input")
    def test_createNewPokemon_name(self, mock_input):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            mock_input.return_value = None
            returnValue = createNewPokemon()
            self.assertEqual(returnValue, False)
            self.assertEqual(mock_stdout.getvalue().strip(), "Invalid name")

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            mock_input.return_value = ""
            returnValue = createNewPokemon()
            self.assertEqual(returnValue, False)
            self.assertEqual(mock_stdout.getvalue().strip(), "Invalid name")
    
    @patch("builtins.input", side_effect = ["Pokemon", "a"])
    def test_createNewPokemon_number(self, mock_input):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            returnValue = createNewPokemon()
            self.assertEqual(returnValue, False)
            self.assertEqual(mock_stdout.getvalue().strip(), "Invalid number")

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            mock_input.side_effect = ["Pokemon", ""]
            returnValue = createNewPokemon()
            self.assertEqual(returnValue, False)
            self.assertEqual(mock_stdout.getvalue().strip(), "Invalid number")

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            mock_input.side_effect = ["Pokemon", "1.1.0"]
            returnValue = createNewPokemon()
            self.assertEqual(returnValue, False)
            self.assertEqual(mock_stdout.getvalue().strip(), "Invalid number")

    @patch("builtins.input")
    def test_createNewPokemon_object(self, mock_input):
        mock_input.side_effect = ["Name", 1234, "Type"]
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:   
            newPokemon = createNewPokemon()
            self.assertEqual(mock_stdout.getvalue().strip(), f"You created the following pokemon: {newPokemon}")
            self.assertEqual(newPokemon._name, "Name")
            self.assertEqual(newPokemon._number, 1234)
            self.assertEqual(newPokemon._pokeType, "Type")

    @patch("builtins.input")
    def test_attackPokemon_amount(self, mock_input):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            returnValue = attackPokemon(self.pokemonStorage0)
            self.assertEqual(returnValue, False)
            self.assertEqual(mock_stdout.getvalue().strip(), "You need at least 2 pokemon to fight.")

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            returnValue = attackPokemon(self.pokemonStorage1)
            self.assertEqual(returnValue, False)
            self.assertEqual(mock_stdout.getvalue().strip(), "You need at least 2 pokemon to fight.")
 
    @patch("source.game.getPokemon", side_effect = [False, True])
    @patch("builtins.input", side_effect = ["PokemonName1", "PokemonName2"])
    def test_attackPokemon_invalidName1(self, mock_input, mock_getPokemon):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            returnValue = attackPokemon(self.pokemonStorage2)
            self.assertEqual(returnValue, False)
            self.assertEqual(mock_stdout.getvalue().strip(), "")
            mock_getPokemon.assert_called_once_with(self.pokemonStorage2, "PokemonName1")

    @patch("source.game.getPokemon", side_effect = [True, False])
    @patch("builtins.input", side_effect = ["PokemonName1", "PokemonName2"])
    def test_attackPokemon_invalidName2(self, mock_input, mock_getPokemon):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            returnValue = attackPokemon(self.pokemonStorage2)
            self.assertEqual(returnValue, False)
            self.assertEqual(mock_stdout.getvalue().strip(), "")

        expectedCalls = [call(self.pokemonStorage2, "PokemonName1"), call(self.pokemonStorage2, "PokemonName2")]
        mock_getPokemon.assert_has_calls(expectedCalls)

    @patch.object(Pokemon, "attack")
    @patch("source.game.getPokemon", return_value = True)
    @patch("builtins.input", return_value = " ")
    def test_attackPokemon_valid(self, mock_input, mock_getPokemon, mock_attack):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            mock_getPokemon.side_effect = [self.pokemon1, self.pokemon2]
            returnValue = attackPokemon(self.pokemonStorage2)
            self.assertEqual(returnValue, True)
            self.assertEqual(mock_stdout.getvalue().strip(), "")
            mock_attack.assert_called_once_with(self.pokemon2)

        mock_attack.reset_mock()

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            mock_getPokemon.side_effect = [self.pokemon2, self.pokemon1]
            returnValue = attackPokemon(self.pokemonStorage2)
            self.assertEqual(returnValue, True)
            self.assertEqual(mock_stdout.getvalue().strip(), "")
            mock_attack.assert_called_once_with(self.pokemon1)

    @patch("source.game.getPokemon", side_effect = [False, False, "PokemonName"])
    @patch("builtins.input", side_effect = ["Call1", "Call2", "Call3"])
    def test_viewPokemonStats(self, mock_input, mock_getPokemon):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            viewPokemonStats(self.pokemonStorage0)
            mock_getPokemon.assert_called_once_with(self.pokemonStorage0, "Call1")
            self.assertEqual(mock_stdout.getvalue().strip(), "")

            viewPokemonStats(self.pokemonStorage1)
            mock_getPokemon.assert_called_with(self.pokemonStorage1, "Call2")
            self.assertEqual(mock_stdout.getvalue().strip(), "")

            viewPokemonStats(self.pokemonStorage2)
            mock_getPokemon.assert_called_with(self.pokemonStorage2, "Call3")
            self.assertEqual(mock_stdout.getvalue().strip(), "PokemonName")

    def test_getPokemon_invalid(self):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            returnValue = getPokemon(self.pokemonStorage0, "a")
            self.assertEqual(returnValue, False)
            self.assertEqual(mock_stdout.getvalue().strip(), "Sorry. The pokemon a does not exist.")

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            returnValue = getPokemon(self.pokemonStorage2, "c")
            self.assertEqual(returnValue, False)
            self.assertEqual(mock_stdout.getvalue().strip(), "Sorry. The pokemon c does not exist.")

    def test_getPokemon_valid(self):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            returnValue = getPokemon(self.pokemonStorage1, "a")
            self.assertEqual(returnValue, 1)
            self.assertEqual(mock_stdout.getvalue().strip(), "")

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            returnValue = getPokemon(self.pokemonStorage2, "b")
            self.assertEqual(returnValue, 2)
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch("source.game.welcome")
    @patch("builtins.input", return_value = "Q")
    def test_main_welcome(self, mock_input, mock_welcome):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            main()
            mock_welcome.assert_called_once()
            self.assertEqual(mock_stdout.getvalue(), "\n\n--------------------------------\n\n\nBye\n")

    @patch("source.game.createNewPokemon")
    @patch("builtins.input", side_effect = ["1", "Q"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_main_choice1(self, mock_stdout, mock_input, mock_createNewPokemon):
        main()
        mock_createNewPokemon.assert_called_once()

    @patch("source.game.attackPokemon")
    @patch("builtins.input", side_effect = ["2", "Q"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_main_choice2(self, mock_stdout, mock_input, mock_attackPokemon):
        main()
        mock_attackPokemon.assert_called_once_with(self.pokemonStorage0)

    @patch("source.game.viewPokemonStats")
    @patch("builtins.input", side_effect = ["3", "Q"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_main_choice3(self, mock_stdout, mock_input, mock_viewPokemonStats):
        main()
        mock_viewPokemonStats.assert_called_once_with(self.pokemonStorage0)

    @patch("source.game.welcome")
    @patch("builtins.input", side_effect = ["q", "Q"])
    def test_main_choiceQuit(self, mock_input, mock_welcome):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            main()
            self.assertEqual(mock_stdout.getvalue(), "\n\n--------------------------------\n\n\nBye\n")

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            main()
            self.assertEqual(mock_stdout.getvalue(), "\n\n--------------------------------\n\n\nBye\n")

    @patch("source.game.welcome")
    @patch("builtins.input", side_effect = ["4", "Q", "", "Q"])
    def test_main_choiceInvalid(self, mock_input, mock_welcome):
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            main()
            self.assertEqual(mock_stdout.getvalue(), "\n\n--------------------------------\n\n\nInvalid option.\n\n\n--------------------------------\n\n\nBye\n")

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            main()
            self.assertEqual(mock_stdout.getvalue(), "\n\n--------------------------------\n\n\nInvalid option.\n\n\n--------------------------------\n\n\nBye\n")
