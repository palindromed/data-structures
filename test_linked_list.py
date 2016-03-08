import pytest


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


def test_remove():
    from linked_list import LinkedList
    new_list = LinkedList()

    # test without iterable
    for i in range(4):
        new_list.insert(i)
    for i in range(4):
        new_list.remove(i)
        # testing on .size() makes sure whole list still linked
        assert new_list.size() == 4 - i
        new_list.search(i)  == "That node does not exist in the list."

    new_list = LinkedList()
    for i in range(3):
        new_list.insert(i)
    for i in range(4):
        new_list.remove(i)
        # testing on .size() makes sure whole list still linked
        assert new_list.size() == 4 - i
        new_list.search(i)  == "That node does not exist in the list."


# def test_display():
#     from linked_list import LinkedList
#     new_list = LinkedList()
#     assert new_list.display() == '()'
