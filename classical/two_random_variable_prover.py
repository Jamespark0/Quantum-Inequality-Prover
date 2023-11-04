from dataclasses import InitVar, dataclass, field

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.optimize import linprog


@dataclass
class TwoRVInequalityProver:
    # Elemental inequalities which are served as the constraints in the primal problem
    # Assume the column index in the order of H(1), H(2), H(1, 2)
    # While the row stands for H(1|2), I(1:2), H(2|1)
    G: NDArray = field(init=False, default_factory= lambda: np.array([[0, -1, 1], [1, 1, -1], [-1, 0, 1]]))
    constraints: list = field(default_factory=list)
    

    def is_shannon_type(self, inequality: ArrayLike) -> bool:
        primal_lower_bound: NDArray = np.zeros(3) 
        inequality = np.array(inequality)

        success: bool = linprog(-primal_lower_bound, A_ub=self.G.transpose(), b_ub=inequality).success

        return success
    


         

