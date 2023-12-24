from dataclasses import dataclass, field

import numpy as np
from numpy.typing import NDArray


@dataclass
class Canonical:
    """
    This class stores the information of the inequality to be proved, and the information
    of the constraints which the given inequality is under.

    The inequality was initially set to np.emtpy((0, dim))
    The constraints was initially set to np.empty((0, dim))

    dim: [int] = The dimension of the vector or the space we're working in.
    """

    dim: int
    _inequality: NDArray = field(
        init=False,
    )
    _constraints: NDArray = field(
        init=False,
    )

    def __post_init__(self):
        self._inequality = np.empty((0, self.dim))
        self._constraints = np.empty((0, self.dim))

    @property
    def inequality(self) -> NDArray:
        return self._inequality

    @property
    def constraints(self) -> NDArray:
        return self._constraints
