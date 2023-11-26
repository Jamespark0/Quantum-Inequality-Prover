from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray

from src.shared.entropic_space import EntropicSpace


@dataclass
class ShannonInequality:
    entropic_space: EntropicSpace

    def __post_init__(self):
        self._ELEMENTAL = self._get_elemental_inequalities()

        self.index_to_pair = dict(
            zip(
                [x for x in range(2 ** (self.entropic_space.n) - 1)],
                self.entropic_space.all_pairs,
            )
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

        elemental_vector_i: list[int] = [
            0 for _ in range(2 ** (self.entropic_space.n) - 1)
        ]
        elemental_vector_i[
            self.entropic_space.to_index[self.entropic_space.universal]
        ] = 1
        elemental_vector_i[
            self.entropic_space.to_index[self.entropic_space.universal - {i}]
        ] = -1

        return elemental_vector_i

    def _get_type2_elemental_entropic_vector(self, i: int, j: int) -> list[list[int]]:
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
        supersets_ij = [
            pair - {i, j}
            for pair in self.entropic_space.all_pairs
            if pair.issuperset({i, j})
        ]

        all_type2_entropic_vecotrs_ij = []
        for superset in supersets_ij:
            curr_entropic_vec: list[int] = [
                0 for _ in range(2 ** (self.entropic_space.n) - 1)
            ]
            curr_entropic_vec[self.entropic_space.to_index[superset.union({i, j})]] = -1
            # When set K is not an empty set
            if superset != set():
                curr_entropic_vec[self.entropic_space.to_index[superset]] = -1
            curr_entropic_vec[self.entropic_space.to_index[superset.union({i})]] = 1
            curr_entropic_vec[self.entropic_space.to_index[superset.union({j})]] = 1

            all_type2_entropic_vecotrs_ij.append(curr_entropic_vec)

        return all_type2_entropic_vecotrs_ij

    def _get_elemental_inequalities(self) -> NDArray:
        g: list[list[int]] = []
        # Get type 1 elemental inequalities
        for i in range(1, self.entropic_space.n + 1):
            g.append(self._get_type1_elemental_entropic_vector(i=i))

        #  Get type 2 elemental inequalities
        for pair in self.entropic_space.all_pairs:
            if len(pair) == 2:
                g.extend(self._get_type2_elemental_entropic_vector(*pair))

            # The following line is used for speed boost as I assume the order of the corresponding
            # joint entropy is ascending
            elif len(pair) > 2:
                break

        return np.array(g)

    @property
    def ELEMENTAL(self):
        return self._ELEMENTAL
