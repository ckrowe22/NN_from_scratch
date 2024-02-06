from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
import random


class MultiLinkNode(ABC):
    """Creating Abstract Base Class MultiLinkNode."""

    class Side(Enum):
        """Enum class to identify neurode relationships."""
        UPSTREAM = 1
        DOWNSTREAM = 2

    def __init__(self):
        """Initialize an instance of MultiLinkNode Class.
        Parameters: None.
        """
        self._reporting_nodes = {self.Side.UPSTREAM: 0, self.Side.DOWNSTREAM: 1}
        self._reference_value = {self.Side.UPSTREAM: 0, self.Side.DOWNSTREAM: 1}
        self._neighbors = {self.Side.UPSTREAM: [], self.Side.DOWNSTREAM: []}

    def __str__(self):
        """String representation of the node in context."""
        return f'Node ID: {self._reference_value} ' \
               f'\nUpstream Node IDs: {self._neighbors[self.Side.UPSTREAM]} ' \
               f'\nDownstream Node IDs: {self._neighbors[self.Side.DOWNSTREAM]}'

    @abstractmethod
    def _process_new_neighbor(self, node: MultiLinkNode, side: Side):
        """..."""
        pass

    def reset_neighbors(self, nodes: list, side: Side):
        """..."""
        self._neighbors[side] = []
        for node in nodes:
            self._neighbors[side].append(node)
            self._process_new_neighbor(node, side)

        # assignment, copy, or deepcopy.
        # The client could modify and reuse the nodes list, which has the potential to
        # corrupt self._neighbors.
        # We don't want to create new MultiLinkNodes, we want references to nodes
        # that already exist.


class Neurode(MultiLinkNode, ABC):
    """Class inheriting from MultiLinkNode"""

    _learning_rate = .05

    def __init__(self):
        """Initialize an instance of MultiLinkNode Class.
        Parameters: None.
        """
        self._value = 0
        self._weights = {}
        super().__init__()

    @property
    def learning_rate(self):
        # property decorator .05
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, value: float):
        self._learning_rate = value

        # This is actually a pair of methods, a setter and a getter coded
        # with the @ property decorator.They should get or set the class
        # attribute that you defined above.In your testing, make sure that this
        # truly behaves as a class attribute.In other words, changing the
        # learning rate for one object of the class should change the learning rate
        # for all objects of the class.

    def _process_new_neighbor(self, node: MultiLinkNode, side: ABC.Side):
        if side == ABC.Side.UPSTREAM:
            self._weights[node] = random.random()

    def _check_in(self, node: Neurode, side: ABC.Side):
        index = self._neighbors[side].index(node)
        self._reporting_nodes[side] = node[index]
        if self._reporting_nodes[side] == self._reference_value:
            self._reporting_nodes = 0
            return True
        else:
            return False

    def get_weight(self, node: Neurode):
        return self._weights.get(node, None)

    @property
    def value(self):
        return self._value
