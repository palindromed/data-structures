from linked_list import LinkedList


class Stack(object):
    """Stack data type is composed using linked list data type"""

    def __init__(self, iterable=[]):
        self.ll = LinkedList(iterable)

    def push(self, val):
        """Add val to top of stack"""
        self.ll.insert(val)

    def pop(self):
        """Remove and return first element of stack"""
        return self.ll.pop()
