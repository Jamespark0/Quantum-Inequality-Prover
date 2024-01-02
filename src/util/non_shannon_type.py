import numpy as np
from numpy.typing import NDArray

from src.model import EntropicSpace


def non_shannon_type_under_four_random_variable(
    space: EntropicSpace,
) -> NDArray[np.float64]:
    index_to_coefficient = {
        frozenset([1]): -1,
        frozenset([1, 2]): -1,
        frozenset([3, 4]): 3,
        frozenset([1, 3, 4]): -4,
        frozenset([1, 3]): 3,
        frozenset([1, 4]): 3,
        frozenset([2, 3]): 1,
        frozenset([2, 4]): 1,
        frozenset([2, 3, 4]): -1,
        frozenset([3]): -2,
        frozenset([4]): -2,
    }

    non_shannon_vec = np.zeros(len(space.all_pairs))
    for pair, coefficient in index_to_coefficient.items():
        non_shannon_vec[space.to_index[pair]] = coefficient

    return non_shannon_vec.reshape((-1))


if __name__ == "__main__":
    space = EntropicSpace(n=4)
    print(non_shannon_type_under_four_random_variable(space))
