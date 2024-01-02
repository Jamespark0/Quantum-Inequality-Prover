import numpy as np
from pytest import MonkeyPatch

from src.view import TerminalInput


def test_valid_inequality(monkeypatch: MonkeyPatch) -> None:
    inequalities = "-1 1 3.14"
    monkeypatch.setattr("builtins.input", lambda _: inequalities)

    user_input = TerminalInput().get_inequality()
    assert (user_input == np.array([float(num) for num in inequalities.split()])).all()


def test_one_non_numeric_inequality_input(monkeypatch: MonkeyPatch) -> None:
    valid_input = "1 0 0"

    all_inputs: list[str] = ["a b c d", valid_input]

    monkeypatch.setattr("builtins.input", lambda _: all_inputs.pop(0))

    user_input = TerminalInput().get_inequality()
    assert (
        user_input == np.array([float(value) for value in valid_input.split()])
    ).all()


def test_two_invalid_and_final_valid_inequality(monkeypatch: MonkeyPatch) -> None:
    valid_input = "1 0 0"

    all_inputs = ["a b c d", "1 3.14 hello", valid_input]

    monkeypatch.setattr("builtins.input", lambda _: all_inputs.pop(0))

    user_input = TerminalInput().get_inequality()

    assert (
        user_input == np.array([float(value) for value in valid_input.split()])
    ).all()


def test_empty_constraint(monkeypatch: MonkeyPatch) -> None:
    intended_input = ""
    monkeypatch.setattr("builtins.input", lambda _: intended_input)

    result = TerminalInput().get_constraints()

    assert (result == np.array([[]])).all()


def test_single_constraint(monkeypatch: MonkeyPatch) -> None:
    intended_input = "0 -1 3.14"

    monkeypatch.setattr("builtins.input", lambda _: intended_input)

    result = TerminalInput().get_constraints()

    assert (
        result == np.array([[float(value) for value in intended_input.split()]])
    ).all()


def test_multiple_valid_constraints(monkeypatch) -> None:
    intended_input = "1 0 3.14, 2 -3.2 -5"

    monkeypatch.setattr("builtins.input", lambda _: intended_input)

    result = TerminalInput().get_constraints()

    assert (
        result
        == np.array(
            [
                [float(value) for value in constraint.split()]
                for constraint in intended_input.split(",")
            ]
        )
    ).all()


def test_single_invalid_input_and_one_valid_input(monkeypatch) -> None:
    intended_input = ["a b c d", "1 0 0"]

    monkeypatch.setattr("builtins.input", lambda _: intended_input.pop())

    result = TerminalInput().get_constraints()

    assert (result == np.array([[1, 0, 0]])).all()


def test_multiple_invalid_input_and_single_valid_constraint(
    monkeypatch: MonkeyPatch,
) -> None:
    intended = ["a b c d", "e e e", "1 0"]

    monkeypatch.setattr("builtins.input", lambda _: intended.pop())

    result = TerminalInput().get_constraints()

    assert (result == np.array([[1, 0]])).all()


def test_all_numeric_but_different_dim(monkeypatch: MonkeyPatch) -> None:
    valid_input = "1 0 3.14, 2 -3.2 -5"
    intended = ["1 2 3, 4 5", valid_input]

    monkeypatch.setattr("builtins.input", lambda _: intended.pop())

    result = TerminalInput().get_constraints()

    assert (
        result
        == np.array(
            [
                [float(value) for value in constraint.split()]
                for constraint in valid_input.split(",")
            ]
        )
    ).all()
