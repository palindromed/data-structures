class LinkedList(object):
    def __init__(self, iterable=None):
        self.head_node = Node(None, None)
        if iterable is not None:
            for n in range(0, len(iterable)):
                self.insert(iterable[n])

    def insert(self, val):
        """Insert a new value at the head of the list."""
        self.head_node = Node(val, self.head_node)

    def pop(self):
        """Remove the first value of list and return it."""
        try:
            return_value = self.head_node.value
            self.head_node = self.head_node.next
            return return_value
        except AttributeError:
            return "The list is empty."

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
        try:
            while val != value:
                node = value.next
                value = value.next.value
            return node
        except AttributeError:
            return "That value is not in the list."

    def remove(self, node):
        """Remove given node from list if it exists."""
        this = self.head_node
        if node != this:
            self.head_node = this.next
        try:
            while node != this:
                prev_node = this
                this = this.next
        except AttributeError:
            return "That node does not exist in the list."
        else:
            next_node = this.next
            prev_node.update_next(next_node)

    def display(self):
        """Print list as a Python tuple literal."""
        print("()")
        pass


class Node(object):
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def update_next(self, next):
        self.next = next

