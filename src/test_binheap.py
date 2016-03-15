# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def create_heap_for_tests():
    from binheap import BinHeap
    sample_list = [None, 16, 14, 15, 9, 7, 6, 5, 1, 2, 3]
    bh = BinHeap(sample_list)


def test_push():
    bh.push(4)
    assert bh._container == sample_list.append(4)


def test_push_larger_value():
