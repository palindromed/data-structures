# -*- coding: utf-8 -*-
from linked_list import Node


class DoubleLinkedList(object):
    """Create double linked list."""

    def __init__(self, iterable=[]):
        """Construct a Double linked list"""
        self.head_node = DLLNode(None, None, None)
        self.tail_node = DLLNode(None, None, None)
        # for n in range(0, len(iterable)):
            # self.insert(iterable[n])

    def insert(self, value):
        """Insert a new node to beginning of list."""
        new_node = DLLNode(value, self.head_node, None)
        self.head_node.update_previous(new_node)
        self.head_node = new_node

    def append(self, value):
        """Append a new node to end of the list."""
        new_node = DLLNode(value, None, self.tail_node)
        self.tail_node.update_next(new_node)
        self.tail_node = new_node


class DLLNode(Node):
    """Add previous value to Node"""

    def __init__(self, value, next, previous):
        self.previous = previous
        Node.__init__(self, value, next)

    def update_previous(self, previous):
        self.previous = previous
