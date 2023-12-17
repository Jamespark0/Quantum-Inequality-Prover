import numpy as np

from src.model import Constraints


def test_initialize() -> None:
    n = 3

    constraints_mach = Constraints(n=3)

    assert constraints_mach._expressions.size == 0
    assert constraints_mach._expressions.shape == (0, 2**n - 1)


def test_add_single_list_constraints_to_empty_constraint() -> None:
    n = 3

    constraints_mach = Constraints(n=n)
    og_shape = constraints_mach._expressions.shape

    constraint = [0 for _ in range(2**n - 1)]
    constraints_mach.add_expressions(constraint)

    assert (
        constraints_mach._expressions == np.array(constraint).reshape((-1, 2**n - 1))
    ).all()
    assert constraints_mach._expressions.shape == (og_shape[0] + 1, og_shape[1])


def test_add_1d_array_constraint_to_empty_constraint() -> None:
    n = 3

    constraint_mach = Constraints(n=n)
    og_shape = constraint_mach._expressions.shape

    new_constraint = np.array([_ for _ in range(2**n - 1)])
    constraint_mach.add_expressions(new_constraint)

    assert (
        constraint_mach._expressions == np.array(new_constraint).reshape(-1, 2**n - 1)
    ).all()
    assert constraint_mach._expressions.shape == (og_shape[0] + 1, og_shape[1])


def test_add_2d_single_constraint_to_empty_constraint() -> None:
    n = 3

    constraint_mach = Constraints(n=n)

    new_constraint = np.array([[_ for _ in range(2**n - 1)]]).reshape(
        (-1, 2**n - 1)
    )
    constraint_mach.add_expressions(new_constraint)

    assert (constraint_mach._expressions == new_constraint).all()


def test_add_multiple_constraints_in_list_to_empty_constraint() -> None:
    n = 3
    constraint_mach = Constraints(n=n)

    num_constraints = 5
    new_constraints = [
        [_ * (2**n - 1) + x for x in range(2**n - 1)]
        for _ in range(num_constraints)
    ]
    constraint_mach.add_expressions(new_constraints)

    assert (constraint_mach._expressions == np.array(new_constraints)).all()


def test_add_multiple_constraints_array_to_empty_constraint() -> None:
    n = 3
    constraint_mach = Constraints(n=n)

    num_constraints = 5
    new_constraints = np.array(
        [
            [_ * (2**n - 1) + x for x in range(2**n - 1)]
            for _ in range(num_constraints)
        ]
    )
    constraint_mach.add_expressions(new_constraints)

    assert (constraint_mach._expressions == new_constraints).all()


def test_clear_constraint_from_empty_constraint() -> None:
    n = 3
    constraint_mach = Constraints(n=n)
    constraint_mach.clear_expressions()

    assert constraint_mach._expressions.size == 0
    assert constraint_mach._expressions.shape == (0, 2**n - 1)


def test_clear_constraint_from_non_empty_constraints() -> None:
    n = 3
    constraint_mach = Constraints(n=n)

    num_constraints = 5
    new_constraints = np.array(
        [
            [_ * (2**n - 1) + x for x in range(2**n - 1)]
            for _ in range(num_constraints)
        ]
    )
    constraint_mach.add_expressions(new_constraints)

    constraint_mach.clear_expressions()

    assert constraint_mach._expressions.size == 0
    assert constraint_mach._expressions.shape == (0, 2**n - 1)


def test_single_constraint_to_non_empty_constraint() -> None:
    n = 3
    constraint_mach = Constraints(n=n)

    num_constraints = 5
    old_constraint = np.array(
        [
            [_ * (2**n - 1) + x for x in range(2**n - 1)]
            for _ in range(num_constraints)
        ]
    )
    constraint_mach.add_expressions(old_constraint)
    og_shape = constraint_mach._expressions.shape

    new_constraint = [0 for _ in range(2**n - 1)]
    constraint_mach.add_expressions(new_constraint)

    assert constraint_mach._expressions.shape == (og_shape[0] + 1, og_shape[1])
    assert (
        constraint_mach._expressions == np.vstack((old_constraint, new_constraint))
    ).all()


def test_single_constraint_1d_array_to_non_empty_constraint() -> None:
    n = 3
    constraint_mach = Constraints(n=n)

    num_constraints = 5
    old_constraint = np.array(
        [
            [_ * (2**n - 1) + x for x in range(2**n - 1)]
            for _ in range(num_constraints)
        ]
    )
    constraint_mach.add_expressions(old_constraint)
    og_shape = constraint_mach._expressions.shape

    new_constraint = np.array([0 for _ in range(2**n - 1)])
    constraint_mach.add_expressions(new_constraint)

    assert constraint_mach._expressions.shape == (og_shape[0] + 1, og_shape[1])
    assert (
        constraint_mach._expressions == np.vstack((old_constraint, new_constraint))
    ).all()


def test_single_constraint_2d_array_to_non_empty_constraint() -> None:
    n = 3
    constraint_mach = Constraints(n=n)

    num_constraints = 5
    old_constraint = np.array(
        [
            [_ * (2**n - 1) + x for x in range(2**n - 1)]
            for _ in range(num_constraints)
        ]
    )
    constraint_mach.add_expressions(old_constraint)
    og_shape = constraint_mach._expressions.shape

    new_constraint = np.array([[0 for _ in range(2**n - 1)]])
    constraint_mach.add_expressions(new_constraint)

    assert constraint_mach._expressions.shape == (og_shape[0] + 1, og_shape[1])
    assert (
        constraint_mach._expressions == np.vstack((old_constraint, new_constraint))
    ).all()


def test_add_multi_constraints_list_to_non_empty_constraints() -> None:
    n = 3
    constraint_mach = Constraints(n=n)

    num_constraints = 5
    old_constraint = np.array(
        [
            [_ * (2**n - 1) + x for x in range(2**n - 1)]
            for _ in range(num_constraints)
        ]
    )
    constraint_mach.add_expressions(old_constraint)
    og_shape = constraint_mach._expressions.shape

    num_constraints = 2
    new_constraint = [[0 for _ in range(2**n - 1)] for x in range(num_constraints)]
    constraint_mach.add_expressions(new_constraint)

    assert constraint_mach._expressions.shape == (
        og_shape[0] + num_constraints,
        og_shape[1],
    )
    assert (
        constraint_mach._expressions == np.vstack((old_constraint, new_constraint))
    ).all()


def test_add_multi_constraints_array_to_non_empty_constraints() -> None:
    n = 3
    constraint_mach = Constraints(n=n)

    num_constraints = 5
    old_constraint = np.array(
        [
            [_ * (2**n - 1) + x for x in range(2**n - 1)]
            for _ in range(num_constraints)
        ]
    )
    constraint_mach.add_expressions(old_constraint)
    og_shape = constraint_mach._expressions.shape

    num_constraints = 2
    new_constraint = np.array(
        [[0 for _ in range(2**n - 1)] for x in range(num_constraints)]
    )
    constraint_mach.add_expressions(new_constraint)

    assert constraint_mach._expressions.shape == (
        og_shape[0] + num_constraints,
        og_shape[1],
    )
    assert (
        constraint_mach._expressions == np.vstack((old_constraint, new_constraint))
    ).all()
