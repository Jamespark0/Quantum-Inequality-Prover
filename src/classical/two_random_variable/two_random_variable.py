import numpy as np
from numpy.typing import NDArray
from scipy.optimize import linprog

# Elemental inequalities which are served as the constraints
# Assume the column index in the order of H(1), H(2), H(1, 2)
# While the row stands for H(1|2), I(1:2), H(2|1)
G: NDArray = np.array([[0, -1, 1], [1, 1, -1], [-1, 0, 1]])


# Apply duality to check if the "unconstrained" inequality is Shannon-type
# Inequality whose mathematical form is a * H(1) + b * H(2) + c * H(1, 2) >= 0
# is expressed as [a,b,c]
def prover_without_constraint(inequality: NDArray):
    primal_lower_bound: NDArray = np.zeros(3)
    result = linprog(-primal_lower_bound, A_ub=G.transpose(), b_ub=inequality)
    return result
