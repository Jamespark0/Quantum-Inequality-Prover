import numpy as np
from numpy.typing import NDArray

from src.controller.controller import Controller
from src.model import Inequality
from src.view import InequalityView


class InequalityController(Controller):
    def __init__(self, model: Inequality, view: InequalityView) -> None:
        self._model: Inequality = model
        self._view: InequalityView = view

    def get_expressions(self) -> NDArray:
        return self._model.expressions

    def add_expressions(self):
        self._view.show_rules()
        print(self._view.get_input_message())
        while True:
            new_inequality = self._view.get_user_input()

            try:
                new_inequality = self._validate_and_format_user_input(
                    inequality=new_inequality
                )

                self._model.expressions = np.vstack(
                    (np.empty((0, self._model.expressions.shape[1])), new_inequality)
                )
                break
            except ValueError as e:
                print(str(e).split("\n")[-1], end="\n" * 2)
                print("Please enter a new inequality!")
            except Exception as e:
                # Handle errors that are not value errors
                # which I do not expect
                print(f"Unexpected Error: {e}")

    def _validate_and_format_user_input(self, inequality: str):
        """
        Format a single constraint which string into a list of numbers.

        Also check if the constraint has the correct length.

        Args:
            inequality (str): A single constraint. The coefficients in the canonical form is separated by space.

        Raises:
            ValueError: If the coefficients does not match the number of joint entropies.

        Returns:
            list[float]: A list of float which represents the coefficient of the given constraint in canonical form.
        """
        coefficients = inequality.split()
        if len(coefficients) != self._model.expressions.shape[1]:
            raise ValueError(
                f"The inequality should contains '{self._model.expressions.shape[1]}' coefficients."
            )
        return list(map(float, coefficients))

    def show_expressions(self):
        self._view.show_expressions(self._model.expressions)


if __name__ == "__main__":
    from src.model import EntropicSpace

    n = 2
    controller = InequalityController(
        model=Inequality(n=n),
        view=InequalityView(EntropicSpace(n).all_pairs),
    )

    print("Initialize:")
    controller.show_expressions()
    controller.add_expressions()
    print("Set 1st:")
    controller.show_expressions()
    controller.add_expressions()
    controller.add_expressions()
    print("Set2nd:")
    controller.show_expressions()
