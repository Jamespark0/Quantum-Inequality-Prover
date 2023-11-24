import numpy as np

from src.classical import ShannonInequality
from src.shared.entropic_space import EntropicSpace


def test_type1_elemental_inequalities() -> None:
    entropic_space = EntropicSpace(n=10)
    shannon = ShannonInequality(entropic_space)

    for i in range(10):
        conditional_entropic_vector = shannon._get_type1_elemental_entropic_vector(i=i)
        assert shannon.index_to_pair[
            conditional_entropic_vector.index(-1)
        ] == shannon.entropic_space.universal - {i}


def test_all_type2_elemental_inequalities_with_2_random_variables() -> None:
    entropic_space = EntropicSpace(n=2)
    shannon = ShannonInequality(entropic_space)

    i, j = 1, 2

    assert shannon._get_type2_elemental_entropic_vector(i, j) == [[1, 1, -1]]


def test_all_types_elemental_inequalities_with_3_random_variables() -> None:
    entropic_space = EntropicSpace(n=3)
    shannon = ShannonInequality(entropic_space)


    i, j = 1, 2
    assert shannon._get_type2_elemental_entropic_vector(i, j) == [
        [1, 1, 0, -1, 0, 0, 0],
        [0, 0, -1, 0, 1, 1, -1],
    ]
    
    i, j = 1, 3
    assert shannon._get_type2_elemental_entropic_vector(i,j) == [
        [1, 0, 1, 0, -1, 0, 0],
        [0, -1, 0, 1, 0, 1, -1],
    ]
    
    i, j = 2, 3
    assert shannon._get_type2_elemental_entropic_vector(i,j) == [
        [0, 1, 1, 0, 0, -1, 0],
        [-1, 0, 0, 1, 1, 0, -1],
    ]

def test_get_all_elemental_inequalities_with_2_random_variables() -> None:
    entropic_space = EntropicSpace(n=2)
    shannon = ShannonInequality(entropic_space)


    intended_g = np.array([[0, -1, 1], [-1, 0, 1], [1, 1, -1]])

    assert (shannon.get_elemental_inequalities() == intended_g).all()

def test_get_all_elemental_inequalities_with_3_random_variables() -> None:
    entropic_space = EntropicSpace(n=3)
    shannon = ShannonInequality(entropic_space)

    intended_g = np.array([
        [0, 0, 0, 0, 0, -1, 1],
        [0, 0, 0, 0, -1, 0, 1],
        [0, 0, 0, -1, 0, 0, 1],
        [1, 1, 0, -1, 0, 0, 0],
        [0, 0, -1, 0, 1, 1, -1],
        [1, 0, 1, 0, -1, 0, 0],
        [0, -1, 0, 1, 0, 1, -1],
        [0, 1, 1, 0, 0, -1, 0],
        [-1, 0, 0, 1, 1, 0, -1],
    ])

    assert (shannon.get_elemental_inequalities() == intended_g).all()

def test_get_all_inequalities_with_6_random_variables() -> None:
    entropic_space = EntropicSpace(n=6)
    shannon = ShannonInequality(entropic_space)

    # As it is hard to generate the intended g by hand, so I just check the shape
    assert shannon.get_elemental_inequalities().shape == (6 + 15 * (2**4), 2**6 - 1)