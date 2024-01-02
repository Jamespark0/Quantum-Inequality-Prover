from dataclasses import dataclass
from itertools import combinations

import numpy as np
from numpy.typing import NDArray

from src.model import EntropicSpace


@dataclass
class QuantumInequality:
    space: EntropicSpace

    def __post_init__(self):
        self._elemental = self._get_all_inequalities()
        self.index_to_pair = dict(
            (
                zip(
                    [x for x in range(1, len(self.space.all_pairs) + 1)],
                    self.space.all_pairs,
                )
            )
        )

    def _get_type_1_elemental_vector(self, i: int, j: int):
        remaining: frozenset[int] = self.space.universal - {i, j}

        elemental_i_j: NDArray = np.empty((0, len(self.space.all_pairs)))

        # Combinations run from r = 0 to r = num of all remainings
        for r in range(len(remaining) + 1):
            for intersection in combinations(remaining, r):
                set_i = frozenset(intersection).union({i})
                set_j = frozenset(intersection).union({j})

                vector = np.zeros(len(self.space.all_pairs))
                vector[self.space.to_index[set_i]] = 1
                vector[self.space.to_index[set_j]] = 1
                vector[self.space.to_index[frozenset(set_i.union(set_j))]] = -1

                # Exclude intersections being empty
                if intersection != tuple():
                    vector[self.space.to_index[frozenset(intersection)]] = -1

                elemental_i_j = np.vstack((elemental_i_j, vector))

        return elemental_i_j

    def _get_type_2_elemental_vector(self, k: int):
        intersection = {k}

        i_diff_j = {(k + 1) % self.space.n if k + 1 > self.space.n else k + 1}

        remaining = self.space.universal - intersection - i_diff_j

        elemental_k = np.empty((0, len(self.space.all_pairs)))

        for r in range(0, len(remaining) + 1):
            for i_remaning in combinations(remaining, r):
                vec = np.zeros(len(self.space.all_pairs))

                i_remaning = frozenset(i_remaning)
                j_remaining = remaining.difference(i_remaning)
                set_i = (i_remaning.union(i_diff_j)).union(intersection)
                set_j = j_remaining.union(intersection)

                vec[self.space.to_index[set_i]] = 1
                vec[self.space.to_index[set_j]] = 1
                vec[self.space.to_index[set_i.difference(set_j)]] = -1
                if j_remaining != frozenset():
                    vec[self.space.to_index[set_j.difference(set_i)]] = -1

                elemental_k = np.vstack((elemental_k, vec))

        return elemental_k

    def _get_all_type_1(self):
        all_type_1: NDArray = np.empty((0, len(self.space.all_pairs)))
        for group in self.space.all_pairs:
            if len(group) > 2:
                break
            elif len(group) == 2:
                i, j = group
                all_type_1 = np.vstack(
                    (all_type_1, self._get_type_1_elemental_vector(i, j))
                )
        return all_type_1

    def _get_all_type_2(self):
        all_type_2 = np.empty((0, len(self.space.all_pairs)))
        for k in range(1, self.space.n + 1):
            all_type_2 = np.vstack((all_type_2, self._get_type_2_elemental_vector(k=k)))

        return all_type_2

    def _get_all_inequalities(self):
        return np.vstack((self._get_all_type_1(), self._get_all_type_2()))

    @property
    def ELEMENTAL(self):
        return self._elemental
