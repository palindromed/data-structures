import pytest

INSERT_PARAMETERS = [
    ([None, (7, "banana")], (6, "apple"), [None, (7, "banana"), (6, "apple")]),
    ([None, (7, "banana")], (8, "pear"), [None, (8, "pear"), (7, "banana")]),
    ([None, (9, "pineapple"), (7, "banana")],
     (8, "pear"),
     [None, (9, "pineapple"), (8, "pear"), (7, "banana")]),
    ([None, (9, "pineapple"), (8, "pear"), (7, "banana")],
     (8, "second pear"),
     [None, (9, "pineapple"), (8, "pear"), (8, "second pear"), (7, "banana")]),
]


def test_insert_on_empty():
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    pq.insert((7, "banana"))
    assert pq._container == [None, (7, "banana")]


@pytest.mark.parametrize(("populated_pq", "insert_item", "result_pq"), INSERT_PARAMETERS)
def test_insert(populated_pq, insert_item, result_pq):
    from priorityq import PriorityQueue
    pq = PriorityQueue()
    pq._container = populated_pq
    pq.insert(insert_item)
    assert pq._container == result_pq


def test_pop():
    assert False


def test_peek():
    assert False
