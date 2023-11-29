from numpy.typing import NDArray

from src.model import EntropicSpace
from src.util import to_joint_entropy


class InequalityView:
    def __init__(self, space: EntropicSpace) -> None:
        self.index_order = tuple(
            item[0] for item in sorted(space.to_index.items(), key=lambda x: x[1])
        )

    def show_inequality(self, inequality: NDArray):
        # Prevents the provided inequalities is not what we are looking for
        if inequality.shape[1] != len(self.index_order):
            raise ValueError(
                "The columns of the inequalities does not match the dimension of the entropic space."
            )

        # Prevent without init
        if inequality.shape[0] != 0:
            print(
                f'{" + ".join(f"{coefficient} * {to_joint_entropy(self.index_order[i])}" for i, coefficient in enumerate(inequality[0]))}',
                end=" = 0\n",
            )
        print()

    def display_inequality_rules(self) -> None:
        print(
            "An information inequality is expressed as the following:",
            end="\n" * 2,
        )
        print(
            f'{" + ".join(f"a({i}) * {to_joint_entropy(pair=x)}" for i, x in enumerate(self.index_order, start=1))}',
            end=" >= 0" + "\n" * 2,
        )

    def get_inequality_input_message(self) -> str:
        return (
            f"The input should contain {len(self.index_order)} numbers, and in the order of: "
            + f'{", ".join(f"a({i})" for i in range(1, len(self.index_order) + 1))}'
            + "\n# "
        )
