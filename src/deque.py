from queue import Queue


class Deque(object):
    """Create a deque data structure."""
    def __init__(self):
        self.q = Queue()
        # name q's container attribute 'dll' (which is a doubly linked list)
        self.dll = self.q.container

    def append(self, value):
        """Insert value at tail of deque."""
        self.dll.append(value)

    def appendleft(self, value):
        """Insert value at head of deque."""
        self.dll.insert(value)

    def pop(self):
        """Return right/tail value and removes from deque."""
        return self.dll.shift()

    def popleft(self):
        """Return left/head value and removes from deque."""
        return self.dll.pop()

    def peek(self):
        """Return tail value in deque without removing it."""
        return self.q.peek()

    def peekleft(self):
        """Return head value in deque without removing it."""
        if self.dll.head_node is None:
            return None
        return self.dll.head_node.value

    def size(self):
        """Return size of deque, 0 if empty."""
        return self.q.size()
