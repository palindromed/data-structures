class BinHeap(object):
    def __init__(self, init=[]):
        self._container = init
        self._container.insert(0, None)
        if init != []:
            self._heapify(1)

    def _heapify(self, index):
        left = 2 * index
        right = 2 * index + 1
        largest = index

        if left <= len(self._container) and self._container[left] > self._container[largest]:
            largest = left
        if right <= len(self._container) and self._container[right] > self._container[largest]:
            largest = right

        if largest != index:
            this_node_value = self._container[index]
            self._container[index] = self._container[largest]
            self._container[largest] = this_node_value
            self._heapify(largest)
