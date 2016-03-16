# -*- coding: utf-8 -*-

import pytest


# @pytest.fixture
# def create_heap_for_tests(scope="function"):
#     from binheap import BinHeap
#     sample_list = [16, 14, 15, 9, 7, 6, 5, 1, 2, 3]
#     bh = BinHeap(sample_list)


def test_push():
    from binheap import BinHeap
    sample_list = [16, 14, 15, 9, 7, 6, 5, 1, 2, 3]
    bh = BinHeap(sample_list)
    bh.push(4)
    assert bh._container == sample_list.append(4)


# def test_push_larger_value():


def test_pop_empty_heap():
    from binheap import BinHeap
    bh = BinHeap()
    with pytest.raises(IndexError):
        bh.pop()


def test_pop():
    from binheap import BinHeap
    bh = BinHeap([1, 2, 3])
    bh.pop()
    # [3, 2, 1]
    # [1, 2, 3]
    # [1, 2]
    # [2, 1]
    assert bh._container == [None, 2, 1]
