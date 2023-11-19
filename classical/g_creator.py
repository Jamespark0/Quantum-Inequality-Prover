from dataclasses import dataclass
from itertools import combinations


@dataclass
class ShannonInequality:
    n: int

    def __post_init__(self):
        self.all_pairs: tuple = self._get_all_pairs(self.n)
        self.to_index = dict(zip(self.all_pairs, [x for x in range(2**self.n - 1)]))

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


if __name__ == "__main__":
    shannon_inequality = ShannonInequality(n=3)
    print(shannon_inequality.__dict__)
