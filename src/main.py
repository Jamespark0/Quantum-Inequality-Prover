import time

from src.classical import ShannonInequality
from src.classical.non_shannon_type import non_shannon_type_under_four_random_variable
from src.classical_prover import ClassicalProver
from src.controller.constraint_controller import ConstraintController
from src.controller.inequality_controller import InequalityController
from src.controller_factory import ControllerFactory
from src.model import EntropicSpace


def main(space: EntropicSpace):
    factory = ControllerFactory(space=space)
    constraint_controller = factory.get_constraint_controller()
    inequality_controller = factory.get_inequality_controller()
    shannon = ShannonInequality(entropic_space=space)

    constraint_controller.show_expressions()
    inequality_controller.show_expressions()
    print(shannon.ELEMENTAL)

    # abstraction = Abstraction(
    #     prover=ClassicalProver(),
    #     inequality_control=factory.get_inequality_controller(),
    #     constraint_control=factory.get_constraint_controller(),
    #     shannon=ShannonInequality(space),
    # )

    # abstraction.one_round()


if __name__ == "__main__":
    # Prompt user to get the number of random variables
    while True:
        n = input("Input the number of random variables in the system:\n# ")
        if n.isdigit() and int(n) > 1:
            n = int(n)
            break
        else:
            print(f"{n} is not an integer greater than 1!")

    space = EntropicSpace(n=n)
    main(space=space)
