from dataclasses import InitVar, dataclass, field

import numpy as np
from numpy.typing import ArrayLike, NDArray


@dataclass
class ConstraintHandler:
    random_variables: InitVar[int]
    _constraints: NDArray = field(init=False)

    def __post_init__(self, random_variables: int):
        self._constraints = np.empty((0, 2**random_variables - 1))

    @property
    def constraints(self):
        return self._constraints

    def add_constraints(self, new_constraints: ArrayLike):
        self._constraints = np.vstack((self._constraints, new_constraints))

    def add_constraints_v2(self, *new_constraints) -> None:
        new_constraints = np.array(new_constraints)
        self._constraints = np.vstack((self._constraints, new_constraints))

    def clear_constraint(self):
        self._constraints = np.empty((0, self._constraints.shape[1]))
