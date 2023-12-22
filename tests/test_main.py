import unittest 
from source import main

import io
import sys

class TestMain(unittest.TestCase):
    def setUp(self):
        self.capturedOutput = io.StringIO()  
        sys.stdout = self.capturedOutput
  
    def tearDown(self):
        sys.stdout = sys.__stdout__ 

    def test_welcome(self):
        main.welcome()
        self.assertEqual(self.capturedOutput.getvalue(), "Welcome to the pokemon game!\n")

