from dataclasses import dataclass
from typing import Sequence

from numpy.typing import NDArray

from src.util import vec_to_entropy_expression


@dataclass(frozen=True)
class ProverResultMessage:
    def _shortest(
        self,
        elemental_opening_msg: str,
        used_elementals: NDArray | None,
        used_constraints: NDArray | None,
        elementals: NDArray,
        constraints: NDArray,
        index_order: Sequence[frozenset],
        show_coefficients: bool = True,
    ) -> tuple[tuple, tuple]:
        """
        This method is only called for generating the shortest proof for von-Neumann/Shannon-type inequality

        Returns:
            str: Expressed in coefficients times joint entropy
        """
        if used_elementals is not None:
            msg_elementals: tuple = tuple(
                [elemental_opening_msg]
                + [
                    (
                        f"{used} x [{vec_to_entropy_expression(vec=elemental, index_order = index_order)}]"
                        if show_coefficients
                        else f"{vec_to_entropy_expression(vec=elemental, index_order = index_order)}"
                    )
                    for used, elemental in zip(used_elementals, elementals)
                    if used != 0
                ]
            )
        else:
            msg_elementals = tuple()

        if used_constraints is not None and len(used_constraints) != 0:
            msg_constraints: tuple = tuple(
                ["The following constraints are used:"]
                + [
                    (
                        f"{used} x [{vec_to_entropy_expression(vec=constraint, index_order = index_order)}]"
                        if show_coefficients
                        else f"{vec_to_entropy_expression(vec=constraint, index_order = index_order)}"
                    )
                    for used, constraint in zip(used_constraints, constraints)
                    if used != 0
                ]
            )
        else:
            msg_constraints = tuple()

        return (msg_elementals, msg_constraints)

    def generate_shortest_proof(
        self,
        used_elementals: NDArray | None,
        used_constraints: NDArray | None,
        elementals: NDArray,
        constraints: NDArray,
        index_order: Sequence[frozenset],
        show_coefficients: bool = True,
    ) -> tuple[tuple, tuple]:
        return self._shortest(
            elemental_opening_msg="The following inequalities are used!",
            used_elementals=used_elementals,
            used_constraints=used_constraints,
            elementals=elementals,
            constraints=constraints,
            index_order=index_order,
            show_coefficients=show_coefficients,
        )

    def generate_shortest_disprove(
        self,
        used_elementals: NDArray | None,
        used_constraints: NDArray | None,
        elementals: NDArray,
        constraints: NDArray,
        index_order: Sequence[frozenset],
    ) -> tuple[tuple, tuple]:
        return self._shortest(
            elemental_opening_msg="To disprove the inequality, the following quantities can be set to zero!",
            used_elementals=used_elementals,
            used_constraints=used_constraints,
            elementals=elementals,
            constraints=constraints,
            index_order=index_order,
            show_coefficients=False,
        )
