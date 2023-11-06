from src.two_random_variable_cli import is_valid_input


def test_empty_string() -> None:
    string = "".split()

    assert is_valid_input(string) is False

def test_one_num_string() -> None:
    string = "1".split()

    assert is_valid_input(string) is False

def test_valid_input() -> None:
    string = "-1 3.14 2".split()

    assert is_valid_input(string)

def test_contain_only_one_non_numerical() -> None:
    string = "a".split()

    assert not is_valid_input(string)

def test_contain_multi_non_numerical() -> None:
    string = "a abc".split()
     
    assert not is_valid_input(string)

def test_mixed_type() -> None:
    string = "abc 1 3.14".split()

    assert not is_valid_input(string)
    
def test_with_zero():
    stirng = "1 0 0".split()

    assert is_valid_input(stirng) == [1, 0, 0]