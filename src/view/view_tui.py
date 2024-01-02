# Terminal User Interface View
import logging
from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from src.util import to_joint_entropy
from src.view.view import BaseInput, BaseMessage

logging.basicConfig(level=logging.INFO)


@dataclass(frozen=True)
class TerminalMessage(BaseMessage):
    """
    This class is only used to display the constraints and inequality stored in the model.
    """

    index_order: tuple

    def _show_expressions(self, expressions: NDArray, ending: str) -> tuple[str, ...]:
        messages = [
            f'{" + ".join(f"{coefficient} * {to_joint_entropy(self.index_order[i])}" for i, coefficient in enumerate(expression))}'
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


@dataclass(frozen=True)
class TerminalInput(BaseInput):
    """
    This class is responsible for getting inequalities and constraints from users, and return
    numpy.array respectively.

    """

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
