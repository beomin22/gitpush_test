import pytest

from list_util import find_max


def test_find_max_of_positive_numbers():
    assert find_max([1, 5, 3]) == 5


def test_find_max_with_negative_numbers():
    assert find_max([-5, -1, -3]) == -1


def test_find_max_with_single_element():
    assert find_max([7]) == 7


def test_find_max_with_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        find_max([])


def test_find_max_with_none_raises_value_error():
    with pytest.raises(ValueError):
        find_max(None)
