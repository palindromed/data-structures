import pytest

# TODO implement fixtures
#@pytest.fixture(scope='function')
#def buildup():
#    from double_linked_list import DoubleLinkedList
#    dll = DoubleLinkedList()
#    return dll


def test_insert():
    from double_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.insert(5)
    assert dll.head_node.value == 5
    assert dll.head_node.next == dll.tail_sentinal
    assert dll.head_node.previous == dll.head_sentinal

    # list is 1 element long, so head and tail are that element
    assert dll.tail_node.value == 5
    assert dll.tail_node.next == dll.tail_sentinal
    assert dll.tail_node.previous == dll.head_sentinal


def test_append():
    from double_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.append(4)
    assert dll.tail_node.value == 5
    assert dll.tail_node.next == dll.tail_sentinal
    assert dll.tail_node.previous == dll.head_sentinal

    # list is 1 element long, so head and tail are that element
    assert dll.head_node.value == 5
    assert dll.head_node.next == dll.tail_sentinal
    assert dll.head_node.previous == dll.head_sentinal




# def test_pop_from_append():
#     from double_linked_list import DoubleLinkedList
#     dll = DoubleLinkedList()
#     dll.append(5)
#     dll.append('banana')
#     return_value = dll.pop()
#     assert return_value == 5
#     assert dll.head_node.value == 'banana'
#     dll.pop()
#     assert dll.head_node == None
#     assert dll.tail_node == None
#     with pytest.raises(AttributeError):
#         dll.head_node.value == None
#         dll.head_node.next == None
#         dll.head_node.previous == None

#         dll.tail_node.value == None
#         dll.tail_node.next == None
#         dll.tail_node.previous == None

# def test_pop_from_insert():
#     from double_linked_list import DoubleLinkedList
#     dll = DoubleLinkedList()
#     dll.insert(5)
#     dll.insert('banana')
#     return_value = dll.pop()
#     assert return_value == 'banana'
#     assert dll.head_node.value == 5
