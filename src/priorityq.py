# -*- coding: utf-8 -*-
from __future__ import division


class PriorityQueue(object):

    def __init__(self):
        """Create a priority queue."""
        self._container = []

    def insert(self, item):
        """Insert item into priority queue."""
        self._container.append(item)
        self._sort_up(len(self._container))

    def pop(self):
        """Remove and return highest priority item in priority queue."""
        if len(self._container) == 1:
            return self._container.pop()
        elif len(self._container) > 1:
            return_value = self._container[0]
            self._container[0] = self._container.pop()
            self._sort_down(0)
            return return_value
        else:
            raise IndexError("Priority queue empty")

    def peek(self):
        """Return highest priority item in priority queue without removing it."""
        return self._container[0]
        pass

    def _sort_down(self, index):
        # helper method to maintain heap property after popping
        index += 1
        left, right = 2 * index, 2 * index + 1
        largest = index
        length = len(self._container)
        if (left <= length and
            self._container[left - 1][0] >= self._container[largest - 1][0]):
            largest = left
        if (right <= length and
            self._container[right - 1][0] >= self._container[largest - 1][0]):
            largest = right
        if largest != index:
            this_node_value = self._container[index - 1]
            self._container[index - 1] = self._container[largest - 1]
            self._container[largest - 1] = this_node_value
            self._sort_down(largest - 1)

    def _sort_up(self, index):
        # helper method to maintain heap property after inserting
        child = index
        parent = child // 2
        while (child > 1 and
               self._container[child - 1][0] > self._container[parent - 1][0]):
            smaller_parent = self._container[parent - 1]
            self._container[parent - 1] = self._container[child - 1]
            self._container[child - 1] = smaller_parent
            child = parent
            parent = child // 2


