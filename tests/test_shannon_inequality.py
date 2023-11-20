import numpy as np

from classical import ShannonInequality


def test_from_no_random_variable() -> None:
    shannon = ShannonInequality(n=0)

    assert shannon.all_pairs == ()


def test_from_single_element() -> None:
    shannon = ShannonInequality(n=1)

    assert shannon.all_pairs == ({1},)


def test_from_two_element() -> None:
    shannon = ShannonInequality(n=2)

    assert shannon.all_pairs == (
        {1},
        {2},
        {1, 2},
    )


def test_from_three_element() -> None:
    shannon = ShannonInequality(n=3)

    assert shannon.all_pairs == (
        {1},
        {2},
        {3},
        {1, 2},
        {1, 3},
        {2, 3},
        {1, 2, 3},
    )


def test_from_four_element() -> None:
    shannon = ShannonInequality(n=4)

    assert len(shannon.all_pairs) == 2**4 - 1


def test_from_ten_element() -> None:
    shannon = ShannonInequality(n=10)
    assert len(shannon.all_pairs) == 2**10 - 1


def test_type1_elemental_inequalities() -> None:
    shannon = ShannonInequality(n=10)
    for i in range(10):
        conditional_entropic_vector = shannon._get_type1_elemental_entropic_vector(i=i)
        assert shannon.index_to_pair[
            conditional_entropic_vector.index(-1)
        ] == shannon.all_pairs[-1] - {i}


def test_all_type2_elemental_inequalities_with_2_random_variables() -> None:
    shannon = ShannonInequality(n=2)

    i, j = 1, 2

    assert shannon._get_type2_elemental_entropic_vector(i, j) == [[1, 1, -1]]


def test_all_types_elemental_inequalities_with_3_random_variables() -> None:
    shannon = ShannonInequality(n=3)

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
    shannon = ShannonInequality(n=2)

    intended_g = np.array([[0, -1, 1], [-1, 0, 1], [1, 1, -1]])

    assert (shannon.get_elemental_inequalities() == intended_g).all()

def test_get_all_elemental_inequalities_with_3_random_variables() -> None:
    shannon = ShannonInequality(n=3)

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