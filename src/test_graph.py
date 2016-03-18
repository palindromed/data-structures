import pytest

GRAPHS = [
    ({},
     [],
     []),
    ({'nodeA': {}},
     ['nodeA'],
     []),
    ({'nodeA': {'nodeB'}, 'nodeB': {}},
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
     {'nodeN': {}}),
    ({'nodeA': {'nodeB', 'nodeC'}},
     'nodeN',
     {'nodeA': {'nodeB', 'nodeC'}, 'nodeN': {}}),
    ({'nodeA': {'nodeA', 'nodeB'}, 'nodeB': {'nodeC', 'nodeA'}},
     'nodeN',
     {'nodeA': {'nodeA', 'nodeB'}, 'nodeB': {'nodeC', 'nodeA'}, 'nodeN': {}}),
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


# @pytest.mark.parametrize(("built_graph", "new_node", "expected"), GRAPHS_FOR_NODE_INSERT)
# def test_add_node(graph_fixture, built_graph, new_node, expected):
#     graph_fixture._container = built_graph
#     graph_fixture.add_node(new_node)
#     assert graph_fixture._container == expected
#     pass


# def test_add_edge(graph_fixture, n1, n2):
#     pass
# 
# 
# def test_del_node(graph_fixture, n):
#     # if node doesn't exist: raise error
#     # else: del node
#     pass
# 
# 
# def test_del_edge(graph_fixture, n1, n2):
#     # if edge doesn't exist: raise error
#     # else: del edge
#     pass
# 
# 
# def test_has_node(graph_fixture, n):
#     pass
# 
# 
# def test_neighbors(graph_fixture, n):
#     # if node doesn't exist: raise error
#     # else: neighbors(graph_fixture, n)
#     pass
# 
# 
# def test_adjacent(graph_fixture, n1, n2):
#     # if n1, n2 don't exist: raise error
#     pass
