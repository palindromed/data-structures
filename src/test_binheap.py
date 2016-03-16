
# -*- coding: utf-8 -*-

import pytest


# @pytest.fixture
# def create_heap_for_tests(scope="function"):
#     from binheap import BinHeap
#     sample_list = [16, 14, 15, 9, 7, 6, 5, 1, 2, 3]
#     bh = BinHeap(sample_list)

ITERABLES = [
    ([1, 2, 3], [None, 3, 1, 2]),
    ([3, 2, 1], [None, 3, 2, 1]),
    ([3, 2, 1, 4], [None, 4, 3, 1, 2])
]

POP_ITERABLES = [
    ([1, 2, 3, 5, 22, 44], [None, 22, 5, 2, 1, 3]),
    ([16, 14, 15, 9, 7, 6, 5, 1, 2, 3], [None, 15, 14, 6, 9, 7, 3, 5, 1, 2])
]

def test_push():
    from binheap import BinHeap
    sample_list = [16, 14, 15, 9, 7, 6, 5, 1, 2, 3]
    bh = BinHeap(sample_list)
    sample_list.insert(0, None)
    sample_list.append(4)
    bh.push(4)
    assert bh._container == sample_list


# def test_push_larger_value():


def test_pop_empty_heap():
    from binheap import BinHeap
    bh = BinHeap()
    with pytest.raises(IndexError):
        bh.pop()


# def test_pop():
#     from binheap import BinHeap
#     bh = BinHeap([1, 2, 3])
#     bh.pop()
#     # [3, 2, 1]
#     # [1, 2, 3]
#     # [1, 2]
#     # [2, 1]
#     assert bh._container == [None, 2, 1]

@pytest.mark.parametrize(("iterable", "expected"), POP_ITERABLES)
def test_pop(iterable, expected):
    from binheap import BinHeap
    bh = BinHeap(iterable)
    bh.pop()
    assert bh._container == expected


def test_init():
    from binheap import BinHeap
    bh = BinHeap()
    assert bh._container == [None]


@pytest.mark.parametrize(("iterable", "expected"), ITERABLES)
def test_init_from_iter(iterable, expected):
    from binheap import BinHeap
    bh = BinHeap(iterable)
    assert bh._container == expected
