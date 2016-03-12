import pytest

# TODO implement fixtures
#@pytest.fixture(scope='function')
#def buildup():
#    from double_linked_list import DoubleLinkedList
#    dll = DoubleLinkedList()
#    return dll


def test_insert_on_empty_list():
    # test insert single element to empty list
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


def test_append_on_empty_list():
    # test append single element on empty list
    from double_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.append(4)
    assert dll.tail_node.value == 4
    assert dll.tail_node.next == dll.tail_sentinal
    assert dll.tail_node.previous == dll.head_sentinal

    # list is 1 element long, so head and tail are that element
    assert dll.head_node.value == 4
    assert dll.head_node.next == dll.tail_sentinal
    assert dll.head_node.previous == dll.head_sentinal


def test_insert():
    # test multiple insert calls
    from double_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.insert(5)
    dll.insert(10)
    assert dll.head_node.value == 10
    assert dll.head_node.next.value == 5
    assert dll.head_node.previous == dll.head_sentinal

    assert dll.tail_node.value == 5
    assert dll.tail_node.next == dll.tail_sentinal
    assert dll.tail_node.previous == dll.head_node


def test_append():
    # test multiple append calls
    from double_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.append(4)
    dll.append(8)
    assert dll.head_node.value == 4
    assert dll.head_node.next.value == 8
    assert dll.head_node.previous == dll.head_sentinal

    assert dll.tail_node.value == 8
    assert dll.tail_node.next == dll.tail_sentinal
    assert dll.tail_node.previous == dll.head_node


def test_pop_singleton():
    from double_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.append(5)
    return_value = dll.pop()
    assert return_value == 5
    assert dll.head_node is None
    assert dll.tail_node is None


def test_pop_empty_list():
    from double_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    with pytest.raises(ValueError):
        dll.pop()


def test_pop():
    from double_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.append(5)
    dll.insert(10)
    dll.append(15)
    dll.insert(20)
    return_value_1 = dll.pop()
    assert return_value_1 == 20
    assert dll.head_node.value == 10



def test_shift_singleton():
    from double_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.append(5)
    return_value = dll.shift()
    assert return_value == 5
    assert dll.head_node is None
    assert dll.tail_node is None


def test_shift_empty_list():
    from double_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    with pytest.raises(ValueError):
        dll.shift()


def test_shift():
    from double_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.append(5)
    dll.insert(10)
    dll.append(15)
    dll.insert(20)
    # [20, 10, 5, 15]
    return_value_1 = dll.shift()
    assert return_value_1 == 15
    assert dll.tail_node.value == 5


def test_remove_empty_list():
    from double_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    with pytest.raises(ValueError):
        dll.remove(5)


def test_remove_value_not_in_list():
    from double_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.append(5)
    dll.insert(10)
    dll.append(15)
    dll.insert(20)
    with pytest.raises(ValueError):
        dll.remove('bananas')


def test_remove_value():
    from double_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.insert(3)
    dll.insert(2)
    dll.insert(1)
    dll.remove(2)
    assert dll.head_node.next.value == 3
    assert dll.tail_node.value == 3
    assert dll.tail_node.previous == dll.head_node

def test_remove__first_value():
    from double_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.insert(4)
    dll.insert(2)
    dll.insert(3)
    dll.insert(2)
    dll.insert(1)
    dll.remove(2)
    assert dll.head_node.next.value != 2
    assert dll.tail_node.previous.value == 2

def test_remove_tail():
    from double_linked_list import DoubleLinkedList
    dll = DoubleLinkedList()
    dll.insert(3)
    dll.insert(2)
    dll.insert(1)
    assert dll.tail_node.value == 3
    dll.remove(3)
    assert dll.tail_node.value == 2
    assert dll.tail_node.next == dll.tail_sentinal
