import numpy as np

from src.model import ConstraintHandler


def test_initialize() -> None:
    n = 3

    constraints_mach = ConstraintHandler(random_variables=3)

    assert constraints_mach._constraints.size == 0
    assert constraints_mach._constraints.shape == (0, 2**n - 1)


def test_add_single_list_constraints_to_empty_constraint() -> None:
    n = 3

    constraints_mach = ConstraintHandler(random_variables=n)
    og_shape = constraints_mach._constraints.shape

    constraint = [0 for _ in range(2**n - 1)]
    constraints_mach.add_constraints(constraint)

    assert (
        constraints_mach._constraints == np.array(constraint).reshape((-1, 2**n - 1))
    ).all()
    assert constraints_mach._constraints.shape == (og_shape[0] + 1, og_shape[1])


def test_add_1d_array_constraint_to_empty_constraint() -> None:
    n = 3

    constraint_mach = ConstraintHandler(random_variables=n)
    og_shape = constraint_mach._constraints.shape

    new_constraint = np.array([_ for _ in range(2**n - 1)])
    constraint_mach.add_constraints(new_constraints=new_constraint)

    assert (
        constraint_mach._constraints == np.array(new_constraint).reshape(-1, 2**n - 1)
    ).all()
    assert constraint_mach._constraints.shape == (og_shape[0] + 1, og_shape[1])


def test_add_2d_single_constraint_to_empty_constraint() -> None:
    n = 3

    constraint_mach = ConstraintHandler(random_variables=n)
    og_shape = constraint_mach._constraints.shape

    new_constraint = np.array([[_ for _ in range(2**n - 1)]]).reshape(
        (-1, 2**n - 1)
    )
    constraint_mach.add_constraints(new_constraints=new_constraint)

    assert (constraint_mach._constraints == new_constraint).all()


def test_add_multiple_constraints_in_list_to_empty_constraint() -> None:
    n = 3
    constraint_mach = ConstraintHandler(random_variables=n)
    og_shape = constraint_mach._constraints.shape

    num_constraints = 5
    new_constraints = [
        [_ * (2**n - 1) + x for x in range(2**n - 1)]
        for _ in range(num_constraints)
    ]
    constraint_mach.add_constraints(new_constraints=new_constraints)

    assert (constraint_mach._constraints == np.array(new_constraints)).all()


def test_add_multiple_constraints_array_to_empty_constraint() -> None:
    n = 3
    constraint_mach = ConstraintHandler(random_variables=n)
    og_shape = constraint_mach._constraints.shape

    num_constraints = 5
    new_constraints = np.array(
        [
            [_ * (2**n - 1) + x for x in range(2**n - 1)]
            for _ in range(num_constraints)
        ]
    )
    constraint_mach.add_constraints(new_constraints=new_constraints)

    assert (constraint_mach._constraints == new_constraints).all()


def test_clear_constraint_from_empty_constraint() -> None:
    n = 3
    constraint_mach = ConstraintHandler(random_variables=n)
    constraint_mach.clear_constraint()

    assert constraint_mach._constraints.size == 0
    assert constraint_mach._constraints.shape == (0, 2**n - 1)


def test_clear_constraint_from_non_empty_constraints() -> None:
    n = 3
    constraint_mach = ConstraintHandler(random_variables=n)

    num_constraints = 5
    new_constraints = np.array(
        [
            [_ * (2**n - 1) + x for x in range(2**n - 1)]
            for _ in range(num_constraints)
        ]
    )
    constraint_mach.add_constraints(new_constraints=new_constraints)

    constraint_mach.clear_constraint()

    assert constraint_mach._constraints.size == 0
    assert constraint_mach._constraints.shape == (0, 2**n - 1)


def test_single_constraint_to_non_empty_constraint() -> None:
    n = 3
    constraint_mach = ConstraintHandler(random_variables=n)

    num_constraints = 5
    old_constraint = np.array(
        [
            [_ * (2**n - 1) + x for x in range(2**n - 1)]
            for _ in range(num_constraints)
        ]
    )
    constraint_mach.add_constraints(new_constraints=old_constraint)
    og_shape = constraint_mach._constraints.shape

    new_constraint = [0 for _ in range(2**n - 1)]
    constraint_mach.add_constraints(new_constraints=new_constraint)

    assert constraint_mach._constraints.shape == (og_shape[0] + 1, og_shape[1])
    assert (
        constraint_mach._constraints == np.vstack((old_constraint, new_constraint))
    ).all()


def test_single_constraint_1d_array_to_non_empty_constraint() -> None:
    n = 3
    constraint_mach = ConstraintHandler(random_variables=n)

    num_constraints = 5
    old_constraint = np.array(
        [
            [_ * (2**n - 1) + x for x in range(2**n - 1)]
            for _ in range(num_constraints)
        ]
    )
    constraint_mach.add_constraints(new_constraints=old_constraint)
    og_shape = constraint_mach._constraints.shape

    new_constraint = np.array([0 for _ in range(2**n - 1)])
    constraint_mach.add_constraints(new_constraints=new_constraint)

    assert constraint_mach._constraints.shape == (og_shape[0] + 1, og_shape[1])
    assert (
        constraint_mach._constraints == np.vstack((old_constraint, new_constraint))
    ).all()


def test_single_constraint_2d_array_to_non_empty_constraint() -> None:
    n = 3
    constraint_mach = ConstraintHandler(random_variables=n)

    num_constraints = 5
    old_constraint = np.array(
        [
            [_ * (2**n - 1) + x for x in range(2**n - 1)]
            for _ in range(num_constraints)
        ]
    )
    constraint_mach.add_constraints(new_constraints=old_constraint)
    og_shape = constraint_mach._constraints.shape

    new_constraint = np.array([[0 for _ in range(2**n - 1)]])
    constraint_mach.add_constraints(new_constraints=new_constraint)

    assert constraint_mach._constraints.shape == (og_shape[0] + 1, og_shape[1])
    assert (
        constraint_mach._constraints == np.vstack((old_constraint, new_constraint))
    ).all()


def test_add_multi_constraints_list_to_non_empty_constraints() -> None:
    n = 3
    constraint_mach = ConstraintHandler(random_variables=n)

    num_constraints = 5
    old_constraint = np.array(
        [
            [_ * (2**n - 1) + x for x in range(2**n - 1)]
            for _ in range(num_constraints)
        ]
    )
    constraint_mach.add_constraints(new_constraints=old_constraint)
    og_shape = constraint_mach._constraints.shape

    num_constraints = 2
    new_constraint = [[0 for _ in range(2**n - 1)] for x in range(num_constraints)]
    constraint_mach.add_constraints(new_constraints=new_constraint)

    assert constraint_mach._constraints.shape == (
        og_shape[0] + num_constraints,
        og_shape[1],
    )
    assert (
        constraint_mach._constraints == np.vstack((old_constraint, new_constraint))
    ).all()


def test_add_multi_constraints_array_to_non_empty_constraints() -> None:
    n = 3
    constraint_mach = ConstraintHandler(random_variables=n)

    num_constraints = 5
    old_constraint = np.array(
        [
            [_ * (2**n - 1) + x for x in range(2**n - 1)]
            for _ in range(num_constraints)
        ]
    )
    constraint_mach.add_constraints(new_constraints=old_constraint)
    og_shape = constraint_mach._constraints.shape

    num_constraints = 2
    new_constraint = np.array(
        [[0 for _ in range(2**n - 1)] for x in range(num_constraints)]
    )
    constraint_mach.add_constraints(new_constraints=new_constraint)

    assert constraint_mach._constraints.shape == (
        og_shape[0] + num_constraints,
        og_shape[1],
    )
    assert (
        constraint_mach._constraints == np.vstack((old_constraint, new_constraint))
    ).all()


def test_add_constraints_with_v2_to_empty_constraints() -> None:
    n = 3
    constraints_mach = ConstraintHandler(random_variables=n)

    new_constraints = [[0 for _ in range(2**n - 1)]]
    constraints_mach.add_constraints_v2(*new_constraints)

    assert constraints_mach._constraints.shape == (1, 2**n - 1)
