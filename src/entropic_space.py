from dataclasses import dataclass
from itertools import combinations


@dataclass
class EntropicSpace:
    """
    Generate all possible pairs from n random variables.

    The class includes information of 

    1. All the pairs

    2. The index in an entropic vector that corresponds to the given pairing
    
    """
    n: int

    def __post_init__(self):
        self.all_pairs: tuple[frozenset[int], ...] = self._get_all_pairs(self.n)
        self.to_index = dict(zip(self.all_pairs, [x for x in range(2**self.n - 1)]))
        self.universal: frozenset = frozenset({x for x in range(1, self.n + 1)})

    # Just to help generate pairs
    def _get_all_pairs(self, n: int) -> tuple[frozenset[int], ...]:
        random_variable_labeling = set(range(1, n + 1))

        return tuple(
            [
                frozenset(x)
                for _ in range(1, n + 1)
                for x in combinations(random_variable_labeling, r=_)
            ]
        )