
# -*- coding: utf-8 -*-
import math


class BinHeap(object):
    def __init__(self, init=[]):
        # TODO: test if works when root, childen do not violate heap property
        self._container = init
        self._container.insert(0, None)
        if init != []:
            self._heapify(1)

    def _heapify(self, index):
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
            # TODO: rewrite as while loop
            self._heapify(largest)

    def pop(self):
        self._container[1] = self._container.pop()
        self._heapify(1)

    def push(self, value):
        self._container.append(value)
        child = len(self._container) - 1
        parent = math.floor(child / 2)
        while (self._container[child] > self._container[parent] and child > 1):
            # swap parent and child
            # move up the chain towards the root
            pass
