from dataclasses import InitVar, dataclass, field

import numpy as np
from numpy.typing import ArrayLike, NDArray


@dataclass
class Inequality:
    n: InitVar[int]
    _inequality: NDArray = field(init=False)

    def __post_init__(self, n: int):
        self._inequality = np.empty((0, 2**n - 1))

    def _clear_inequality(self) -> None:
        self._inequality = np.empty((0, self._inequality.shape[1]))

    @property
    def inequality(self) -> NDArray:
        return self._inequality

    @inequality.setter
    def inequality(self, new_inequality: ArrayLike):
        self._clear_inequality()
        self._inequality = np.vstack((self.inequality, new_inequality))
