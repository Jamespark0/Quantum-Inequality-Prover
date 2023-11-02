import sys

import numpy as np
from numpy.typing import NDArray

sys.path.insert(0, "../")

from classical import two_random_variable as trv


def test_shannon_entropy() -> None:
    inequality = np.array([1, 0, 0])
    optimal_value: float = trv.prover_without_constraint(inequality).fun
    assert optimal_value == 0
