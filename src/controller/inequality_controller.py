from numpy.typing import NDArray

from src.model import Inequality
from src.view import InequalityView


class InequalityController:
    def __init__(self, model: Inequality, view: InequalityView) -> None:
        self._model: Inequality = model
        self._view: InequalityView = view

    def get_inequality(self) -> NDArray:
        return self._model.inequality

    def set_inequality(self):
        self._view.display_inequality_rules()
        while True:
            new_inequality = input(self._view.get_inequality_input_message())

            try:
                new_inequality = self._format_inequality(inequality=new_inequality)
                self._model.inequality = new_inequality
                break
            except ValueError as e:
                print(str(e).split("\n")[-1], end="\n" * 2)
            except Exception as e:
                # Handle errors that are not value errors
                # which I do not expect
                print(f"Unexpected Error: {e}")

    def _format_inequality(self, inequality: str):
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
        if len(coefficients) != self._model.inequality.shape[1]:
            raise ValueError(
                f"The inequality should contains '{self._model.inequality.shape[1]}' coefficients."
            )
        return list(map(float, coefficients))

    def show_inequality(self):
        self._view.show_inequality(self._model.inequality)


if __name__ == "__main__":
    from src.model import EntropicSpace

    n = 2
    controller = InequalityController(
        model=Inequality(n=n),
        view=InequalityView(EntropicSpace(n)),
    )

    print("Initialize:")
    controller.show_inequality()
    controller.set_inequality()
    print("Set 1st:")
    controller.show_inequality()
    controller.set_inequality()
    print("Set2nd:")
    controller.show_inequality()
