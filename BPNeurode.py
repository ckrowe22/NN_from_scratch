from Neurode import Neurode


class BPNeurode(Neurode):
    """Creating class BPNeurode."""

    def __init__(self):
        """Initialize an instance of BPNeurode Class.
         Parameters: None.
         """
        super().__init__()
        self._delta = 0

    @staticmethod
    def _sigmoid_derivative(value: float):
        """Getting the derivative of sigmoid function."""
        return value * (1 - value)

    def _calculate_delta(self, expected_value: float = None):
        """Calculate delta for the neurode."""

        #output layer nodes - this works
        if expected_value is not None:
            self._delta = (expected_value - self.value) * self._sigmoid_derivative(self.value)
        #hidden layer nodes - this does not :(
        else:
            hidden_delta = 0
            # Calculate the sum of the product of downstream node's delta and the weight
            for node in self._neighbors[Neurode.Side.DOWNSTREAM]:
                hidden_delta += node.delta * self.get_weight(node)
            # Multiply by the derivative of the sigmoid function applied to the current node's value
            self._delta = hidden_delta * self._sigmoid_derivative(self.value)

    def data_ready_downstream(self, node: Neurode):
        """Checking downstream nodes for data."""
        if self._check_in(node, Neurode.Side.DOWNSTREAM):
            self._calculate_delta()
            self._fire_upstream()
            self._update_weights()

    def set_expected(self, expected_value: float):
        """Set expected values for output layer nodes."""
        self._calculate_delta(expected_value)
        for node in self._neighbors[Neurode.Side.UPSTREAM]:
            node.data_ready_downstream(self)

    def adjust_weights(self, node: Neurode, adjustment: float):
        """Adjusting upstream nodes."""
        self._weights[node] = self.get_weight(node) + adjustment

    def _update_weights(self):
        """Update the weights of the nodes."""
        for node in self._neighbors[Neurode.Side.DOWNSTREAM]:
            adjustment = node.learning_rate * node.delta * self.value
            node.adjust_weights(self, adjustment)

    def _fire_upstream(self):
        """Firing data to upstream nodes."""
        for node in self._neighbors[Neurode.Side.UPSTREAM]:
            node.data_ready_downstream(self)

    @property
    def delta(self):
        """Getter for delta."""
        return self._delta
