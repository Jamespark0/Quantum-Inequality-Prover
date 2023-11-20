from dataclasses import dataclass
from itertools import combinations


@dataclass
class ShannonInequality:
    n: int

    def __post_init__(self):
        self.all_pairs: tuple = self._get_all_pairs(self.n)
        self.to_index = dict(zip(self.all_pairs, [x for x in range(2**self.n - 1)]))
        # to be deleted, just for testing
        self.index_to_pair = dict(zip([x for x in range(2**(self.n) - 1)], self.all_pairs))

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
    
    def _get_type1_elemental_entropic_vector(self, i: int) -> list[int]:
        """
        The type 1 elemental form is the conditional entropy, taking the form of
        H(X_{i}|X_{N-{i}})

        Args:
            i (int): The random variable will focus on

        Returns:
            list[int]: The entropic vector of the given conditional entropy
        """
        elemental_vector_i: list[int] = [0 for _ in range(2**(self.n) - 1)]
        elemental_vector_i[-1] = 1
        elemental_vector_i[self.to_index[self.all_pairs[-1] - {i}]] = -1

        return elemental_vector_i

if __name__ == "__main__":
    shannon_inequality = ShannonInequality(n=3)
    print(shannon_inequality.all_pairs)
    print(shannon_inequality.all_pairs[-1] - {1})
    print(shannon_inequality._get_type1_elemental_entropic_vector(1))
