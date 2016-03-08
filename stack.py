from linked_list import LinkedList, Node


class Stack(object):
    def __init__(self, iterable=[]):
        self.ll = LinkedList(iterable)

    def push(self, val):
        return self.ll.insert(val)

    def pop(self):
        return self.ll.pop()
