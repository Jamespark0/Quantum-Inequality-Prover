from dataclasses import dataclass
from itertools import combinations

import numpy as np
from numpy.typing import NDArray


@dataclass
class ShannonInequality:
    n: int

    def __post_init__(self):
        self.all_pairs: tuple[frozenset[int], ...] = self._get_all_pairs(self.n)
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
    
    def _get_type2_elemental_entropic_vector(self, i:int, j:int) -> list[list[int]]:
        """
        The type 2 elemental form is the mutual conditional entropy, taking the form of 
        I(X_{i}; X_{j}|X_{K}) where K is a subset of N - {i,j}

        Args:
            i (int): the index of a random variable
            j (int): the index of the other random variable

        Returns:
            list[list[int]]: a list of entropic vectors, each row corresponds to a mutual 
            conditional entropy given by i and j.
        """
        supersets_ij = [pair - {i,j} for pair in self.all_pairs if pair.issuperset({i, j})]
        
        all_type2_entropic_vecotrs_ij = []
        for superset in supersets_ij:
            curr_entropic_vec: list[int] = [0 for _ in range(2**(self.n) - 1)]
            curr_entropic_vec[self.to_index[superset.union({i,j})]] = -1
            if superset != set():
                curr_entropic_vec[self.to_index[superset]] = -1
            curr_entropic_vec[self.to_index[superset.union({i})]] = 1
            curr_entropic_vec[self.to_index[superset.union({j})]] = 1

            all_type2_entropic_vecotrs_ij.append(curr_entropic_vec)
        
        return all_type2_entropic_vecotrs_ij
    
    def get_elemental_inequalities(self) -> NDArray:
        g: list[list[int]] = []
        # Get type 1 elemental inequalities
        for i in range(1, self.n+1):
            g.append(self._get_type1_elemental_entropic_vector(i=i))

        #  Get type 2 elemental inequalities
        for pair in self.all_pairs:
            if len(pair) == 2:
                g.extend(self._get_type2_elemental_entropic_vector(*pair))

        return np.array(g)
            

if __name__ == "__main__":
    shannon_inequality = ShannonInequality(n=2)
    print(shannon_inequality.all_pairs)
    print(shannon_inequality.all_pairs[-1] - {1})
    print(shannon_inequality._get_type1_elemental_entropic_vector(1))

    print(shannon_inequality.get_elemental_inequalities().shape)
    print(shannon_inequality.get_elemental_inequalities())
    print(shannon_inequality.all_pairs)
    