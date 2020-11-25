# pylint: disable=too-few-public-methods
""" Find longest word game """

import random
import string
import requests

class Game:
    """ Find longest word game """

    score=0
    curr_score=0

    def __init__(self, score=0):
        """ init """
        self.grid = []
        self.score=score
        self.curr_score=0
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        """ check if a gusssing word is valid for grid """

        curr_score=0

        if not word:
            self.curr_score=0
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                curr_score=curr_score+1
                letters.remove(letter)
            else:
                self.curr_score=0
                return False

        # increment only is_valid==True
        self.curr_score=curr_score
        return self.__check_dictionary(word)


    #@property # https://www.artima.com/forums/flat.jsp?forum=122&thread=153649
    def Score(self):
        return self.score

    def CurrScore(self):
        return self.curr_score

    @staticmethod
    def __check_dictionary(word):
        """ check if a gusssing word is in dictionary """
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']
