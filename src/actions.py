from src.controller.constraint_controller import ConstraintController
from src.controller.inequality_controller import InequalityController


def add_new_constraints(controller: ConstraintController):
    controller.add_expressions()


def show_constraints(controller: ConstraintController) -> None:
    controller.show_expressions()


def clear_all_constraints(controller: ConstraintController) -> None:
    controller.clear_constraints()


def update_inequality(controller: InequalityController) -> None:
    controller.add_expressions()


def show_inequality(controller: InequalityController) -> None:
    controller.show_expressions()
