from Neurode import Neurode


class BPNeurode(Neurode):
    """Creating class BPNeurode."""

    def __init__(self):
        super().__init__()
        self._delta = 0

    @staticmethod
    def _sigmoid_derivative(value: float):
        return value * (1 - value)

    def _calculate_delta(self, expected_value: float): #= None
        """."""
        self._delta = (expected_value - self.value) * self.value * (1 - self.value)

    def data_ready_downstream(self, node: Neurode):
        """Checking downstream nodes for data."""
        if self._check_in(node, Neurode.Side.DOWNSTREAM):
            self._calculate_delta()
            self._fire_upstream()
            self._update_weights()

    def set_expected(self, expected_value: float):
        """."""
        self._calculate_delta(expected_value)
        for node in self._neighbors[Neurode.Side.UPSTREAM]:
            node.data_ready_downstream(self)

    def adjust_weights(self, node: Neurode, adjustment: float):
        """."""
        #weight = weight + Value of Upstream node * Delta Downstream * Learning Rate Downstream
        # node.value
        # self._weights
        node._weights[self] += adjustment * self._calculate_delta() * node._learning_rate

    def _update_weights(self):
        """."""
        for node in self._neighbors[Neurode.Side.DOWNSTREAM]:
            node.adjust_weights(node, self)

    def _fire_upstream(self):
        """Firing data to upstream nodes."""
        for node in self._neighbors[Neurode.Side.UPSTREAM]:
            node.data_ready_downstream(self)

    @property
    def delta(self):
        """Getter for delta."""
        return self._delta
