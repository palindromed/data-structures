# -*- coding: utf-8 -*-
from __future__ import division


class BinHeap(object):
    """Create instance of Bin Heap."""

    def __init__(self, init=[]):
        """Create heap empty or with given values."""
        self._container = []
        for element in init:
            self.push(element)

    def _sort_down(self, index):
        # Maintain heap property for children of given node(index).
        left, right = 2 * index, 2 * index + 1
        largest = index
        length = len(self._container) - 1

        if left <= length and self._container[left] > self._container[largest]:
            largest = left
        if right <= length and self._container[right] > self._container[largest]:
            largest = right
        if largest != index:
            this_node_value = self._container[index]
            self._container[index] = self._container[largest]
            self._container[largest] = this_node_value
            self._sort_down(largest)

    def pop(self):
        """Remove root of heap and ensures heap is maintained."""
        self._container[0] = self._container.pop()
        self._sort_down(0)

    def push(self, value):
        """Add given value to heap and maintain heap property."""
        self._container.append(value)
        child = len(self._container) - 1
        parent = child // 2
        while (child >= 0 and self._container[child] > self._container[parent]):
            smaller_parent = self._container[parent]
            self._container[parent] = self._container[child]
            self._container[child] = smaller_parent
            child = parent
            parent = child // 2
