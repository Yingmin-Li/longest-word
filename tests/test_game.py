import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

        self.assertIs(new_game.CurrScore(), 0) # check won score in current game
        self.assertIs(new_game.Score(), 0) # check total score

    def test_empty_word_is_invalid(self):
        new_game = Game()
        self.assertIs(new_game.is_valid(''), False)

        self.assertIs(new_game.CurrScore(), 0)
        self.assertIs(new_game.Score(), 0)

    def test_is_valid(self):
        new_game = Game()
        new_game.grid = list('KWEUEAKRZ') # Force the grid to a test case:
        self.assertIs(new_game.is_valid('EUREKA'), True)
        self.assertEqual(new_game.grid, list('KWEUEAKRZ')) # Make sure the grid remained untouched

        self.assertIs(new_game.CurrScore(), 6)
        self.assertIs(new_game.Score(), 0) # total score is only updated in wsgi

    def test_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KWEUEAKRZ') # Force the grid to a test case:
        self.assertIs(new_game.is_valid('SANDWICH'), False)

        self.assertIs(new_game.CurrScore(), 0)
        self.assertIs(new_game.Score(), 0)


        self.assertEqual(new_game.grid, list('KWEUEAKRZ')) # Make sure the grid remained untouched

    def test_unknown_word_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        self.assertIs(new_game.is_valid('FEUN'), False)

        self.assertIs(new_game.CurrScore(), 0)
        self.assertIs(new_game.Score(), 0)
