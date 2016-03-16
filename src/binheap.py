import math


class BinHeap(object):
    def __init__(self, init=[]):
        self._container = init
        self._container.insert(0, None)
        if init != []:
            self._heapify(1)

    def _heapify(self, index):
        # indices
        left = 2 * index
        right = 2 * index + 1
        largest = index

        if left <= (len(self._container) - 1) and self._container[left] > self._container[largest]:
            largest = left
        if right <= (len(self._container) - 1) and self._container[right] > self._container[largest]:
            largest = right
        if largest != index:
            this_node_value = self._container[index]
            self._container[index] = self._container[largest]
            self._container[largest] = this_node_value
            self._heapify(largest)

    def pop(self):
        self._container[1] = self._container.pop()
        self._heapify(1)


    def push(self, value):
        self._container.append(value)
        #  compare this node with parent
        # [None, 1, 2, 3]
        child = (len(self._container) - 1)
        parent = math.floor(child / 2)
        while (self._container[child] > self._container[parent] and child > 1):
            # swap parent and child
            # move up the chain towards the root
            pass
