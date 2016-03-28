from collections import deque
from queue import Queue
from math import inf


class Graph():
    def __init__(self):
        # Create empty graph
        self._container = {}

    def nodes(self):
        """Return a list of all nodes."""
        return [node for node in self._container]

    def edges(self):
        """Retun a list of all edges."""
        edges = []
        for node in self._container:
            for value in self._container[node]:
                edges.append((node, value))
        return edges

    def add_node(self, n):
        """Add node to graph."""
        self._container.setdefault(n, {})

    def add_edge(self, n1, n2, weight='weight'):
        """Add edge connecting node n1 to node n2.

        Creates nodes n1, n2 if necessary.
        """
        self.add_node(n1)  # add_node handles this, whether or not n1 exists
        self.add_node(n2)
        self._container[n1][n2] = weight

    def del_node(self, n):
        """Delete node."""
        if self.has_node(n):
            del self._container[n]
            for node in self._container:
                self._container[node].pop(n, None)
        else:
            raise KeyError("Node not in graph.")

    def del_edge(self, n1, n2):
        """Delete edge connecting n1 to n2."""
        try:
            del self._container[n1][n2]
        except (KeyError, ValueError):
            raise ValueError("Edge not in graph.")

    def has_node(self, n):
        """Return True node exists."""
        return n in self._container

    def neighbors(self, n):
        """Return a list of all nodes connected to n by edges."""
        if not self.has_node(n):
            raise KeyError
        return [n for n in self._container[n]]

    def adjacent(self, n1, n2):
        """Return True if n1 is connected to n2 by an edge."""
        # NOTE: try...except meant to indicate error raising is deliberate
        try:
            self._container[n2]
        except KeyError:
            raise KeyError
        return n2 in self._container[n1]

    def breadth_first_traversal(self, start):
        if self._container == {}:
            raise IndexError("Empty Graph")
        queue = Queue()
        path = [start]
        queue.enqueue(start)
        while queue.size() > 0:
            cursor = queue.dequeue()
            for neighbor in sorted(self.neighbors(cursor)):
                if neighbor not in path:
                    path.append(neighbor)
                    queue.enqueue(neighbor)
        return path

    def depth_first_traversal(self, start):
        if self._container == {}:
            raise IndexError("Empty Graph")
        stack = deque()
        path = []
        stack.append(start)
        while stack:
            cursor = stack.pop()
            if cursor not in path:
                path.append(cursor)
                for neighbor in sorted(self.neighbors(cursor)):
                    stack.append(neighbor)
        return path

    def get_weight(self, n1, n2):
        """Return weight for given edge.

        Error for bad node params."""
        return self._container[n1][n2]

    def dijkstra_path(self, n1, n2):
        # for key, value in dist: key =  given node, value = total distance from given node to source
        dist = {}
        unvisited = []
        path = {}
        for node in self._container:
            dist[node] = inf
            path[node] = ''
            unvisited.append(node)
        dist[n1] = 0
        cursor = n1

        while len(unvisited) > 0:
            cursor = unvisited[0]
            min_edge = dist[cursor]
            for node in unvisited:
                if dist[node] < min_edge:
                    cursor = node
                    min_edge = dist[node]
            if cursor == n2:
                break
            unvisited.remove(cursor)
            for neighbor in self.neighbors(cursor):
                if neighbor in unvisited:
                    alt = dist[cursor] + self.get_weight(cursor, neighbor)
                    if alt < dist[neighbor]:
                        dist[neighbor] = alt
                        path[neighbor] = cursor  # ??

        stack = deque()
        another_cursor = n2
        stack.appendleft(another_cursor)
        while another_cursor != n1:
            stack.appendleft(path[another_cursor])
            another_cursor = path[another_cursor]

        total = dist[n2]

        return total, stack
