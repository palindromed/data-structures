import pytest

DISPLAY = [
    ([], '()', ),
    ([1], '(1, )', ),
    ([1, 2], '(2, 1, )', ),
    ([1, 2, 3], '(3, 2, 1, )', ),
]


def test_init_empty_list():
    from linked_list import LinkedList
    new_list = LinkedList()
    assert new_list.head_node.value == None


def test_insert():
    from linked_list import LinkedList
    new_list = LinkedList()
    new_list.insert(5)
    assert new_list.head_node.value == 5
    new_list.insert(10)
    assert new_list.head_node.value == 10
    assert new_list.head_node.next.value == 5
    assert new_list.head_node.next.next.value == None


def test_pop():
    from linked_list import LinkedList
    new_list = LinkedList()
    new_list.insert(5)
    assert new_list.head_node.value == 5
    new_list.insert(10)
    assert new_list.head_node.value == 10
    assert new_list.head_node.next.value == 5
    assert new_list.head_node.next.next.value == None
    pop = new_list.pop()
    assert pop == 10
    assert new_list.head_node.value == 5
    assert new_list.head_node.next.value == None

    # pop all the way down to empty list
    new_list.pop()

    # then insert again
    new_list.insert(10)
    assert new_list.head_node.value == 10
    assert new_list.head_node.next.value == None


def test_size():
    # bad test because it relies on .insert(), .pop()
    from linked_list import LinkedList
    new_list = LinkedList()
    assert new_list.size() == 0
    new_list.insert(1)
    assert new_list.size() == 1
    new_list.insert(2)
    assert new_list.size() == 2
    new_list.pop()
    assert new_list.size() == 1
    new_list.pop()
    assert new_list.size() == 0

    new_list = LinkedList()
    for i in range(3):
        new_list.insert(i)
    new_list.size() == 3


def test_search():
    # using insert without iterable
    from linked_list import LinkedList
    new_list = LinkedList()
    new_list.insert(10)
    node = new_list.search(10)
    assert node.value == 10

    new_list.insert(20)
    new_list.insert(30)
    node = new_list.search(20)
    assert node.value == 20

    new_list = LinkedList()
    for i in range(3):
        new_list.insert(i)
    node = new_list.search(2)
    assert node.value == 2


def test_remove_in_list():
    from linked_list import LinkedList
    new_list = LinkedList()

    # populate list
    for i in range(4):
        new_list.insert(i)
        assert new_list.size() == i + 1

    # remove elements and test on size, search
    for i in range(4):
        new_list.remove(new_list.search(i))
        # testing on .size() makes sure whole list still linked
        assert new_list.size() == 3 - i
        new_list.search(i)  == "That node does not exist in the list."


def test_remove_not_in_list():
    from linked_list import LinkedList, Node
    new_list = LinkedList()
    for i in range(3):
        new_list.insert(i)
    new_list.remove(new_list.search(0))
    new_list.remove(new_list.search(1))
    new_list.remove(new_list.search(2))

    # item not in list
    node_not_in_list = Node("banana", None)
    assert new_list.remove(node_not_in_list) == "That node does not exist in the list."


@pytest.mark.parametrize(("in_", "expected"), DISPLAY)
def test_display(in_, expected):
    """Confirm linked list displaying properly."""
    import sys
    from linked_list import LinkedList
    from io import StringIO

    out = StringIO()
    sys.stdout = out
    ll = LinkedList(in_)
    ll.display()
    assert out.getvalue().strip() == expected
