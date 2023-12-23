import unittest
from unittest.mock import patch
import main
from source.game import *

import io
import sys

class TestGame(unittest.TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_welcome(self, mock_stdout):
        welcome()
        self.assertEqual(mock_stdout.getvalue().strip(), "Welcome to the pokemon game!")

