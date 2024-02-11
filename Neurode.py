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
        self._reporting_nodes = {self.Side.UPSTREAM: 0, self.Side.DOWNSTREAM: 0}
        self._reference_value = {self.Side.UPSTREAM: 0, self.Side.DOWNSTREAM: 0}
        self._neighbors = {self.Side.UPSTREAM: [], self.Side.DOWNSTREAM: []}

    def __str__(self):
        """String representation of the node in context."""
        return f'Node ID: {id(self._reference_value)} ' \
               f'\nUpstream Node IDs: {id(self._neighbors[self.Side.UPSTREAM])} ' \
               f'\nDownstream Node IDs: {id(self._neighbors[self.Side.DOWNSTREAM])}'

    @abstractmethod
    def _process_new_neighbor(self, node: MultiLinkNode, side: Side):
        """Creating abstract method to process new neighbor."""
        pass

    def reset_neighbors(self, nodes: list, side: Side):
        """Reset neighbor nodes."""
        self._neighbors[side] = []
        self._neighbors[side] = nodes[:]
        num_nodes = len(nodes)
        if num_nodes > 0:
            self._reference_value[side] = 2 ** num_nodes - 1
        else:
            self._reference_value[side] = 0
        for node in nodes:
            self._process_new_neighbor(node, side)


class Neurode(MultiLinkNode, ABC):
    """Class inheriting from MultiLinkNode"""

    _learning_rate = .05

    def __init__(self):
        """Initialize an instance of Neurode Class.
        Parameters: None.
        """
        self._value = 0
        self._weights = {}
        super().__init__()

    @property
    def learning_rate(self):
        """Getter for learning rate."""
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, value: float):
        """Setter for learning rate."""
        self._learning_rate = value

    def _process_new_neighbor(self, node: MultiLinkNode, side: MultiLinkNode.Side):
        """Process new neighbors for UPSTREAM nodes."""
        if side == MultiLinkNode.Side.UPSTREAM:
            self._weights[node] = random.random()

    def _check_in(self, node: Neurode, side: MultiLinkNode.Side):
        """Checks if neighboring nodes have reported."""
        index = self._neighbors[side].index(node)
        self._reporting_nodes[side] |= 1 << index
        if self._reporting_nodes[side] == self._reference_value[side]:
            self._reporting_nodes[side] = 0
            return True
        else:
            return False

    def get_weight(self, node: Neurode):
        """Get weights for nodes."""
        return self._weights.get(node, None)

    @property
    def value(self):
        """Returns value."""
        return self._value
