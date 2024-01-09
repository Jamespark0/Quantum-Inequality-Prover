from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray
from scipy.optimize import OptimizeResult, linprog


@dataclass(frozen=True)
class Prover:
    elemental: NDArray

    def calculate(self, inequality: NDArray, constraints: NDArray) -> OptimizeResult:
        # Negative sign in 'c' arises from the fact that scipy.linprog calculates minimal value
        return linprog(
            c=-np.zeros(self.elemental.shape[0] + constraints.shape[0]),
            A_eq=np.vstack((self.elemental, -constraints)).transpose(),
            b_eq=inequality,
            bounds=self._bounds(
                non_negative=self.elemental.shape[0], unbounded=constraints.shape[0]
            ),
        )

    def check_type(self, result: OptimizeResult) -> bool:
        max_value: int = 0
        return (result.success) and (result.fun == max_value)

    def shortest_proof_generator(
        self, inequality: NDArray, constraints: NDArray
    ) -> tuple[NDArray, NDArray] | tuple[None, None]:
        """
        This method is called only when the given inequality is von-Neumann-type/Shannon-type

        Following from the paper, "Proving and Disproving Information Inequalities"
        """
        A_ub = np.zeros(
            (
                self.elemental.shape[0] + 2 * constraints.shape[0],
                self.elemental.shape[0] + 2 * constraints.shape[0],
            )
        )
        # Ensure -z <= mu <= z
        for row in range(
            self.elemental.shape[0], self.elemental.shape[0] + constraints.shape[0]
        ):
            A_ub[row][row] = 1
            A_ub[row][row + constraints.shape[0]] = -1
        for row in range(
            self.elemental.shape[0] + constraints.shape[0],
            self.elemental.shape[0] + 2 * constraints.shape[0],
        ):
            A_ub[row][row] = -1
            A_ub[row][row + constraints.shape[0]] = -1

        result = linprog(
            c=np.array(
                [
                    *[1] * self.elemental.shape[0],
                    *[0] * constraints.shape[0],
                    *[1] * constraints.shape[0],
                ]
            ),
            A_eq=np.vstack(
                (
                    (np.vstack((self.elemental, -constraints))),
                    np.zeros((constraints.shape[0], constraints.shape[1])),
                )
            ).transpose(),
            b_eq=inequality,
            bounds=tuple(
                [(0, None)] * len(self.elemental)
                + [(None, None)] * (2 * constraints.shape[0])
            ),
            b_ub=np.zeros(self.elemental.shape[0] + 2 * constraints.shape[0]),
            A_ub=A_ub,
        )
        return (
            (
                result.x[: self.elemental.shape[0]],
                result.x[
                    self.elemental.shape[0] : self.elemental.shape[0]
                    + constraints.shape[0]
                ],
            )
            if result.success
            else (None, None)
        )

    def _bounds(self, non_negative: int, unbounded: int) -> tuple:
        y_bounds = tuple([(0, None)] * non_negative)
        mu_bounds = tuple([(None, None)] * unbounded)

        return tuple([*y_bounds, *mu_bounds])
