from pytest import MonkeyPatch

from src.view import TwoRandomVariableCLI as cli


def test_empty_input(monkeypatch: MonkeyPatch) -> None:
    intended_input = ""

    monkeypatch.setattr("builtins.input", lambda _: intended_input)

    result = cli().get_constraints()

    assert result is False


def test_single_valid_input(monkeypatch: MonkeyPatch) -> None:
    intended_input = "0 -1 3.14"

    monkeypatch.setattr("builtins.input", lambda _: intended_input)

    result = cli().get_constraints()

    assert result == [[0, -1, 3.14]]


def test_single_invalid_input(monkeypatch: MonkeyPatch) -> None:
    intended_input = "a 0 3.14"

    monkeypatch.setattr("builtins.input", lambda _: intended_input)

    result = cli().get_constraints()

    assert result is False


def test_single_invalid_input_with_incorrect_length(monkeypatch: MonkeyPatch) -> None:
    intended_input = "1 1 1 1"

    monkeypatch.setattr("builtins.input", lambda _: intended_input)

    result = cli().get_constraints()

    assert result is False


def test_multiple_valid_inputs(monkeypatch: MonkeyPatch) -> None:
    intended_input = "1 0 0, 0 -1 0"

    monkeypatch.setattr("builtins.input", lambda _: intended_input)

    result = cli().get_constraints()

    assert result == [[1, 0, 0], [0, -1, 0]]


def test_multiple_invalid_inputs(monkeypatch: MonkeyPatch) -> None:
    intended_input = " a b c, -1 0 helloworld 0"

    monkeypatch.setattr("builtins.input", lambda _: intended_input)

    result = cli().get_constraints()

    assert result is False


def test_mixed_inputs(monkeypatch: MonkeyPatch) -> None:
    intended_input = "-1 0 0,  1 0 0, 3.14 a hello"

    monkeypatch.setattr("builtins.input", lambda _: intended_input)

    result = cli().get_constraints()

    assert result is False
