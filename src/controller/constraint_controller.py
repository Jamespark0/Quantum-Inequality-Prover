from src.model import CustomizeConstraint
from src.view import ConstraintView


class ConstraintController:
    def __init__(self, model: CustomizeConstraint, view: ConstraintView):
        self.model: CustomizeConstraint = model
        self.view: ConstraintView = view

    def get_constraints(self):
        """
        Get inequality from user, and add the constraints to model.constraints

        """
        self.view.display_constraint_rules()
        while True:
            new_constraints = input(self.view.get_constraint_input_message()).split(",")

            try:
                # Remove empty string from new_constraints
                new_constraints = list(filter(None, new_constraints))
                new_constraints = list(map(self._constraint_formatter, new_constraints))
                self.model.add_constraints(new_constraints)
                break
            except ValueError as e:
                print(str(e).split("\n")[-1], end="\n" * 2)

    def _constraint_formatter(self, constraint: str):
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
        if len(coefficients) != self.model.constraints.shape[1]:
            raise ValueError(
                f"The inequality should contains '{self.model.constraints.shape[1]}' coefficients."
            )
        return list(map(float, coefficients))

    def clear_constraints(self):
        self.model.clear_constraint()

    def show_constraints(self):
        self.view.show_current_constraint(self.model.constraints)


if __name__ == "__main__":
    from src.model import EntropicSpace

    n = 2
    controller = ConstraintController(
        model=CustomizeConstraint(random_variables=n),
        view=ConstraintView(EntropicSpace(n)),
    )

    print("Initialize:")
    controller.show_constraints()
    controller.get_constraints()
    print("Add 1st:")
    controller.show_constraints()
    controller.get_constraints()
    print("Add 2nd:")
    controller.show_constraints()
    controller.clear_constraints()
    print("After clearing")
    controller.show_constraints()
