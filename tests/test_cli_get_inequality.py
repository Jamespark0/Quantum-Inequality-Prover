from pytest import MonkeyPatch

from src.view import TwoRandomVariableCLI


def test_valid_input(monkeypatch: MonkeyPatch) -> None:
    inequalities = "-1 1 3.14"
    monkeypatch.setattr("builtins.input", lambda _: inequalities)

    user_input = TwoRandomVariableCLI().get_inequality()
    assert user_input == [float(num) for num in inequalities.split()]

def test_first_wrong_entries_input(monkeypatch: MonkeyPatch) -> None:
    valid_input = "1 0 0"
    
    all_inputs: list[str] = ["a b c d", valid_input]

    monkeypatch.setattr("builtins.input", lambda _: all_inputs.pop(0))
    
    user_input: list[float] = TwoRandomVariableCLI().get_inequality()
    assert user_input == [float(value) for value in valid_input.split()]


def test_first_string_with_non_numerical_value(monkeypatch: MonkeyPatch) -> None:
    valid_input = "1 0 0"

    all_inputs = ["1 0 a", valid_input]

    monkeypatch.setattr("builtins.input", lambda _: all_inputs.pop(0))

    user_input = TwoRandomVariableCLI().get_inequality()
    assert user_input == [float(value) for value in valid_input.split()]

def test_two_invalid_and_final_valid(monkeypatch: MonkeyPatch) -> None:
    valid_input = "1 0 0"

    all_inputs = ["a b c d", "1 3.14 hello", valid_input]

    monkeypatch.setattr("builtins.input", lambda _: all_inputs.pop(0))

    user_input = TwoRandomVariableCLI().get_inequality()

    assert user_input == [float(value) for value in valid_input.split()]
