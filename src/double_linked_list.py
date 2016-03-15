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
            self.head_node = DLLNode(value,
                                     self.head_sentinal,
                                     self.tail_sentinal)
            self.tail_node = self.head_node
        else:
            new_head = DLLNode(value, self.head_sentinal, self.head_node)
            self.head_node.previous = new_head
            self.head_node = new_head

    def append(self, value):
        """Add a new value to the end of the list."""
        if self.tail_node is None:
            self.tail_node = DLLNode(value,
                                     self.head_sentinal,
                                     self.tail_sentinal)
            self.head_node = self.tail_node
        else:
            new_tail = DLLNode(value, self.tail_node, self.tail_sentinal)
            self.tail_node.next = new_tail
            self.tail_node = new_tail

    def pop(self):
        """Pop the first value and return it"""
        # pop an empty list
        if self.head_node is None:
            raise ValueError
        old_head_value = self.head_node.value
        # pop a one-element list
        if self.head_node.next == self.tail_sentinal:
            self.head_node = None
            self.tail_node = None
        else:
            self.head_node = self.head_node.next
            self.head_node.previous = self.head_sentinal
        return old_head_value

    def shift(self):
        """Shift the last value and return it"""
        # pop an empty list
        if self.tail_node is None:
            raise ValueError
        old_tail_value = self.tail_node.value
        # pop a one-element list
        if self.tail_node.previous == self.head_sentinal:
            self.head_node = None
            self.tail_node = None
        else:
            self.tail_node = self.tail_node.previous
            self.tail_node.next = self.tail_sentinal
        return old_tail_value

    def remove(self, val):
        """Search for and remove a value from the list if present"""
        if self.head_node is None:
            raise ValueError
        if self.head_node.value == val:
            self.pop()
        cursor = self.head_node
        try:
            while cursor.value != val:
                cursor = cursor.next

            update_next = cursor.previous
            update_previous = cursor.next
            update_next.next = update_previous
            if cursor != self.tail_node:
                update_previous.previous = update_next
            elif cursor == self.tail_node:
                self.tail_node = update_next
        except AttributeError:
            raise ValueError


class DLLNode(Node):
    """Add previous value to Node"""

    def __init__(self, value, previous, next):
        self.previous = previous
        Node.__init__(self, value, next)
