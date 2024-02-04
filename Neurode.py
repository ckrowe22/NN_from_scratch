from __future__ import annotations
from enum import Enum

class MultiLinkNode:
    """..."""
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
               f'\nUpstream Node IDs: {self._neighbors[0]} ' \
               f'\nDownstream Node IDs: {self._neighbors[1]}'

    def _process_new_neighbor(self, node: MultiLinkNode, side: Side):
        """..."""

    def reset_neighbors(self, nodes: list, side: Side):
