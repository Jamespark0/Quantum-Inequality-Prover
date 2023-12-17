from dataclasses import dataclass, field

from src.classical.shannon_inequality import ShannonInequality
from src.controller.constraint_controller import ConstraintController
from src.controller.inequality_controller import InequalityController
from src.controller_factory import ControllerFactory
from src.model.app_model import AppModel
from src.model.entropic_space import EntropicSpace
from src.model.quantum_inequality import QuantumInequality
from src.view.app_view import AppView


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


@dataclass
class ClassicalAppController:
    model: AppModel = field(init=False)
    view: AppView = field(init=False)

    def initialization(self):
        self.view = AppView()

        self.view.greeting()
        space = EntropicSpace(n=self.view.get_num_random_variables())
        factory = ControllerFactory(space=space)

        self.model = AppModel(
            _constraint_controller=factory.get_constraint_controller(),
            _inequality_controller=factory.get_inequality_controller(),
            _elemental_inequalities=ShannonInequality(space).ELEMENTAL,
        )

        self.model.actions = {
            "1": (add_new_constraints, self.model.constraint_controller),
            "2": (show_constraints, self.model.constraint_controller),
            "3": (clear_all_constraints, self.model.constraint_controller),
            "4": (update_inequality, self.model.inequality_controller),
            "5": (show_inequality, self.model.inequality_controller),
            "6": (self.is_shannon_type,),
        }

    def is_shannon_type(self):
        pass


class QuantumAppController:
    model: AppModel = field(init=False)
    view: AppView = field(init=False)

    def initialization(self):
        self.view = AppView()

        self.view.greeting()
        space = EntropicSpace(n=self.view.get_num_random_variables())
        factory = ControllerFactory(space=space)

        self.model = AppModel(
            _constraint_controller=factory.get_constraint_controller(),
            _inequality_controller=factory.get_inequality_controller(),
            _elemental_inequalities=QuantumInequality(space).ELEMENTAL,
        )

        self.model.actions = {
            "1": (add_new_constraints, self.model.constraint_controller),
            "2": (show_constraints, self.model.constraint_controller),
            "3": (clear_all_constraints, self.model.constraint_controller),
            "4": (update_inequality, self.model.inequality_controller),
            "5": (show_inequality, self.model.inequality_controller),
            "6": (self.is_shannon_type,),
        }

    def is_shannon_type(self):
        pass


if __name__ == "__main__":
    # app = ClassicalAppController()
    app = QuantumAppController()
    app.initialization()
    app.view.show_actions(app.model.actions)

    print(app.view.get_action(app.model.actions))
