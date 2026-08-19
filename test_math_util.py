import pytest

from math_util import average


def test_average_of_positive_numbers():
    assert average([1, 2, 3, 4, 5]) == 3


def test_average_of_single_number():
    assert average([10]) == 10


def test_average_with_negative_numbers():
    assert average([-1, 0, 1]) == 0


def test_average_with_floats():
    assert average([1.5, 2.5]) == 2.0


def test_average_with_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        average([])


def test_average_with_none_raises_value_error():
    with pytest.raises(ValueError):
        average(None)
