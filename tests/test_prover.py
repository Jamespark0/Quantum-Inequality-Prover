import numpy as np
from numpy.typing import NDArray

from src.controller import Prover
from src.model import EntropicSpace, QuantumInequality, ShannonInequality

"""
The prover can also be applied in the classical regime by replacing 
QuantumInequality(space).ELEMENtAL with ShannonInequality(space).ELEMMENTAL
"""


def test_quantum_strong_subadditivity() -> None:
    space = EntropicSpace(n=3)
    prover = Prover(elemental=QuantumInequality(space=space).ELEMENTAL)
    inequality: NDArray[np.float64] = np.zeros(len(space.all_pairs))
    inequality[space.to_index[frozenset({1, 2, 3})]] = -1
    inequality[space.to_index[frozenset({3})]] = -1
    inequality[space.to_index[frozenset({1, 3})]] = 1
    inequality[space.to_index[frozenset({2, 3})]] = 1

    assert prover.check_type(
        result=prover.calculate(
            inequality=inequality, constraints=np.empty((0, len(space.all_pairs)))
        )
    )


def test_quantum_weak_monotonacity() -> None:
    space = EntropicSpace(n=3)
    prover = Prover(elemental=QuantumInequality(space=space).ELEMENTAL)
    inequality = np.zeros(len(space.all_pairs))

    inequality[space.to_index[frozenset({1})]] = -1
    inequality[space.to_index[frozenset({2})]] = -1
    inequality[space.to_index[frozenset({1, 3})]] = 1
    inequality[space.to_index[frozenset({2, 3})]] = 1

    assert prover.check_type(
        result=prover.calculate(
            inequality=inequality, constraints=np.empty((0, len(space.all_pairs)))
        )
    )


def test_conditional_von_neumann_entropy() -> None:
    space = EntropicSpace(n=2)
    prover = Prover(elemental=QuantumInequality(space=space).ELEMENTAL)
    inequality = np.zeros(len(space.all_pairs))

    inequality[space.to_index[frozenset({1, 2})]] = 1
    inequality[space.to_index[frozenset({2})]] = -1

    assert (
        prover.check_type(
            result=prover.calculate(
                inequality=inequality, constraints=np.empty((0, len(space.all_pairs)))
            )
        )
        is False
    )


def test_constrained_non_von_neumann_type() -> None:
    space = EntropicSpace(n=4)
    prover = Prover(elemental=QuantumInequality(space=space).ELEMENTAL)

    constraints = np.zeros((3, len(space.all_pairs)))
    # I(C;A|B) = 0
    constraints[0][space.to_index[frozenset({2, 3})]] = 1
    constraints[0][space.to_index[frozenset({1, 2})]] = 1
    constraints[0][space.to_index[frozenset({1, 2, 3})]] = -1
    constraints[0][space.to_index[frozenset({2})]] = -1
    # I(B;C|A) = 0
    constraints[1][space.to_index[frozenset({1, 2})]] = 1
    constraints[1][space.to_index[frozenset({1, 3})]] = 1
    constraints[1][space.to_index[frozenset({1, 2, 3})]] = -1
    constraints[1][space.to_index[frozenset({1})]] = -1
    # I(A;B|D) = 0
    constraints[2][space.to_index[frozenset({1, 4})]] = 1
    constraints[2][space.to_index[frozenset({2, 4})]] = 1
    constraints[2][space.to_index[frozenset({1, 2, 4})]] = -1
    constraints[2][space.to_index[frozenset({4})]] = -1

    inequality = np.zeros(len(space.to_index))
    # I(C;D) >= I(C;AB)
    # equivalently, (S_{c} + S_{d} - S_{c,d}) - (S_{c} + S_{ab} - S_{abc}) >= 0
    inequality[space.to_index[frozenset({4})]] = 1
    inequality[space.to_index[frozenset({3, 4})]] = -1
    inequality[space.to_index[frozenset({1, 2})]] = -1
    inequality[space.to_index[frozenset({1, 2, 3})]] = 1

    assert (
        prover.check_type(
            result=prover.calculate(inequality=inequality, constraints=constraints)
        )
        is False
    )
