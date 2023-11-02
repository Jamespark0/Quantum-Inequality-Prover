import sys

import numpy as np
from numpy.typing import NDArray

sys.path.insert(0, "../")

from classical.two_random_variable_prover import TwoRVInequalityProver


def test_shannon_type_prover() -> None:
    inequality = np.array([1, 0, 0])

    prover = TwoRVInequalityProver()

    assert prover.is_shannon_type(inequality=inequality)

def test_invalid_information_inequality() -> None:
    inequality = [-1, 0, 0]

    prover = TwoRVInequalityProver()
    
    assert prover.is_shannon_type(inequality=inequality) is False