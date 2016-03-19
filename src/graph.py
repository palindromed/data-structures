import itertools


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
        self._container.setdefault(n, set())

    def add_edge(self, n1, n2):
        """Add edge connecting node n1 to node n2.

        Creates nodes n1, n2 if necessary.
        """
        self.add_node(n2)
        self._container.setdefault(n1, set()).add(n2)

    def del_node(self, n):
        """Delete node"""
        if self.has_node(n):
            del self._container[n]
            for node in self._container:
                self._container[node].discard(n)
        else:
            raise KeyError("Node not in graph.")

    def del_edge(self, n1, n2):
        """Delete edge connecting n1 to n2."""
        try:
            # NOTE: deliberately not using .discard()
            self._container[n1].remove(n2)
        except (KeyError, ValueError):
            raise ValueError("Edge not in graph.")

    def has_node(self, n):
        """Return True node exists."""
        return n in self._container

    def neighbors(self, n):
        """Return a list of all nodes connected to n by edges."""
        if not self.has_node(n):
            raise KeyError
        return [k for k, v in self._container.items() if n in v]

    def adjacent(self, n1, n2):
        """Return True if n1 is connected to n2 by an edge."""
        # if n1, n2 don't exist: raise error
        if self.has_node(n1) and self.has_node(n2):
            return n2 in self._container[n1]
        else:
            raise KeyError
