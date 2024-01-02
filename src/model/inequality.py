from dataclasses import dataclass, field

import numpy as np
from numpy.typing import NDArray


@dataclass
class Inequality:
    """
    This class stores the information of the inequality to be proved, and the information
    of the constraints which the given inequality is under.

    The expression was initially set to np.emtpy((0, dim))
    The constraints was initially set to np.empty((0, dim))

    dim: [int] = The dimension of the vector or the space we're working in.
    """

    dim: int
    _expression: NDArray = field(
        init=False,
    )
    _constraints: NDArray = field(
        init=False,
    )

    def __post_init__(self):
        self._expression = np.empty((0, self.dim))
        self._constraints = np.empty((0, self.dim))

    @property
    def expression(self) -> NDArray:
        return self._expression

    @property
    def constraints(self) -> NDArray:
        return self._constraints
