from itertools import combinations


def all_combinations(n: int) -> tuple[set[int], ...]:
    random_variable_labeling = set(range(1, n + 1))

    return tuple(
        [
            set(x)
            for _ in range(1, n + 1)
            for x in combinations(random_variable_labeling, r=_)
        ]
    )

