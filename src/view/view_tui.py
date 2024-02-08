# Terminal User Interface View
import logging
from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from src.util import to_joint_entropy, turn_str_to_pair
from src.util.convertor import InvalidPairError, vec_to_entropy_expression
from src.view.view import BaseInput, BaseMessage

logging.basicConfig(level=logging.INFO)

ASSIGNMENT_SYMBOL = "->"


@dataclass(frozen=True)
class TerminalMessage(BaseMessage):
    """
    This class is only used to display the constraints and inequality stored in the model.
    """

    index_order: tuple

    def _show_expressions(self, expressions: NDArray, ending: str) -> tuple[str, ...]:
        messages = [
            # f'{" + ".join(f"{coefficient} * {to_joint_entropy(self.index_order[i])}" for i, coefficient in enumerate(expression))}'
            vec_to_entropy_expression(vec=expression, index_order=self.index_order)
            + ending
            for expression in expressions
        ]

        return tuple(messages)

    def show_inequality(self, inequalities: NDArray) -> tuple[str, ...]:
        ending = " >= 0" + "\n"

        return self._show_expressions(expressions=inequalities, ending=ending)

    def show_constraints(self, constraints: NDArray) -> tuple[str, ...]:
        ending = " = 0" + "\n"
        return self._show_expressions(expressions=constraints, ending=ending)

    def _get_rules(self, ending: str) -> tuple[str, ...]:
        rules = []
        rules.append("An information inequality is expressed as the following:")
        rules.append(
            f'{" + ".join(f"a({i}) * {to_joint_entropy(pair=x)}" for i, x in enumerate(self.index_order, start=1))}'
            + ending
        )
        return tuple(rules)

    def get_constraints_rules(self) -> tuple[str, ...]:
        return self._get_rules(ending=" >= 0")

    def get_inequality_rules(self) -> tuple[str, ...]:
        return self._get_rules(ending=" = 0")

    def get_input_message(self) -> str:
        return (
            f"The input should contain {len(self.index_order)} numbers, and in the order of: "
            + f'{", ".join(f"a({i})" for i in range(1, len(self.index_order) + 1))}'
        )

    def get_single_expression_msg(self) -> str:
        return (
            "Input the coefficients as the following:\n"
            + f"{repr('pair[separated by space] -> coefficients')}."
            + f"Different coefficients are separated by {repr(';')}"
        )


@dataclass(frozen=True)
class TerminalInput(BaseInput):
    """
    This class is responsible for getting inequalities and constraints from users, and return
    numpy.array respectively.

    """

    def _get_index_coefficient(self, string: str) -> tuple[frozenset, float]:
        """
        Turn a string to a tuple of frozentset which holds the info of the current pair and the
        corresponding coefficient value.

        Args:
            string (str): string to be converted into (pair, coefficient)

        Raises:
            SyntaxError: If more than one "->" occurs
        """
        split_symbol = ASSIGNMENT_SYMBOL

        pair, coefficient, *_ = string.split(split_symbol)

        if len(_) != 0:
            raise SyntaxError(
                f"Coefficient assignement involves only one {repr(split_symbol)}"
            )

        return (turn_str_to_pair(string=pair), float(coefficient))

    def get_inequality(self) -> NDArray[np.float64]:
        while True:
            new_inequality = input("# ")
            try:
                return np.array([float(value) for value in new_inequality.split()])
            except ValueError as e:
                print(e)
            except Exception as e:
                logging.warning(f"Unexpected: {e}")

    def get_constraints(self) -> NDArray[np.float64]:
        while True:
            new_constraints = input("# ")
            try:
                return np.array(
                    list(
                        map(
                            lambda x: [float(value) for value in x.split()],
                            filter(None, new_constraints.split(",")),
                        )
                    )
                )
            except ValueError as e:
                print(e)

            except Exception as e:
                logging.warning(f"Unexpected: {e}")

    def get_single_expression(
        self, dim: int, mapping: dict[frozenset, int]
    ) -> NDArray[np.float64]:
        expression = np.zeros(dim)
        while True:
            indices_coefficients = input("# ").split(";")
            try:
                for index_constraint in indices_coefficients:
                    pair, coefficient = self._get_index_coefficient(
                        string=index_constraint
                    )
                    expression[mapping.get(pair, len(mapping))] = coefficient

                return expression
            except InvalidPairError as e:
                print(e)

            except ValueError as e:
                print(e)

            except Exception as e:
                print(f"Unexpected error: {e}")
