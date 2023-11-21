"""
This is file is meant to see if search method is faster or not.

Result: No!
"""

import time
from itertools import combinations


def get_all_pairs(n: int) -> tuple[frozenset[int], ...]:
        random_variable_labeling = set(range(1, n + 1))

        return tuple(
            [
                frozenset(x)
                for _ in range(1, n + 1)
                for x in combinations(random_variable_labeling, r=_)
            ]
        )

if __name__ == "__main__":
    n = 20
    all_pairs = get_all_pairs(n)
    
    ta_0 = time.time()
    a = max(all_pairs)
    ta_1 = time.time()

    print(f"Search method time: {ta_1 - ta_0}")

    tb_0 = time.time()
    b = {x for x in range(n)}
    tb_1 = time.time()

    print(f"Creation time: {tb_1 - tb_0}")
