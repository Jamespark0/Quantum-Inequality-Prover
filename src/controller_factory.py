from src.controller.constraint_controller import ConstraintController
from src.controller.inequality_controller import InequalityController
from src.model import Canonical, Constraints, EntropicSpace
from src.view import ConstraintView, InequalityView


class ControllerFactory:
    """
    Create the Constraint controller we need.

    This factory does not hold the controller. Instead, only responsible for creating it.
    """

    def __init__(self, space: EntropicSpace) -> None:
        self.n = space.n
        self.order_pairs = tuple(
            [pair[0] for pair in sorted(space.to_index.items(), key=lambda x: x[1])]
        )

    def get_constraint_controller(self) -> ConstraintController:
        constraint_model = Constraints(n=self.n)
        constraint_view = ConstraintView(index_order=self.order_pairs)
        return ConstraintController(model=constraint_model, view=constraint_view)

    def get_inequality_controller(self):
        inequality_model = Canonical(dim=self.n)
        inequality_view = InequalityView(index_order=self.order_pairs)
        return InequalityController(model=inequality_model, view=inequality_view)
