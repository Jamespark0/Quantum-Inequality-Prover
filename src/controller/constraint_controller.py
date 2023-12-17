import numpy as np

from src.controller.controller import Controller
from src.model import Constraints
from src.view import ConstraintView


class ConstraintController(Controller):
    def __init__(self, model: Constraints, view: ConstraintView):
        self.model: Constraints = model
        self.view: ConstraintView = view

    def get_expressions(self):
        return self.model.expressions

    def add_expressions(self):
        """
        Get inequality from user, and add the constraints to model.constraints

        """
        self.view.show_rules()
        print(self.view.get_input_message())
        while True:
            new_constraints = self.view.get_user_input()

            # If the user input nothing, then nothing should be added
            if new_constraints.split() == []:
                return

            try:
                # Remove empty string from new_constraints
                self.model.expressions = np.vstack(
                    (
                        self.model.expressions,
                        self._validate_and_format_user_input(new_constraints),
                    )
                )
                break
            except ValueError as e:
                print(str(e).split("\n")[-1], end="\n" * 2)
                print("Please enter new constraints!")
            except Exception as e:
                # Handle errors that are not value errors
                # which I do not expect
                print(f"Unexpected Error: {e}")

    def _validate_and_format_user_input(
        self, new_constraints: str
    ) -> list[list[float]]:
        """
        Validate and format a list of constraints.

        Args:
            new_constraints (list[str]): List of constraints, and each constraint is a string.

        Returns:
            list[list[float]]: Formatted constraints. Each constraint is described by the list of coefficients.
        """
        # Remove empty string from new_constraints
        return list(
            map(
                self._format_single_constraint,
                list(filter(None, new_constraints.split(","))),
            )
        )

    def _format_single_constraint(self, constraint: str):
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
        coefficients = constraint.split()
        if len(coefficients) != self.model.expressions.shape[1]:
            raise ValueError(
                f"The inequality should contains '{self.model.expressions.shape[1]}' coefficients."
            )
        return list(map(float, coefficients))

    def clear_constraints(self):
        self.model.expressions = np.empty((0, self.model.expressions.shape[1]))

    def show_expressions(self):
        self.view.show_expressions(self.model.expressions)


if __name__ == "__main__":
    from src.model import EntropicSpace

    n = 2
    controller = ConstraintController(
        model=Constraints(n=n), view=ConstraintView(EntropicSpace(n).all_pairs)
    )

    print("Initialize:")
    controller.show_expressions()
    controller.add_expressions()
    print("Add 1st:")
    controller.show_expressions()
    controller.add_expressions()
    print("Add 2nd:")
    controller.show_expressions()
    controller.clear_constraints()
    print("After clearing")
    controller.show_expressions()
