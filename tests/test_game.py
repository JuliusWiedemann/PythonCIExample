import unittest 
import main
from source.game import *

import io
import sys

class TestGame(unittest.TestCase):
    def setUp(self):
        self.capturedOutput = io.StringIO()  
        sys.stdout = self.capturedOutput
  
    def tearDown(self):
        sys.stdout = sys.__stdout__ 

    def test_welcome(self):
        welcome()
        self.assertEqual(self.capturedOutput.getvalue(), "Welcome to the pokemon game!\n")

