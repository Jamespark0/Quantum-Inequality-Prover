from typing import Sequence

import numpy as np
from numpy.typing import NDArray
from scipy.optimize import OptimizeResult, linprog


class ClassicalProver:
    def is_shannon_type(
        self,
        inequality: Sequence | NDArray,
        elemental_inequality: NDArray,
        constraints: NDArray,
    ) -> bool:
        A_eq = np.vstack((elemental_inequality, -constraints)).transpose()
        c = np.zeros(elemental_inequality.shape[0] + constraints.shape[0])
        result: OptimizeResult = linprog(
            c=-c,
            A_eq=A_eq,
            b_eq=inequality,
            bounds=self._bounds(
                non_negative=elemental_inequality.shape[0], bounded=constraints.shape[0]
            ),
        )
        return (result.success) and (result.fun == 0)

    def _get_unbounded_bound(self):
        return (None, None)

    def _get_non_negative_bound(self):
        return (0, None)

    def _bounds(self, non_negative: int, bounded: int) -> tuple:
        y_bounds = tuple([self._get_non_negative_bound() for _ in range(non_negative)])
        mu_bounds = tuple([self._get_unbounded_bound() for _ in range(bounded)])

        return tuple([*y_bounds, *mu_bounds])
