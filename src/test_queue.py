import pytest


def test_enqueue():
    from queue import Queue
    q = Queue()
    q.enqueue('q')
    assert q.container.head_node.value == 'q'


def test_dequeue():
    from queue import Queue
    q = Queue()
    with pytest.raises(ValueError):
        q.dequeue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue('q')
    # ['q', 2, 1]
    q.dequeue()
    assert q.container.head_node.value == 'q'
    assert q.container.tail_node.value == 2


def test_peek():
    from queue import Queue
    q = Queue()
    assert q.peek() is None
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue('q')
    assert q.peek() == 1


def test_size():
    from queue import Queue
    q = Queue()
    assert q.size() == 0
    q.enqueue(123)
    assert q.size() == 1
    q.enqueue(234)
    assert q.size() == 2
    q.enqueue(345)
    assert q.size() == 3
    q.dequeue()
    assert q.size() == 2
    q.dequeue()
    assert q.size() == 1
    q.dequeue()
