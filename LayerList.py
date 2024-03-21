from DoublyLinkedList import DoublyLinkedList
from Neurode import Neurode


def create_layer(num_nodes: int, neurode_type: type(Neurode)):
    """Helper function to create lists of nodes in layer."""
    new_layer_list = [neurode_type() for x in range(num_nodes)]
    return new_layer_list


class LayerList(DoublyLinkedList):
    """Implementing LayerList class."""

    def __init__(self, inputs: int, outputs: int, neurode_type: type(Neurode)):
        """
        Initialize an instance of LayerList Class.

        Parameters:
        inputs (int): Inputs for input layer.
        outputs (int): Outputs for output layer.
        neurode_type (Neurode): Upstream or downstream neurode.
        """
        super().__init__()
        self._neurode_type = neurode_type
        if inputs < 1 or outputs < 1:
            raise ValueError
        self.input_layer = create_layer(inputs, neurode_type)
        self.output_layer = create_layer(outputs, neurode_type)
        self.add_to_head(self.input_layer)
        self.add_after_current(self.output_layer)
        self.link_with_next_layer()

    def link_with_next_layer(self):
        """Helper function to link layers."""
        for node in self._curr.data:
            node.reset_neighbors(self._curr.next.data, self._neurode_type.Side.DOWNSTREAM)
        for node in self._curr.next.data:
            node.reset_neighbors(self._curr.data, self._neurode_type.Side.UPSTREAM)

    def add_layer(self, num_nodes: int):
        """Add a layer of nodes."""
        if self._curr == self._tail:
            raise IndexError("Cannot add to output layer.")
        if num_nodes > 0:
            raise ValueError
        new_layer = create_layer(num_nodes, self._neurode_type)
        self.add_after_current(new_layer)
        self.link_with_next_layer()
        if self._curr.next:
            self.move_forward()
            self.link_with_next_layer()
            self.move_backward()

    def remove_layer(self):
        """Remove a layer of nodes after the current layer."""
        if self._curr.next == self._tail or self._curr == self._tail:
            raise IndexError("Cannot remove output layer.")
        self.remove_after_current()
        self.link_with_next_layer()

    @property
    def input_nodes(self):
        """Return the input nodes."""
        return self._head.data

    @property
    def output_nodes(self):
        """Return the output nodes."""
        return self._tail.data
