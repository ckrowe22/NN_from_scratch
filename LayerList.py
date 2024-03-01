import DoublyLinkedList
import Neurode


class LayerList(DoublyLinkedList):
    """Implementing LayerList class."""

    def __init__(self, inputs: int, outputs: int, neurode_type: type(Neurode)):
        super().__init__()
        self._neurode_type = neurode_type
        self.input_layer = self._create_layer(inputs, neurode_type)
        self.output_layer = self._create_layer(outputs, neurode_type)
        self.add_to_head(self.input_layer)
        self.add_after_current(self.output_layer)
        self.link_layers(self.input_layer, self.output_layer)

    def _create_layer(self, num_nodes: int, neurode_type: type(Neurode)):
        new_layer_list = [neurode_type() for x in range(num_nodes)]
        return new_layer_list

    def link_layers(self, input_list, output_list):
        for upstream_node in input_list:
            upstream_node.reset_neighbors(output_list, Neurode.Side.DOWNSTREAM)
        for downstream_node in output_list:
            # downstream_node._process_new_neighbor(downstream_node, Neurode.Side.UPSTREAM)
            downstream_node.reset_neighbors(input_list, Neurode.Side.UPSTREAM)

    def add_layer(self, num_nodes: int):
        if self._curr == self._tail:
            raise IndexError("Cannot add to output layer.")
        new_layer = self.create_layer(num_nodes, self._neurode_type)
        self.add_after_current(new_layer)
        self.link_layers(self._curr.data, new_layer)

    def remove_layer(self):
        if self._curr == self._tail:
            raise IndexError("Cannot remove output layer.")
        self.remove(self._curr)

        # remove layer after the current layer
        # raise index error if attempting to remove (tail) output layer

    @property
    def input_nodes(self):
        return self._head.data

    @property
    def output_nodes(self):
        return self._tail.data
