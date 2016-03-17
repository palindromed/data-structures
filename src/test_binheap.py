
# -*- coding: utf-8 -*-

import pytest

ITERABLES = [
    ([1, 2, 3], [3, 1, 2]),
    ([3, 2, 1], [3, 2, 1]),
    ([3, 2, 1, 4], [4, 3, 1, 2])
]

POP_ITERABLES = [
    ([1], []),
    ([2, 3], [2]),
    ([1, 2, 3, 5, 22, 44], [22, 5, 2, 1, 3]),
    ([16, 14, 15, 9, 7, 6, 5, 1, 2, 3], [15, 14, 6, 9, 7, 3, 5, 1, 2])
]


def test_push():
    from binheap import BinHeap
    sample_list = [16, 14, 15, 9, 7, 6, 5, 1, 2, 3]
    bh = BinHeap(sample_list)
    sample_list.append(4)
    bh.push(4)
    assert bh._container == sample_list


def test_pop_empty_heap():
    from binheap import BinHeap
    bh = BinHeap()
    with pytest.raises(IndexError):
        bh.pop()


@pytest.mark.parametrize(("iterable", "expected"), POP_ITERABLES)
def test_pop(iterable, expected):
    from binheap import BinHeap
    bh = BinHeap(iterable)
    bh.pop()
    assert bh._container == expected


def test_init():
    from binheap import BinHeap
    bh = BinHeap()
    assert bh._container == []


@pytest.mark.parametrize(("iterable", "expected"), ITERABLES)
def test_init_from_iter(iterable, expected):
    from binheap import BinHeap
    bh = BinHeap(iterable)
    assert bh._container == expected
