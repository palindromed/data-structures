import pytest
# TODO: use same globals for reverse operations such as add, remove

GRAPHS = [
    ({},
     [],
     []),
    ({'nodeA': set()},
     ['nodeA'],
     []),
    ({'nodeA': {'nodeB'}, 'nodeB': set()},
     ['nodeA', 'nodeB'],
     [('nodeA', 'nodeB')]),
    ({'nodeA': {'nodeB'}, 'nodeB': {'nodeA'}},
     ['nodeA', 'nodeB'],
     [('nodeA', 'nodeB'), ('nodeB', 'nodeA')]),
    ({'nodeA': {'nodeB', 'nodeC'}, 'nodeB': {'nodeA'}, 'nodeC': {'nodeA', 'nodeC'}},
     ['nodeA', 'nodeB', 'nodeC'],
     [('nodeA', 'nodeB'), ('nodeA', 'nodeC'), ('nodeB', 'nodeA'), ('nodeC', 'nodeA'), ('nodeC', 'nodeC')]),
]

GRAPHS_FOR_NODE_INSERT = [
    ({},
     'nodeN',
     {'nodeN': set()}),
    ({'nodeA': {'nodeB', 'nodeC'}},
     'nodeN',
     {'nodeA': {'nodeB', 'nodeC'}, 'nodeN': set()}),
    ({'nodeA': {'nodeA', 'nodeB'}, 'nodeB': {'nodeC', 'nodeA'}},
     'nodeN',
     {'nodeA': {'nodeA', 'nodeB'}, 'nodeB': {'nodeC', 'nodeA'}, 'nodeN': set()}),
]


GRAPHS_ADD_EDGE = [
    ({'nodeA': {'nodeB'}, 'nodeB': {'nodeA'}},
     "nodeX",
     "nodeY",
     {'nodeA': {'nodeB'}, 'nodeB': {'nodeA'}, 'nodeX': {'nodeY'}, 'nodeY': set()}),
    ({'nodeA': {'nodeB'}, 'nodeB': {'nodeA'}},
     'nodeA',
     'nodeB',
     {'nodeA': {'nodeB'}, 'nodeB': {'nodeA'}}),
    ({'nodeA': {'nodeB', 'nodeC'}, 'nodeB': {'nodeA'}, 'nodeC': {'nodeA', 'nodeC'}},
     'nodeB',
     'nodeC',
     {'nodeA': {'nodeB', 'nodeC'}, 'nodeB': {'nodeA', 'nodeC'}, 'nodeC': {'nodeA', 'nodeC'}}),
]

GRAPHS_DEL_NODE = [
    ({'nodeA': {'nodeB'}, 'nodeB': {'nodeA'}, 'nodeX': {'nodeY'}, 'nodeY': set()},
     'nodeA',
     {'nodeB': set(), 'nodeX': {'nodeY'}, 'nodeY': set()}),
    ({'nodeA': {'nodeB'}, 'nodeB': {'nodeA'}},
     'nodeB',
     {'nodeA': set()}),
]

GRAPHS_DEL_EDGE = [
    ({'nodeA': {'nodeB'}, 'nodeB': set()},
     'nodeA',
     'nodeB',
     {'nodeA': set(), 'nodeB': set()}),
    ({'nodeA': {'nodeB', 'nodeC'}, 'nodeB': set(), 'nodeC': set()},
     'nodeA',
     'nodeB',
     {'nodeA': {'nodeC'}, 'nodeB': set(), 'nodeC': set()})
]

NEIGHBORS = [
    ({'nodeA': set(), 'nodeB': {'nodeA'}},
     'nodeB',
     ['nodeA']),
    ({'nodeA': set(), 'nodeB': {'nodeA'}},
     'nodeA',
     []),
    # ({'nodeA': set(), 'nodeB': {'nodeA'}, 'nodeC': {'nodeA'}},
    #  'nodeA',
    #  ['nodeB', 'nodeC']),
    ({'nodeA': {'nodeB', 'nodeC'}, 'nodeB': {'nodeA'}, 'nodeC': {'nodeA'}},
     'nodeA',
     ['nodeB', 'nodeC']),
]

ADJACENT = [
    ({'nodeA': {'nodeB'}, 'nodeB': set()}, 'nodeA', 'nodeB', True),
    ({'nodeA': {'nodeB'}, 'nodeB': set()}, 'nodeB', 'nodeA', False),
]

ADJACENT_NODES_GONE = [
    ({'nodeA': {'nodeB'}, 'nodeB': set()}, 'nodeX', 'nodeB'),
    ({'nodeA': {'nodeB'}, 'nodeB': set()}, 'nodeX', 'nodeY'),
    ({'nodeA': {'nodeB'}, 'nodeB': set()}, 'nodeA', 'nodeY'),
]


NODE_TRAVERSAL_BREADTH = [
    ({'A': {'B', 'C'}, 'B': {'A', 'D', 'E'}, 'C': {'A', 'F', 'G'},
        'D': {'B', 'H'}, 'E': {'B'}, 'F': {'C'}, 'G': {'C'}, 'H': {'D'}},
        'A',
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']),
    ({'A': {'B', 'C'}, 'B': {'C', 'D'}, 'C': set(), 'D': set()},
     'A',
     ['A', 'B', 'C', 'D'])
]

NODE_TRAVERSAL_DEPTH = [
    ({'A': {'B', 'E'}, "B": {'C', 'D'}, 'E': set(), 'C': set(), 'D': set()},
     'A',
     ['A', 'B', 'C', 'D', 'E']),
    ({'A': {'B', 'E'}, "B": {'C', 'D'}, 'E': set(), 'C': {'A', 'E'}, 'D': set()},
     'A',
     ['A', 'B', 'C', 'D', 'E']),
]


@pytest.fixture
def graph_fixture(scope='function'):
    from graph import Graph
    return Graph()


@pytest.mark.parametrize(("built_graph", "node", "expected"), GRAPHS_DEL_NODE)
def test_del_node_exists(graph_fixture, built_graph, node, expected):
    graph_fixture._container = built_graph
    graph_fixture.del_node(node)
    assert graph_fixture._container == expected


@pytest.mark.parametrize(("built_graph", "node_list", "edge_list"), GRAPHS)
def test_nodes(graph_fixture, built_graph, node_list, edge_list):
    graph_fixture._container = built_graph
    result = graph_fixture.nodes()
    assert set(result) == set(node_list)


@pytest.mark.parametrize(("built_graph", "node_list", "edge_list"), GRAPHS)
def test_edges(graph_fixture, built_graph, node_list, edge_list):
    graph_fixture._container = built_graph
    result = graph_fixture.edges()
    assert set(edge_list) == set(result)


@pytest.mark.parametrize(("built_graph", "new_node", "expected"), GRAPHS_FOR_NODE_INSERT)
def test_add_node(graph_fixture, built_graph, new_node, expected):
    graph_fixture._container = built_graph
    graph_fixture.add_node(new_node)
    assert graph_fixture._container == expected


@pytest.mark.parametrize(("built_graph", "n1", "n2", "expected"), GRAPHS_ADD_EDGE)
def test_add_edge(graph_fixture, built_graph, n1, n2, expected):
    graph_fixture._container = built_graph
    graph_fixture.add_edge(n1, n2)
    assert graph_fixture._container == expected


def test_del_node_not_exists(graph_fixture):
    graph_fixture._container = {'nodeA': {'nodeA'}, 'nodeB': set()}
    with pytest.raises(KeyError):
        graph_fixture.del_node('nodeX')


@pytest.mark.parametrize(("built_graph", "node1", "node2", "expected"), GRAPHS_DEL_EDGE)
def test_del_edge(graph_fixture, built_graph, node1, node2, expected):
    graph_fixture._container = built_graph
    graph_fixture.del_edge(node1, node2)
    assert graph_fixture._container == expected


def test_del_edge_not_exists(graph_fixture):
    graph_fixture._container = {'nodeA': set()}
    with pytest.raises(ValueError):
        graph_fixture.del_edge('nodeA', 'nodeB')


def test_has_node_true(graph_fixture):
    graph_fixture._container = {'nodeA': set()}
    assert graph_fixture.has_node('nodeA')


def test_has_node_false(graph_fixture):
    graph_fixture._container = {'nodeA': set()}
    assert not graph_fixture.has_node('nodeB')


@pytest.mark.parametrize(("built_graph", 'node', 'expected'), NEIGHBORS)
def test_neighbors(graph_fixture, built_graph, node, expected):
    graph_fixture._container = built_graph
    assert set(graph_fixture.neighbors(node)) == set(expected)


def test_neighbors_none(graph_fixture):
    graph_fixture._container = {'nodeA': set()}
    with pytest.raises(KeyError):
        graph_fixture.neighbors('nodeB')


@pytest.mark.parametrize(('built_graph', 'n1', 'n2', 'expected'), ADJACENT)
def test_adjacent(graph_fixture, built_graph, n1, n2, expected):
    # if n1, n2 don't exist: raise error
    graph_fixture._container = built_graph
    assert graph_fixture.adjacent(n1, n2) == expected


@pytest.mark.parametrize(('built_graph', 'n1', 'n2'), ADJACENT_NODES_GONE)
def test_adjacent_not_exists(graph_fixture, built_graph, n1, n2):
    # if n1, n2 don't exist: raise error
    graph_fixture._container = built_graph
    with pytest.raises(KeyError):
        graph_fixture.adjacent(n1, n2)

@pytest.mark.parametrize(('built_graph', 'node', 'expected'), NODE_TRAVERSAL_BREADTH)
def test_traverse_breadth(graph_fixture, built_graph, node, expected):
    graph_fixture._container = built_graph
    assert graph_fixture.breadth_first_traversal(node) == expected

def test_empty_graph_breadth(graph_fixture):
    graph_fixture._container = {}
    with pytest.raises(IndexError):
        graph_fixture.breadth_first_traversal('X')

@pytest.mark.parametrize(('built_graph', 'node', 'expected'), NODE_TRAVERSAL_DEPTH)
def test_traverse_depth(graph_fixture, built_graph, node, expected):
    graph_fixture._container = built_graph
    assert graph_fixture.depth_first_traversal(node) == expected














