# pylint: disable=too-few-public-methods
""" Find longest word game """

import random
import string
import requests

class Game:
    """ Find longest word game """

    def __init__(self):
        """  init """
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        """ check if a gusssing word is valid for grid """
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return self.__check_dictionary(word)

    @staticmethod
    def __check_dictionary(word):
        """ check if a gusssing word is in dictionary """
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']
