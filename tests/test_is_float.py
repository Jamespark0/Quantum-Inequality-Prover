"""
    Test whether the function is_float can correctly identify elements that can be 
    converted to float / int.
    """
from src.two_random_variable_cli import is_float


def test_value_is_int() -> None:
    value: str = '3'

    # assert is_float(value) is True
    assert is_float(value)

def test_value_is_float() -> None:
    value: str = "3.14"

    assert is_float(value=value)

def test_value_is_negative_int() -> None:
    value: str = "-5"

    assert is_float(value=value)

def test_value_is_negative_float() -> None:
    value: str = "-5.28"

    assert is_float(value)


def test_value_is_letters() -> None:
    value: str = "Hello world"

    assert not is_float(value)