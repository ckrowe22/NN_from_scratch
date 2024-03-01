from DoublyLinkedList import DoublyLinkedList
from Neurode import Neurode


def link_layers(input_list, output_list):
    """Helper function to link layers."""
    for upstream_node in input_list:
        upstream_node.reset_neighbors(output_list, Neurode.Side.DOWNSTREAM)
    for downstream_node in output_list:
        downstream_node.reset_neighbors(input_list, Neurode.Side.UPSTREAM)


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
        self.input_layer = create_layer(inputs, neurode_type)
        self.output_layer = create_layer(outputs, neurode_type)
        self.add_to_head(self.input_layer)
        self.add_after_current(self.output_layer)
        link_layers(self.input_layer, self.output_layer)

    def add_layer(self, num_nodes: int):
        """Add a layer of nodes."""
        if self._curr == self._tail:
            raise IndexError("Cannot add to output layer.")
        new_layer = create_layer(num_nodes, self._neurode_type)
        self.add_after_current(new_layer)
        link_layers(self._curr.data, new_layer)
        self.move_forward()
        if self._curr.prev:
            link_layers(self._curr.prev.data, self._curr.data)
        if self._curr.next:
            link_layers(self._curr.data, self._curr.next.data)

    def remove_layer(self):
        """Remove a layer of nodes."""
        if self._curr == self._tail:
            raise IndexError("Cannot remove output layer.")
        self.remove_after_current()
        if self._curr.next:  # Ensure there is a next layer before moving forward
            self.link_layers(self._curr.data, self._curr.next.data)

    @property
    def input_nodes(self):
        """Return the input nodes."""
        return self._head.data

    @property
    def output_nodes(self):
        """Return the output nodes."""
        return self._tail.data
