class LinkedList(object):
    def __init__(self, iterable=None):
        if iterable is None:
            self.head_node = Node(None, None)
        else:
            pass

    def insert(self, val):
        """Insert a new value at the head of the list."""
        self.head_node = Node(val, self.head_node)

    def pop(self):
        """Remove the first value of list and return it."""
        pass

    def size(self):
        """Return the length of the list."""
        pass

    def search(self, val):
        """Return the node containing val."""
        pass

    def remove(self, node):
        """Remove given node from list if it exists."""
        pass

    def display(self):
        """Print list as a Python tuple literal."""
        pass



class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next

