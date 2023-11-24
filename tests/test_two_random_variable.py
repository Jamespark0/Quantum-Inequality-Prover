import numpy as np
from numpy.typing import NDArray

from src.classical.two_random_variable import prover_without_constraint


def test_shannon_entropy() -> None:
    inequality = np.array([1, 0, 0])
    optimal_value: float = prover_without_constraint(inequality).fun
    assert optimal_value == 0
