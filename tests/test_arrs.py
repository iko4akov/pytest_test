import pytest

from utils import arrs

@pytest.fixture
def get_list():
    return [1, 2, 3]


def test_get(get_list):
    assert arrs.get(get_list, 1, "test") == 2

def test_get_zero(get_list):
    assert arrs.get(get_list, -5, 'zero') == 'zero'


def test_get_none_list():
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")


def test_slice(get_list):
    assert arrs.my_slice(get_list, 1, 3) == [2, 3]
    assert arrs.my_slice(get_list, 1) == [2, 3]
    assert arrs.my_slice([], 2) == []
    assert arrs.my_slice([1, 2], -4) == [1, 2]
    assert arrs.my_slice([1, 2], -1) == [2]
