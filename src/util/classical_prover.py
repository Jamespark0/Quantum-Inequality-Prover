from typing import Sequence

from numpy.typing import NDArray
from scipy.optimize import linprog


class ClassicalProver:
    def is_shannon_type(
        self, inequality: Sequence, elemental_inequality: NDArray, constraints: NDArray
    ):
        pass

    def _get_unbounded_bound(self):
        return (None, None)

    def _get_non_negative_bound(self):
        return (0, None)

    def _bounds(self, non_negative: int, bounded: int) -> tuple:
        y_bounds = tuple([self._get_non_negative_bound() for _ in range(non_negative)])
        mu_bounds = tuple([self._get_unbounded_bound() for _ in range(bounded)])

        return tuple([*y_bounds, *mu_bounds])


if __name__ == "__main__":
    prover = ClassicalProver()
    print(prover._bounds(non_negative=3, bounded=2))
