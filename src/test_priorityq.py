import pytest

INSERT_PARAMETERS = [
    ([(7, "banana")], (6, "apple"), [(7, "banana"), (6, "apple")]),
    ([(7, "banana")], (8, "pear"), [(8, "pear"), (7, "banana")]),
    ([(9, "pineapple"), (7, "banana")],
     (8, "pear"),
     [(9, "pineapple"), (7, "banana"), (8, "pear")]),
    ([(9, "pineapple"), (8, "pear"), (7, "banana")],
     (8, "second pear"),
     [(9, "pineapple"), (8, "pear"), (7, "banana"), (8, "second pear")]),
]

POP_LIST = [
    ([(9, "pineapple"), (8, "pear"), (7, "banana"), (8, "second pear")],
     [(9, "pineapple"), (8, "pear"), (8, "second pear"), (7, "banana")]),
]


def test_insert_on_empty():
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    pq.insert((7, "banana"))
    assert pq._container == [(7, "banana")]


@pytest.mark.parametrize(("populated_pq", "insert_item", "result_pq"), INSERT_PARAMETERS)
def test_insert(populated_pq, insert_item, result_pq):
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    pq._container = populated_pq
    pq.insert(insert_item)
    assert pq._container == result_pq


@pytest.mark.parametrize(("populated_pq", "pop_values"), POP_LIST)
def test_pop(populated_pq, pop_values):
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    pq._container = populated_pq
    for i in range(len(pq._container)):
        assert pq.pop() == pop_values[i]


@pytest.mark.parametrize(("populated_pq", "insert_item", "result_pq"), INSERT_PARAMETERS)
def test_peek_no_mutate(populated_pq, insert_item, result_pq):
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    pq._container = result_pq
    pq.peek()
    assert pq._container == result_pq


@pytest.mark.parametrize(("populated_pq", "insert_item", "result_pq"), INSERT_PARAMETERS)
def test_peek(populated_pq, insert_item, result_pq):
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    pq._container = result_pq
    assert pq.peek() == result_pq[0]
