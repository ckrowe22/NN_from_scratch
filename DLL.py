""" Implementing the Linked List ADT. """


class DLLNode:
    """ Linked List Node """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """ Implementing Linked List ADT """
    def __init__(self):
        self._head = None
        self._tail = None
        self._curr = None

    def reset_to_head(self):
        """ Reset the current pointer to the head. """
        self._curr = self._head

    def reset_to_tail(self):
        """ Reset the current pointer to the tail. """
        self._curr = self._tail

    def add_to_head(self, data):
        """ Add a new node to the head of the list. """
        new_node = DLLNode(data)
        if self._head is None:
            # if list is empty and self._head = None, the new node will be both the head and the tail
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self.reset_to_head()

    def remove_from_head(self):
        """ Remove a node from the head of the list and return data. """
        if not self._head:
            raise IndexError
        return_value = self._head.data
        self._head = self._head.next
        self.reset_to_head()
        return return_value

    def move_forward(self):
        """ Move forward through the list. """
        if not self._curr or not self._curr.next:
            raise IndexError
        self._curr = self._curr.next

    def move_backward(self):
        """ Move backwards through the list. """
        if not self._curr or not self._curr.prev:
            raise IndexError
        self._curr = self._curr.prev

    @property
    def curr_data(self):
        """ Return the data at the current position. """
        if not self._curr:
            raise IndexError
        return self._curr.data

    def add_after_current(self, data):
        """ Add a node after the current position. """
        if not self._curr:
            raise IndexError
        new_node = DLLNode(data)
        new_node.next = self._curr.next
        new_node.prev = self._curr
        self._curr.next = new_node
        # if there is no node after self._curr (ie it is the current tail), the new node becomes the tail
        if not new_node.next:
            self._tail = new_node
        else:
            new_node.next.prev = new_node

    def remove_after_current(self):
        """ Remove the node after the current node, returning data. """
        if not self._curr or not self._curr.next:
            raise IndexError
        return_value = self._curr.next.data
        self._curr.next = self._curr.next.next
        # if the new self._curr has no value next, it becomes the tail
        if not self._curr.next:
            self._tail = self._curr
        else:
            self._curr.next.prev = self._curr
        return return_value

    def find(self, data):
        """ Find and return an item in the list. """
        temp_curr = self._head
        while temp_curr:
            if temp_curr.data == data:
                return temp_curr.data
            temp_curr = temp_curr.next
        raise IndexError

    def remove(self, data):
        """ Find and remove a node. """
        if not self._head:
            raise IndexError
        if self._head.data == data:
            return self.remove_from_head()
        temp_curr = self._head
        while temp_curr.next:
            if temp_curr.next.data == data:
                return_value = temp_curr.next.data
                temp_curr.next = temp_curr.next.next
                if not temp_curr.next:
                    self._tail = temp_curr
                else:
                    temp_curr.next.prev = temp_curr
                return return_value
            temp_curr = temp_curr.next
        raise IndexError