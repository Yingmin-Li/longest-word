""" Find longest word game """

import random
import string

class Game:
    """ Find longest word game """

    @property
    def grid(self):
        """ random chars """
        return self.grid

    def __init__(self):
        """  init """
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        """ check if a gusssing word is valid for grid """
        list1=self.grid
        list2=word
        result =  all(elem.upper() in list1  for elem in list2)
        return result
