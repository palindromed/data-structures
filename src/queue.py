from double_linked_list import DoubleLinkedList


class Queue(object):
    """Create a queue data structure"""
    def __init__(self):
        self.container = DoubleLinkedList()

    def enqueue(self, val):
        """Inserts value to queue"""
        self.container.insert(val)

    def dequeue(self):
        """Removes next item and returns it"""
        return self.container.shift()

    def peek(self):
        """Return next value in queue without dequeuing it"""
        if self.container.tail_node is None:
            return None
        return self.container.tail_node.value

    def size(self):
        """Return size of queue, 0 if empty"""
        if self.container.head_node is None:
            return 0
        cursor = self.container.head_node
        if self.container.head_node.next == self.container.tail_sentinal:
            return 1
        size = 1
        while cursor.next != self.container.tail_sentinal:
            size += 1
            cursor = cursor.next
        return size
