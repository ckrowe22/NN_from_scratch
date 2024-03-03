from abc import ABC, abstractmethod
from math import sqrt

class RMSE(ABC):
    def __init__(self):
        """
        Initialize an instance of LayerList Class.

        Parameters: none
        """
        self._data = []

    def __add__(self, other):
        """."""
        new_value = self._data + other
        return new_value

    def __iadd__(self, other):
        """."""
        new_data =
        #
        self._data += new_data
        #deep copy self here?
        return self


    def reset(self):
        self._data = [] #? reset list by making it empty again?

    @property
    def error(self):
        #calculate RMSE
        #sq root (sum of every (expected - output)^2 / num of values)
        # and return error

    @staticmethod
    @abstractmethod
    def distance(predicted_output: tuple, expected_output: tuple):
        """Abstract distance method."""
        pass

class Euclidean(RMSE):
    @staticmethod
    def distance(predicted_output, expected_output):
        """Calculates the Euclidian distance."""
        return sqrt(sum((predicted_output[i] - expected_output[i]) for i in range(len(predicted_output))))

class Taxicab(RMSE):
    @staticmethod
    def distance(predicted_output, expected_output):
        """Calculates the Taxicab/Manhattan distance."""
        return sum(abs(predicted_output[i] - expected_output[i]) for i in range(len(predicted_output)))
