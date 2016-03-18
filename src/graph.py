import itertools


class Graph():
    def __init__(self):
        # Create empty graph
        self._container = {}

    def nodes(self):
        """Return a list of all nodes."""
        return [node for node in self._container.keys()]

    def edges(self):
        """Retun a list of all edges."""
        edges = []
        for node in self._container:
            for value in self._container[node]:
                edges.append((node, value))
        return edges

    def add_node(self, n):
        """Add node to graph."""
        pass

    def add_edge(self, n1, n2):
        """Add edge connecting node n1 to node n2.

        Creates nodes n1, n2 if necessary.
        """
        pass

    def del_node(self, n):
        """Delete node"""
        # if node doesn't exist: raise error
        # else: del node
        pass

    def del_edge(self, n1, n2):
        """Delete edge connecting n1 to n2."""
        # if edge doesn't exist: raise error
        # else: del edge
        pass

    def has_node(self, n):
        """Return True node exists."""
        pass

    def neighbors(n):
        """Return a list of all nodes connected to n by edges."""
        # if node doesn't exist: raise error
        # else: neighbors(n)
        pass

    def adjacent(n1, n2):
        """Return True if n1 is connected to n2 by an edge."""
        # if n1, n2 don't exist: raise error
        pass
