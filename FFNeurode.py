from __future__ import annotations
from Neurode import Neurode
from math import exp


class FFNeurode(Neurode):
    """Class FF Neurode."""

    def __init__(self):
        """Initializing instance of FFNeurode Class.
        Parameters: None.
        """
        super().__init__()

    @staticmethod
    def _sigmoid(value: float):
        """Logistic function implementation."""
        return 1/(1 + exp(-value))

    def _calculate_values(self):
        """."""

    def _fire_downstream(self):
        """."""

    def data_ready_upstream(self, node: Neurode):
        """."""
        if self._check_in(node, Neurode.Side.UPSTREAM):
            self._calculate_values()
            self._fire_downstream()
        else:
            raise ValueError("No data upstream.")

    def set_input(self, input_value: float):
        """."""
        self._value = input_value
        self.data_ready_upstream(self)
