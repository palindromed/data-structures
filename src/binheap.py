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
        index += 1
        left, right = 2 * index, 2 * index + 1
        largest = index
        length = len(self._container)
        if left <= length and self._container[left - 1] > self._container[largest - 1]:
            largest = left
        if right <= length and self._container[right - 1] > self._container[largest - 1]:
            largest = right
        if largest != index:
            this_node_value = self._container[index - 1]
            self._container[index - 1] = self._container[largest - 1]
            self._container[largest - 1] = this_node_value
            self._sort_down(largest - 1)

    def pop(self):
        """Remove root of heap and ensures heap is maintained."""
        if len(self._container) == 1:
            self._container.pop()

        elif len(self._container) > 1:
            self._container[0] = self._container.pop()
            self._sort_down(0)

        else:
            raise IndexError("The list is empty")

    def push(self, value):
        """Add given value to heap and maintain heap property."""
        self._container.append(value)
        child = len(self._container)
        parent = child // 2
        while (child > 1 and self._container[child - 1] > self._container[parent -1]):
            smaller_parent = self._container[parent -1]
            self._container[parent-1] = self._container[child-1]
            self._container[child-1] = smaller_parent
            child = parent
            parent = child // 2
