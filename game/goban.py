import numpy as np
from .check import check_correct


class Goban():

    banmen = None

    def __init__(self, array):
        super().__init__()

        if(np.ndarray != type(array)):
            raise TypeError
        else:
            self.banmen = array

    def add(self, row, column, player_id):
        if(check_correct(self, row, column) == "OK"):
            self.banmen[row][column] = player_id
        else:
            raise ValueError
