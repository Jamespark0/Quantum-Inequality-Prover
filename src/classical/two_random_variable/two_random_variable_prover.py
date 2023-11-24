from dataclasses import InitVar, dataclass, field

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.optimize import OptimizeResult, linprog


@dataclass
class TwoRVInequalityProver:
    # Elemental inequalities which are served as the constraints in the primal problem
    # Assume the column index in the order of H(1), H(2), H(1, 2)
    # While the row stands for H(1|2), I(1:2), H(2|1)
    G: NDArray = field(
        init=False,
        default_factory=lambda: np.array([[0, -1, 1], [1, 1, -1], [-1, 0, 1]]),
    )
    constraints: NDArray = field(default_factory=lambda: np.empty((0, 3)), init=False)

    def is_shannon_type(self, inequality: ArrayLike) -> bool:
        primal_lower_bound: NDArray = np.zeros(3)

        inequality = np.array(inequality)
        constraints_eq = np.zeros(len(self.constraints))

        # success: bool = linprog(-primal_lower_bound, A_ub=self.G.transpose(), b_ub=inequality).success
        result: OptimizeResult = linprog(
            inequality,
            A_ub=-self.G,
            b_ub=primal_lower_bound,
            A_eq=self.constraints,
            b_eq=constraints_eq,
        )

        self._clear_constraints()

        return result.success and (result.fun == 0)

    def add_constraints(self, raw_constraints: list) -> None:
        # cnovert a list of constraints into an numpy array
        self.constraints = np.append(self.constraints, values=raw_constraints, axis=0)

    def _clear_constraints(self):
        self.constraints = np.empty((0, 3))
    
    def show_constraints(self) -> None:
        for i, constraint in enumerate(self.constraints):
            print(f"Constraint #{i}", end='\t')
            for value in constraint:
                print(value, end=" ")
            print("\n")

