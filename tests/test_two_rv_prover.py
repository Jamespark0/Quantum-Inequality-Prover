import numpy as np
from numpy.typing import NDArray

from src.classical.two_random_variable import TwoRVInequalityProver


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

def test_non_shannon_type() -> None:
    inequality = np.array([1, -1, 0])

    prover = TwoRVInequalityProver()

    assert not prover.is_shannon_type(inequality=inequality)
    
def test_add_single_constraint_to_empty_constraint() -> None:
    new_constraint = [[1, 1, 0]]

    prover = TwoRVInequalityProver()

    prover.add_constraints(new_constraint)

    assert np.all(prover.constraints == np.array(new_constraint))
    

def test_add_single_constraint_to_non_empty_constraint() -> None:
    init_constraint = [[0, 1, 0]]

    new_constraint: list = [[1, 0, 1]]

    prover = TwoRVInequalityProver()

    prover.add_constraints(init_constraint)
    prover.add_constraints(new_constraint)

    init_constraint.extend(new_constraint)

    assert np.all(prover.constraints == np.array(init_constraint))
    
def test_add_multi_constraints_to_empty_constraint() -> None:
    new_constraint = [[0, 1, 0], [1, 0, 1]]

    prover = TwoRVInequalityProver()
    prover.add_constraints(new_constraint)

    assert np.all(prover.constraints == np.array(new_constraint))

def test_add_multi_constraints_to_non_empty_constraint() -> None:
    init_constraint = [[0, 0, 0]]

    new_constraint = [[0, 1, 0], [1, 0, 1]]

    prover = TwoRVInequalityProver()
    prover.add_constraints(init_constraint)

    prover.add_constraints(new_constraint)

    init_constraint.extend(new_constraint)
    assert np.all(prover.constraints == np.array(init_constraint))

def test_clear_empty_constraitns() -> None:
    prover = TwoRVInequalityProver()

    prover._clear_constraints()

    assert np.all(prover.constraints == np.empty((0, 3)))


def test_clear_non_empty_constraint() -> None:
    prover = TwoRVInequalityProver()

    init_constraint = [[0, 0, 0]]

    prover.add_constraints(init_constraint)

    prover._clear_constraints()

    assert np.all(prover.constraints == np.empty((0,3)))