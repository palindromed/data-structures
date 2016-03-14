import pytest


def test_init():
    from stack import Stack
    from linked_list import LinkedList, Node
    stk = Stack()
    assert stk.pop() == "The list is empty."


def test_init_param():
    from stack import Stack
    from linked_list import LinkedList, Node
    stk = Stack([1, 2, 3])
    assert stk.pop() == 3


def test_push():
    from stack import Stack
    from linked_list import LinkedList, Node
    stk = Stack()
    stk.push(5)
    assert stk.pop() == 5


def test_pop():
    from stack import Stack
    from linked_list import LinkedList, Node
    stk = Stack()
    stk.push('banana')
    assert stk.pop() == 'banana'
