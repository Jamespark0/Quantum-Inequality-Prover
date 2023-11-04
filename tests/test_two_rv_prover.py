import numpy as np
from numpy.typing import NDArray

from classical import TwoRVInequalityProver


def test_h1() -> None:
    inequality = np.array([1, 0, 0])

    prover = TwoRVInequalityProver()

    assert prover.is_shannon_type(inequality=inequality)

def test_invalid_information_inequality() -> None:
    inequality = [-1, 0, 0]

    prover = TwoRVInequalityProver()
    
    assert prover.is_shannon_type(inequality=inequality) is False
    
def test_h2() -> None:
    inequality = np.array([0, 1, 0])

    prover = TwoRVInequalityProver()

    assert prover.is_shannon_type(inequality=inequality)

def test_h12() -> None:
    inequality = np.array([0, 0, 1])

    prover = TwoRVInequalityProver()

    assert prover.is_shannon_type(inequality=inequality)
    

def test_scale_basis() -> None:
    inequality = np.array([3, 0, 0])

    prover = TwoRVInequalityProver()

    assert prover.is_shannon_type(inequality=inequality)
    

def test_arbitrary_positive_axis() -> None:
    inequality = np.array([1, 1, 1])

    prover = TwoRVInequalityProver()

    assert prover.is_shannon_type(inequality=inequality)