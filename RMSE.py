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
        """Overloading add."""
        new_object = self.__class__()
        new_object._data = self._data + [other]
        return new_object

    def __iadd__(self, other):
        """Overloading +=."""
        self._data.append(other)
        return self

    def reset(self):
        """Clears internal data."""
        self._data = []

    @property
    def error(self):
        """Calculates RMSE and returns total error."""
        if not self._data:
            return 0
        errors = [self.distance(predicted, expected) for predicted, expected in self._data]
        mean_squared_error = sum(errors) / len(errors)
        return sqrt(mean_squared_error)

    @staticmethod
    @abstractmethod
    def distance(predicted_output: tuple, expected_output: tuple):
        """Abstract distance method."""
        pass


class Euclidean(RMSE):
    @staticmethod
    def distance(predicted_output, expected_output):
        """Calculates the Euclidian distance."""
        return sum((predicted_output[i] - expected_output[i])**2 for i in range(len(predicted_output)))


class Taxicab(RMSE):
    @staticmethod
    def distance(predicted_output, expected_output):
        """Calculates the Taxicab/Manhattan distance."""
        return sum(abs(predicted_output[i] - expected_output[i]) for i in range(len(predicted_output)))**2
