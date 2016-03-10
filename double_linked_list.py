# -*- coding: utf-8 -*-
from linked_list import Node


class DoubleLinkedList(object):
    """Create double linked list."""

    def __init__(self, iterable=[]):
        """Construct a Double linked list"""
        self.head_node = None
        self.tail_node = None
        #self.head_node = DLLNode(None, None, None)
        #self.tail_node = DLLNode(None, None, None)
#        for n in range(0, len(iterable)):
#            self.insert(iterable[n])

    def insert(self, value):
        """Insert a new node to beginning of list."""
        # create a new node with value as value, with next as current head_node
        new_node = DLLNode(value, self.head_node, None)
        # update current head to point to new head as previous
        if self.head_node is not None:
            self.head_node.update_previous(new_node)
        # name new node "head_node"
        self.head_node = new_node
        if self.tail_node is None:
            self.tail_node = new_node

    def append(self, value):
        """Append a new node to end of the list."""
        new_node = DLLNode(value, None, self.tail_node)
        if self.tail_node is not None:
            self.tail_node.update_next(new_node)
        self.tail_node = new_node
        if self.head_node is None:
            self.head_node = new_node


    def pop(self):
        """Pop the first value off the list and return it"""
        return_value = None
        if self.head_node is not None:
            return_value = self.head_node.value
            self.head_node.update_previous(None)
        elif :
            self.head_node = self.head_node.next
        return return_value


class DLLNode(Node):
    """Add previous value to Node"""

    def __init__(self, value, next, previous):
        self.previous = previous
        Node.__init__(self, value, next)

    def update_previous(self, previous):
        self.previous = previous
