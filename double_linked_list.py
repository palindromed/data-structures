# -*- coding: utf-8 -*-
from linked_list import Node


class DoubleLinkedList(object):
    """Create double linked list."""

    def __init__(self, iterable=[]):
        """Construct a Double linked list"""
        self.head_node = None
        self.tail_node = None
        self.head_sentinal = object()
        self.tail_sentinal = object()

#        for n in range(0, len(iterable)):
#            self.insert(iterable[n])

    def insert(self, value):
        """Insert a new value to beginning of list."""
        # create a new node with value as value, with next as current head_node
        if self.head_node is None:
            self.head_node = DLLNode(value, self.head_sentinal, self.tail_sentinal)
            self.tail_node = self.head_node

        else:
            new_head = DLLNode(value, self.head_sentinal, self.head_node)
            self.head_node.previous = new_head
            self.head_node = new_head

    def append(self, value):
        """Add a new value to the end of the list."""
        if self.tail_node is None:
            self.tail_node = DLLNode(value, self.head_sentinal, self.tail_sentinal)
            self.head_node = self.tail_node
        else:
            new_tail = DLLNode(value, self.tail_node, self.tail_sentinal)
            self.tail_node.next = new_tail
            self.tail_node = new_tail



class DLLNode(Node):
    """Add previous value to Node"""

    def __init__(self, value, previous, next):
        self.previous = previous
        Node.__init__(self, value, next)
