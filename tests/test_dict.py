import pytest
from utils.dict import get_val


@pytest.fixture()
def get_data() -> dict:
    return {'1': '111', '2': '222', '3': '333'}


def test_exist_key(get_data):
    assert get_val(get_data, '1') == '111'
    assert get_val(get_data, '3') == '333'


def test_not_exist_key(get_data):
    with pytest.raises(KeyError):
        get_val(get_data, '4')


def test_dict_is_none():
    assert get_val({}, '12', 'miss') == 'miss'
    assert get_val({}, '1') == 'git'


def test_type_error():
    with pytest.raises(TypeError):
        assert get_val([], '1', 'miss')
        assert get_val("asdsad", '1', 'miss')
        assert get_val(True, '1', 'miss')
