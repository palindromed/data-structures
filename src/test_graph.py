import pytest
# TODO: use same globals for reverse operations such as add, remove

GRAPHS = [
    ({},
     [],
     []),
    ({'nodeA': {}},
     ['nodeA'],
     []),
    ({'nodeA': {'nodeB': 'weight'},
      'nodeB': {}},
     ['nodeA', 'nodeB'],
     [('nodeA', 'nodeB')]),
    ({'nodeA': {'nodeB': 'weight'},
      'nodeB': {'nodeA': 'weight'}},
     ['nodeA', 'nodeB'],
     [('nodeA', 'nodeB'), ('nodeB', 'nodeA')]),
    ({'nodeA': {'nodeB': 'weight', 'nodeC': 'weight'},
      'nodeB': {'nodeA': 'weight'},
      'nodeC': {'nodeA': 'weight', 'nodeC': 'weight'}},
     ['nodeA', 'nodeB', 'nodeC'],
     [('nodeA', 'nodeB'),
      ('nodeA', 'nodeC'),
      ('nodeB', 'nodeA'),
      ('nodeC', 'nodeA'),
      ('nodeC', 'nodeC')]),
]

GRAPHS_FOR_NODE_INSERT = [
    ({},
     'nodeN',
     {'nodeN': {}}),
    ({'nodeA': {'nodeB': 'weight', 'nodeC': 'weight'}},
     'nodeN',
     {'nodeA': {'nodeB': 'weight', 'nodeC': 'weight'},
      'nodeN': {}}),
    ({'nodeA': {'nodeA': 'weight', 'nodeB': 'weight'},
      'nodeB': {'nodeC': 'weight', 'nodeA': 'weight'}},
     'nodeN',
     {'nodeA': {'nodeA': 'weight', 'nodeB': 'weight'},
      'nodeB': {'nodeC': 'weight', 'nodeA': 'weight'},
      'nodeN': {}}),
]


GRAPHS_ADD_EDGE = [
    ({'nodeA': {'nodeB': 'weight'},
      'nodeB': {'nodeA': 'weight'}},
     "nodeX",
     "nodeY",
     {'nodeA': {'nodeB': 'weight'},
      'nodeB': {'nodeA': 'weight'},
      'nodeX': {'nodeY': 'weight'},
      'nodeY': {}}),
    ({'nodeA': {'nodeB': 'weight'},
      'nodeB': {'nodeA': 'weight'}},
     'nodeA',
     'nodeB',
     {'nodeA': {'nodeB': 'weight'},
      'nodeB': {'nodeA': 'weight'}}),
    ({'nodeA': {'nodeB': 'weight', 'nodeC': 'weight'},
      'nodeB': {'nodeA': 'weight'},
      'nodeC': {'nodeA': 'weight', 'nodeC': 'weight'}},
     'nodeB',
     'nodeC',
     {'nodeA': {'nodeB': 'weight', 'nodeC': 'weight'},
      'nodeB': {'nodeA': 'weight', 'nodeC': 'weight'},
      'nodeC': {'nodeA': 'weight', 'nodeC': 'weight'}}),
]

GRAPHS_DEL_NODE = [
    ({'nodeA': {'nodeB': 'weight'},
      'nodeB': {'nodeA': 'weight'},
      'nodeX': {'nodeY': 'weight'},
      'nodeY': {}},
     'nodeA',
     {'nodeB': {},
      'nodeX': {'nodeY': 'weight'},
      'nodeY': {}}),
    ({'nodeA': {'nodeB': 'weight'},
      'nodeB': {'nodeA': 'weight'}},
     'nodeB',
     {'nodeA': {}}),
]

GRAPHS_DEL_EDGE = [
    ({'nodeA': {'nodeB': 'weight'},
      'nodeB': {}},
     'nodeA',
     'nodeB',
     {'nodeA': {},
      'nodeB': {}}),
    ({'nodeA': {'nodeB': 'weight', 'nodeC': 'weight'},
      'nodeB': {},
      'nodeC': {}},
     'nodeA',
     'nodeB',
     {'nodeA': {'nodeC': 'weight'},
      'nodeB': {},
      'nodeC': {}})
]

NEIGHBORS = [
    ({'nodeA': {},
      'nodeB': {'nodeA': 'weight'}},
     'nodeB',
     ['nodeA']),
    ({'nodeA': {},
      'nodeB': {'nodeA': 'weight'}},
     'nodeA',
     []),
    ({'nodeA': {'nodeB': 'weight', 'nodeC': 'weight'},
      'nodeB': {'nodeA': 'weight'},
      'nodeC': {'nodeA': 'weight'}},
     'nodeA',
     ['nodeB', 'nodeC']),
]

ADJACENT = [
    ({'nodeA': {'nodeB': 'weight'},
      'nodeB': {}},
     'nodeA',
     'nodeB',
     True),
    ({'nodeA': {'nodeB': 'weight'},
      'nodeB': {}},
     'nodeB',
     'nodeA',
     False),
]

ADJACENT_NODES_GONE = [
    ({'nodeA': {'nodeB': 'weight'},
      'nodeB': {}},
     'nodeX', 'nodeB'),
    ({'nodeA': {'nodeB': 'weight'},
      'nodeB': {}},
     'nodeX', 'nodeY'),
    ({'nodeA': {'nodeB': 'weight'},
      'nodeB': {}},
     'nodeA', 'nodeY'),
]


NODE_TRAVERSAL_BREADTH = [
    ({'A': {'B': 'weight', 'C': 'weight'},
      'B': {'A': 'weight', 'D': 'weight', 'E': 'weight'},
      'C': {'A': 'weight', 'F': 'weight', 'G': 'weight'},
      'D': {'B': 'weight', 'H': 'weight'},
      'E': {'B': 'weight'},
      'F': {'C': 'weight'},
      'G': {'C': 'weight'},
      'H': {'D': 'weight'}},
     'A',
     ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']),
    ({'A': {'B': 'weight', 'C': 'weight'},
      'B': {'C': 'weight', 'D': 'weight'},
      'C': {},
      'D': {}},
     'A',
     ['A', 'B', 'C', 'D']),
    ({'a': {}}, 'a', ['a']),
]

NODE_TRAVERSAL_DEPTH = [
    ({'A': {'B': 'weight', 'E': 'weight'},
      "B": {'C': 'weight', 'D': 'weight'},
      'E': {},
      'C': {},
      'D': {}},
     'A',
     ['A', 'E', 'B', 'D', 'C']),
    ({'A': {'B': 'weight', 'E': 'weight'},
      "B": {'C': 'weight', 'D': 'weight'},
      'E': {},
      'C': {'A': 'weight', 'E': 'weight'},
      'D': {}},
     'A',
     ['A', 'E', 'B', 'D', 'C']),
    ({'a': {'b': 'weight', 'g': 'weight'},
      'b': {'c': 'weight'},
      'g': {'h': 'weight', 'j': 'weight'},
      'c': {'d': 'weight'},
      'h': {'i': 'weight'},
      'j': {'k': 'weight'},
      'd': {'e': 'weight', 'f': 'weight'},
      'i': {},
      'k': {},
      'e': {},
      'f': {}},
     'a',
     ['a', 'g', 'j', 'k', 'h', 'i', 'b', 'c', 'd', 'f', 'e']),
    ({'a': {}}, 'a', ['a']),
]

GET_WEIGHT = [
    ({'A': {'B': 'weight1', 'E': 'weight2'},
      "B": {'C': 'weight3', 'D': 'weight4'},
      'E': {},
      'C': {},
      'D': {}},
     'A',
     'B',
     'weight1',),
    ({'A': {'B': 'weight1', 'E': 'weight2'},
      "B": {'C': 'weight3', 'D': 'weight4'},
      'E': {},
      'C': {},
      'D': {}},
     'B',
     'C',
     'weight3',),
    ({'A': {'B': 'weight1', 'E': 'weight2'},
      "B": {'C': 'weight3', 'D': 'weight4'},
      'E': {},
      'C': {},
      'D': {}},
     'B',
     'D',
     'weight4',),
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


@pytest.mark.parametrize(("built_graph", "new_node", "expected"),
                         GRAPHS_FOR_NODE_INSERT)
def test_add_node(graph_fixture, built_graph, new_node, expected):
    graph_fixture._container = built_graph
    graph_fixture.add_node(new_node)
    assert graph_fixture._container == expected


@pytest.mark.parametrize(("built_graph", "n1", "n2", "expected"),
                         GRAPHS_ADD_EDGE)
def test_add_edge(graph_fixture, built_graph, n1, n2, expected):
    graph_fixture._container = built_graph
    graph_fixture.add_edge(n1, n2)
    assert graph_fixture._container == expected


def test_del_node_not_exists(graph_fixture):
    graph_fixture._container = {'nodeA': {'nodeA': 'weight'}, 'nodeB': {}}
    with pytest.raises(KeyError):
        graph_fixture.del_node('nodeX')


@pytest.mark.parametrize(("built_graph", "node1", "node2", "expected"),
                         GRAPHS_DEL_EDGE)
def test_del_edge(graph_fixture, built_graph, node1, node2, expected):
    graph_fixture._container = built_graph
    graph_fixture.del_edge(node1, node2)
    assert graph_fixture._container == expected


def test_del_edge_not_exists(graph_fixture):
    graph_fixture._container = {'nodeA': {}}
    with pytest.raises(ValueError):
        graph_fixture.del_edge('nodeA', 'nodeB')


def test_has_node_true(graph_fixture):
    graph_fixture._container = {'nodeA': {}}
    assert graph_fixture.has_node('nodeA')


def test_has_node_false(graph_fixture):
    graph_fixture._container = {'nodeA': {}}
    assert not graph_fixture.has_node('nodeB')


@pytest.mark.parametrize(("built_graph", 'node', 'expected'), NEIGHBORS)
def test_neighbors(graph_fixture, built_graph, node, expected):
    graph_fixture._container = built_graph
    assert set(graph_fixture.neighbors(node)) == set(expected)


def test_neighbors_none(graph_fixture):
    graph_fixture._container = {'nodeA': {}}
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


def test_traverse_depth_empty(graph_fixture):
    graph_fixture._container = {}
    with pytest.raises(IndexError):
        graph_fixture.depth_first_traversal('node')


@pytest.mark.parametrize(('built_graph', 'n1', 'n2', 'expected'), GET_WEIGHT)
def test_get_weight(graph_fixture, built_graph, n1, n2, expected):
    graph_fixture._container = built_graph
    assert graph_fixture.get_weight(n1, n2) == expected
