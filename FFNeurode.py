from __future__ import annotations
from Neurode import Neurode
from math import exp


class FFNeurode(Neurode):
    """Creating Class FFNeurode."""

    def __init__(self):
        """Initializing instance of FFNeurode Class.
        Parameters: None.
        """
        super().__init__()

    @staticmethod
    def _sigmoid(value: float):
        """Implementing logistic function."""
        return 1/(1 + exp(-value))

    def _calculate_values(self):
        """Using sigmoid function on upstream weights."""
        weighted_sum = 0
        for node in self._neighbors[Neurode.Side.UPSTREAM]:
            weight = self.get_weight(node)
            if weight is not None:
                weighted_sum += node.value * weight
        self._value = self._sigmoid(weighted_sum)

    def _fire_downstream(self):
        """Firing data to downstream nodes."""
        for node in self._neighbors[Neurode.Side.DOWNSTREAM]:
            node.data_ready_upstream(self)

    def data_ready_upstream(self, node: Neurode):
        """Processing data from ready nodes upstream."""
        if self._check_in(node, Neurode.Side.UPSTREAM):
            self._calculate_values()
            self._fire_downstream()
        else:
            raise ValueError("No data upstream.")

    def set_input(self, input_value: float):
        """Setting the value of an input layer neurode."""
        self._value = input_value
        for node in self._neighbors[Neurode.Side.DOWNSTREAM]:
            node.data_ready_upstream(self)
