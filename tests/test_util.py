import pytest

from src.util import turn_str_to_pair
from src.util.convertor import InvalidPairError


def test_single_pair() -> None:
    assert turn_str_to_pair(string="1") == frozenset({1})


def test_empty_string() -> None:
    with pytest.raises(InvalidPairError):
        turn_str_to_pair(string="")


def test_parse_empty_string() -> None:
    with pytest.raises(InvalidPairError):
        turn_str_to_pair(string="   ")


def test_marginal_pair() -> None:
    assert turn_str_to_pair(string="1 2 3") == frozenset({1, 2, 3})


def test_parse_marginal_pair() -> None:
    assert turn_str_to_pair(string="1   2 3") == frozenset({1, 2, 3})
