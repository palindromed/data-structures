import pytest

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
    ({'nodeA': {'nodeB'}, 'nodeB': {'nodeA'}}, "nodeX", "nodeY",
      {'nodeA': {'nodeB'}, 'nodeB': {'nodeA'}, 'nodeX': {'nodeY'}, 'nodeY': set()}),
    ({'nodeA': {'nodeB'}, 'nodeB': {'nodeA'}}, 'nodeA', 'nodeB',
     {'nodeA': {'nodeB'}, 'nodeB': {'nodeA'}}),
    ({'nodeA': {'nodeB', 'nodeC'}, 'nodeB': {'nodeA'}, 'nodeC': {'nodeA', 'nodeC'}},
        'nodeB', 'nodeC',
    {'nodeA': {'nodeB', 'nodeC'}, 'nodeB': {'nodeA', 'nodeC'}, 'nodeC': {'nodeA', 'nodeC'}}),

]


GRAPHS_NODE_DELETE = [
    ({'nodeA': {'nodeB', 'nodeC'}, 'nodeB': {'nodeA', 'nodeC'}, 'nodeC': {'nodeA', 'nodeC'}},
    'nodeC', {'nodeA': {'nodeB'}, 'nodeB': {'nodeA'}}),
    ({'nodeA': {'nodeB'}, 'nodeB': {'nodeA'}, 'nodeX': {'nodeY'}, 'nodeY': {'nodeX'}},
    'nodeX', {'nodeA': {'nodeB'}, 'nodeB': {'nodeA'}, 'nodeY': set()})

]

IS_NODE_IN_GRAPH = [
    ({'nodeA': {'nodeB', 'nodeC'}, 'nodeB': {'nodeA', 'nodeC'}, 'nodeC': {'nodeA', 'nodeC'}},
    'nodeC', True),
    ( {'nodeA': {'nodeB'}, 'nodeB': {'nodeA'}, 'nodeX': {'nodeY'}, 'nodeY': {'nodeA'}},
     'banana', False)
]

GRAPH_TEST_EDGE = [
    ({'nodeA': {'nodeB', 'nodeC'}, 'nodeB': {'nodeA', 'nodeC'}, 'nodeC': {'nodeA', 'nodeC'}},
     'nodeA', 'nodeB', {'nodeA': {'nodeC'}, 'nodeB': {'nodeA', 'nodeC'}, 'nodeC': {'nodeA', 'nodeC'}}),
    ({'nodeA': {'nodeB'}, 'nodeB': {'nodeA'}, 'nodeX': {'nodeY'}, 'nodeY': {'nodeB'}},
     'nodeB', 'nodeA', {'nodeA': {'nodeB'}, 'nodeB': set(), 'nodeX': {'nodeY'}, 'nodeY': {'nodeB'}})
    ]

@pytest.fixture
def graph_fixture(scope='function'):
    from graph import Graph
    return Graph()


@pytest.mark.parametrize(("built_graph", "node_list", "edge_list"), GRAPHS)
def test_nodes(graph_fixture, built_graph, node_list, edge_list):
    # TODO: make test tighter
    graph_fixture._container = built_graph
    result = graph_fixture.nodes()
    for node in node_list:
        assert node in result
    for node in result:
        assert node in node_list


@pytest.mark.parametrize(("built_graph", "node_list", "edge_list"), GRAPHS)
def test_edges(graph_fixture, built_graph, node_list, edge_list):
    graph_fixture._container = built_graph
    result = graph_fixture.edges()
    for edge in edge_list:
        assert edge in result
    for edge in result:
        assert edge in edge_list


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


def test_del_node_not_in_graph(graph_fixture):
    graph_fixture._container = {'nodeA': {'nodeB'}, 'nodeB': {'nodeA'}}
    with pytest.raises(KeyError):
        graph_fixture.del_node('nodeZ')

@pytest.mark.parametrize(("built_graph", "node", "expected"), GRAPHS_NODE_DELETE)
def test_del_node_in_graph(graph_fixture, built_graph, node, expected):
    """Delete node n from graph"""
    graph_fixture._container = built_graph
    graph_fixture.del_node(node)
    assert graph_fixture._container == expected

@pytest.mark.parametrize(("built_graph", 'n1', 'n2', 'expected'), GRAPH_TEST_EDGE)
def test_del_edge(graph_fixture, built_graph, n1, n2, expected):
    # if edge doesn't exist: raise error
    # else: del edge
    graph_fixture._container = built_graph
    graph_fixture.del_edge(n1, n2)
    assert graph_fixture._container == expected



@pytest.mark.parametrize(("built_graph", "node", "expected"), IS_NODE_IN_GRAPH)
def test_has_node(graph_fixture, built_graph, node, expected):
    graph_fixture._container = built_graph
    assert graph_fixture.has_node(node) == expected



# def test_neighbors(graph_fixture, n):
#     # if node doesn't exist: raise error
#     # else: neighbors(graph_fixture, n)
#     pass
# 
# 
# def test_adjacent(graph_fixture, n1, n2):
#     # if n1, n2 don't exist: raise error
#     pass
