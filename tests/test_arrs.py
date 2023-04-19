import pytest

from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2

def test_get_zero():
    assert arrs.get([1, 3], -5, 'zero') == 'zero'


def test_get_none_list():
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 2) == []
    assert arrs.my_slice([1, 2], -4) == [1, 2]
    assert arrs.my_slice([1, 2], -1) == [2]
