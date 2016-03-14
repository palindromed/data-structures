import pytest

def test_append():
    from deque import Deque
    d = Deque()
    d.append(9)
    assert d.dll.tail_node.value == 9


def test_appendleft():
    from deque import Deque
    d = Deque()
    d.appendleft(8)
    assert d.dll.head_node.value == 8


def test_pop_empty():
    from deque import Deque
    d = Deque()
    with pytest.raises (ValueError):
        d.pop(8)


def test_pop():
    from deque import Deque
    d = Deque()
    d.append(9)
    d.append(8)
    assert d.pop() == 8
    assert d.dll.tail_node.value == 9
    assert d.dll.head_node.value == 9


def test_popleft():
    from deque import Deque
    d = Deque()
    d.append(9)
    d.append(8)
    assert d.popleft() == 9
    assert d.dll.tail_node.value == 8
    assert d.dll.tail_node.value == 8


def test_peek():
    from deque import Deque
    d = Deque()
    d.append(9)
    assert d.peek() == 9


def test_peekleft():
    from deque import Deque
    d = Deque()
    d.appendleft(9)
    assert d.peekleft() == 9


def test_size():
    from deque import Deque
    d = Deque()
    assert d.size == 0
    d.append(9)
    d.append(8)
    d.appendleft(7)
    assert d.size() == 3

