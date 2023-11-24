from src.view.two_random_variable_cli import is_all_float


def test_empty_list() -> None:

    lst = []

    assert is_all_float(lst) == []

def test_single_float() -> None:
    lst = ['0']

    assert is_all_float(lst) == [0]

def test_single_non_float_list() -> None:
    lst = ['a']

    assert is_all_float(lst) is False