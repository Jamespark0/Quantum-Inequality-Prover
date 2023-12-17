# Terminal User Interface View
from numpy.typing import NDArray

from src.util import to_joint_entropy
from src.view.view import View


class ViewTUI(View):
    def __init__(self, index_order: tuple, target: tuple):
        self.index_order = index_order

        # the first element should be the indicating whether it is a constraint or an inequlaity
        # the second element is whether it is " = 0" or ">= 0" respectively
        # the tuple cna contain only two elements
        self._target = target

    def show_expressions(self, expressions: NDArray):
        # Prevents the provided constraints is not what we are looking for
        if expressions.shape[1] != len(self.index_order):
            raise ValueError(
                f"The columns of the {self._target[0]} does not match the dimension of the entropic space."
            )

        for expression in expressions:
            print(
                f'{" + ".join(f"{coefficient} * {to_joint_entropy(self.index_order[i])}" for i, coefficient in enumerate(expression))}',
                end=f" {self._target[1]} \n",
            )
            print()

    def show_rules(self) -> None:
        print(
            f"An information {self._target[0]} is expressed as the following:",
            end="\n" * 2,
        )
        print(
            f'{" + ".join(f"a({i}) * {to_joint_entropy(pair=x)}" for i, x in enumerate(self.index_order, start=1))}',
            end=f" {self._target[1]} " + "\n" * 2,
        )

    def get_input_message(self) -> str:
        return (
            f"The input should contain {len(self.index_order)} numbers, and in the order of: "
            + f'{", ".join(f"a({i})" for i in range(1, len(self.index_order) + 1))}'
        )

    def get_user_input(self) -> str:
        expressions = input("# ")
        return expressions
