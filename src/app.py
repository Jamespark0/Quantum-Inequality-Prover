import os
from dataclasses import dataclass, field
from typing import Callable

from numpy.typing import NDArray

from src.classical.shannon_inequality import ShannonInequality
from src.classical_prover import ClassicalProver
from src.controller.constraint_controller import ConstraintController
from src.controller.controller import Controller
from src.controller.inequality_controller import InequalityController
from src.controller_factory import ControllerFactory
from src.model.entropic_space import EntropicSpace
from src.model.quantum_inequality import QuantumInequality


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
class App:
    init_status: bool = field(init=False, default=False)
    have_proved: bool = field(init=False, default=False)

    constraint_controller: ConstraintController = field(init=False)
    inequality_controller: InequalityController = field(init=False)
    elemental_inequality: NDArray = field(init=False)

    def entry(self):
        # Greeting message
        print("Welcome to the Information Inequality Prover!")

        # Prompt user to get the number of random variables
        while True:
            n = input("Please enter the number of random variables in the system:\n# ")
            if n.isdigit() and int(n) > 1:
                n = int(n)
                break
            else:
                print(f"{n} is not an integer greater than 1!")

        print()
        self.space = EntropicSpace(n=n)
        self.init_status = False
        self.have_proved = False

    def _setup(self):
        factory = ControllerFactory(space=self.space)
        self.constraint_controller = factory.get_constraint_controller()
        self.inequality_controller = factory.get_inequality_controller()
        # self.elemental_inequality = ShannonInequality(
        #     entropic_space=self.space
        # ).ELEMENTAL
        self.elemental_inequality = QuantumInequality(
            entropic_space=self.space
        ).ELEMENTAL

        self.actions: dict[str, tuple[Callable, Controller]] = {
            str(1): (add_new_constraints, self.constraint_controller),
            str(2): (show_constraints, self.constraint_controller),
            str(3): (clear_all_constraints, self.constraint_controller),
            str(4): (update_inequality, self.inequality_controller),
            str(5): (show_inequality, self.inequality_controller),
        }

        self.init_status = True
        self.have_proved = False

    def _get_action(self) -> tuple:
        os.system("cls" if os.name == "nt" else "clear")

        for key in self.actions.keys():
            print(f"{key} => {self.actions[key][0].__name__}")
        print(f"{len(self.actions) + 1} => check shannon-type")

        while True:
            choice = input("Please choose an operation: ")
            match choice in set(self.actions.keys()):
                case True:
                    print()
                    return self.actions[choice]
                case False:
                    if choice == f"{len(self.actions) + 1}":
                        print()
                        return (
                            self.is_shannon_type,
                            self.inequality_controller.get_expressions(),
                        )
                    else:
                        print("Pleae enter a valid operation!")

    def _prepare(self, action: Callable[..., None], parameters: Controller | NDArray):
        action(parameters)
        input("Press enter to proceed...")

    def one_round(self):
        self._setup()

        while self.have_proved is False:
            self._prepare(*self._get_action())

    def start(self) -> None:
        self.entry()
        self.one_round()

    def is_shannon_type(self, inequality):
        prover = ClassicalProver()

        try:
            result = prover.is_shannon_type(
                inequality=inequality,
                constraints=self.constraint_controller.get_expressions(),
                elemental_inequality=self.elemental_inequality,
            )
            self.have_proved = True
            if result is False:
                print("It is not provable by ITIP")
            else:
                print("It is Shannon-type!")
        except ValueError:
            print("Pleae add some inequality before the proof!")
            print()

        except Exception as e:
            print(e)


def main():
    app = App()
    app.start()


if __name__ == "__main__":
    main()
