from Neurode import Neurode


class BPNeurode(Neurode):
    """Creating class BPNeurode."""

    def __init__(self):
        super().__init__()
        self._delta = 0

    @staticmethod
    def _sigmoid_derivative(value: float):
        return value * (1 - value)

    def _calculate_delta(self, expected_value: float = None):
        """."""

    def data_ready_downstream(self, node: Neurode):
        """."""

    def set_expected(self, expected_value: float):
        """."""

    def adjust_weights(self, node: Neurode, adjustment: float):
        """."""
        weight = weight + Value of Upstream node * Delta Downstream * Learning Rate Downstream

    def _update_weights(self):
        """."""
        for node in self._neighbors[Neurode.Side.DOWNSTREAM]:
            node.adjust_weights(node, self)

    def _fire_upstream(self):
        """."""

    @property
    def delta(self):
        """Getter for delta."""
        return self._delta
