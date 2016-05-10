"""Implement a singly linked list in Python"""
from __future__ import print_function


class LinkedList(object):
    """Create instance of linked list."""

    def __init__(self, iterable=[]):
        """Construct a linked list"""
        self.head_node = Node(None, None)
        for n in range(0, len(iterable)):
            self.insert(iterable[n])

    def insert(self, val):
        """Insert a new value at the head of the list."""
        self.head_node = Node(val, self.head_node)

    def pop(self):
        """Remove the first value of list and return it."""
        if self.head_node.value is None:
            raise ValueError
        else:
            return_value = self.head_node.value
            self.head_node = self.head_node.next
            return return_value

    def size(self):
        """Return the length of the list."""
        value = self.head_node
        counter = -1
        while value is not None:
            value = value.next
            counter += 1
        return counter

    def search(self, val):
        """Return the node containing val."""
        value = self.head_node.value
        node = self.head_node
        if val == value:
            return node
        try:
            while val != value:
                node = node.next
                value = node.value
            return node
        except AttributeError:
            return "That value is not in the list."

    def remove(self, node):
        """Remove given node from list if it exists."""
        this = self.head_node
        try:
            if node == this:
                self.head_node = this.next
                return "Removed {}".format(this.value)
            while node != this:
                prev_node = this
                this = this.next
            next_node = this.next
            prev_node.update_next(next_node)
            return "Removed {} and updated the list.".format(this.value)
        except AttributeError:
            return "That node does not exist in the list."

    def display(self):
        """Print list as a Python tuple literal."""
        out = u'('
        cursor = self.head_node
        while cursor.value is not None:
            out = ''.join([out, str(cursor.value), u', '])
            cursor = cursor.next
        out = ''.join([out, u')'])
        print(out)


class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def update_next(self, next):
        self.next = next

