from dataclasses import dataclass

import numpy as np

from src.controller.controller import BaseController
from src.model import Inequality
from src.view import TerminalInput, TerminalMessage


class DimensionMismatchError(ValueError):
    """Custom Error for wrong dimensional size error"""

    def __init__(self, expected_dim: int, input_dim: int, message: str) -> None:
        self.expected_dim = expected_dim
        self.input_dim = input_dim
        super().__init__(message)


@dataclass(frozen=True)
class InequalityController(BaseController):
    model: Inequality
    messageView: TerminalMessage
    inputView: TerminalInput

    def add_inequality(self) -> None:
        """
        By inputing a new inequality, the new inequality replaces the old one.
        """
        for rule in self.messageView.get_inequality_rules():
            print(rule)
        print()
        print(self.messageView.get_input_message())
        while True:
            try:
                new_inequality = self.inputView.get_inequality()
                if self._single_expression_validator(new_inequality):
                    self.model._expression = np.vstack(
                        (np.empty((0, self.model.dim)), new_inequality)
                    )
                    break
            except DimensionMismatchError as e:
                print(e)

    def add_inequality_v2(self, mapping: dict[frozenset, int]) -> None:
        "Replace the old inequality with the new one. This is done by getting the desired coefficients"
        for rule in self.messageView.get_inequality_rules():
            print(rule)
        print()
        print(self.messageView.get_single_expression_msg())
        new_inequality = self.inputView.get_single_expression(
            dim=self.model.dim, mapping=mapping
        )
        self.model._expression = np.vstack(
            (np.empty((0, self.model.dim)), new_inequality)
        )

    def add_constraints(self) -> None:
        """
        Add new constraints, while keeping the old constraints intact at the same time
        """
        for rule in self.messageView.get_constraints_rules():
            print(rule)
        print()
        print(self.messageView.get_input_message())

        while True:
            try:
                new_constraints = self.inputView.get_constraints()
                if all(
                    [
                        self._single_expression_validator(constraint)
                        for constraint in new_constraints
                    ]
                ):
                    self.model._constraints = np.unique(
                        np.vstack((self.model.constraints, new_constraints)), axis=0
                    )
                    break
            except DimensionMismatchError as e:
                print(e)

    def add_single_constraint(self, mapping: dict[frozenset, int]) -> None:
        for rule in self.messageView.get_constraints_rules():
            print(rule)
        print()
        print(self.messageView.get_single_expression_msg())

        new_constraint = self.inputView.get_single_expression(
            dim=self.model.dim, mapping=mapping
        )

        self.model._constraints = np.unique(
            np.vstack((self.model.constraints, new_constraint)), axis=0
        )

    def show_inequality(self) -> None:
        print("-" * 50)
        print("Current inequality:")
        for inequality in self.messageView.show_inequality(
            inequalities=self.model.expression
        ):
            print(inequality)
            print()

        print("-" * 50)

    def show_constraints(self) -> None:
        print("-" * 50)
        print("Current constraints:")
        for i, constraint in enumerate(
            self.messageView.show_constraints(constraints=self.model.constraints),
            start=1,
        ):
            print(f"{i}. {constraint}")
            print()

        print("-" * 50)

    def _single_expression_validator(self, expression: np.ndarray) -> bool:
        if expression.shape[0] != self.model.dim:
            raise DimensionMismatchError(
                expected_dim=self.model.dim,
                input_dim=expression.shape[0],
                message=f"The dimension of the space is {self.model.dim}!",
            )
        else:
            return True

    def clear_constraints(self) -> None:
        self.model._constraints = np.empty((0, self.model.dim))

    # The following two properties are used for passing to the Inequality Prover
    @property
    def inequality(self):
        return self.model.expression

    @property
    def constraints(self):
        return self.model.constraints
