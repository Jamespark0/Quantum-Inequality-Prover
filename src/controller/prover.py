from dataclasses import dataclass
from typing import Literal

import numpy as np
from numpy.typing import NDArray
from scipy.optimize import OptimizeResult, linprog


@dataclass(frozen=True)
class Prover:
    elemental: NDArray

    def calculate(self, inequality: NDArray, constraints: NDArray) -> OptimizeResult:
        return linprog(
            c=-np.zeros(self.elemental.shape[0] + constraints.shape[0]),
            A_eq=np.vstack((self.elemental, -constraints)).transpose(),
            b_eq=inequality,
            bounds=self._bounds(
                non_negative=self.elemental.shape[0], bounded=constraints.shape[0]
            ),
        )

    def check_type(self, result: OptimizeResult) -> bool:
        max_value: int = 0
        return (result.success) and (result.fun == max_value)

    def _get_unbounded_bound(self) -> tuple[None, None]:
        return (None, None)

    def _get_non_negative_bound(self) -> tuple[Literal[0], None]:
        return (0, None)

    def _bounds(self, non_negative: int, bounded: int) -> tuple:
        y_bounds = tuple([self._get_non_negative_bound() for _ in range(non_negative)])
        mu_bounds = tuple([self._get_unbounded_bound() for _ in range(bounded)])

        return tuple([*y_bounds, *mu_bounds])
