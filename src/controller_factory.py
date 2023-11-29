from src.controller import ConstraintController, InequalityController
from src.model import CustomizeConstraint, EntropicSpace, Inequality
from src.view import ConstraintView, InequalityView


class ControllerFactory:
    """
    Create the Constraint controller we need.

    This factory does not hold the controller. Instead, only responsible for creating it.
    """

    def __init__(self, space: EntropicSpace) -> None:
        self.space = space

    def get_constraint_controller(self) -> ConstraintController:
        constraint_model = CustomizeConstraint(random_variables=self.space.n)
        constraint_view = ConstraintView(space=self.space)
        return ConstraintController(model=constraint_model, view=constraint_view)

    def get_inequality_controller(self):
        inequality_model = Inequality(n=self.space.n)
        inequality_view = InequalityView(space=self.space)
        return InequalityController(model=inequality_model, view=inequality_view)
