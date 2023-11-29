from src.classical import ShannonInequality
from src.classical.non_shannon_type import non_shannon_type_under_four_random_variable
from src.controller import ConstraintController, InequalityController
from src.controller_factory import ControllerFactory
from src.model import EntropicSpace
from src.util import ClassicalProver


class Abstraction:
    def __init__(
        self,
        prover: ClassicalProver,
        inequality_control: InequalityController,
        constraint_control: ConstraintController,
        shannon: ShannonInequality,
    ):
        self._prover = prover
        self._inequality_controller = inequality_control
        self._constraint_controller = constraint_control
        self._shannon = shannon

    def is_shannon_type(self):
        try:
            result = self._prover.is_shannon_type(
                inequality=self._inequality_controller.get_inequality()[0],
                elemental_inequality=self._shannon.ELEMENTAL,
                constraints=self._constraint_controller.get_current_constraints(),
            )

            if result:
                print("It's Shannon-type!\n")
            else:
                print("It's not provable by ITIP algorithm!\n")

        except Exception as e:
            print(str(e).split("\n")[-1], end="\n" * 2)

    def one_round(self):
        # Get constraints:
        self._constraint_controller.add_constraints()

        # get inequalities
        self._inequality_controller.set_inequality()

        # calculate inequalities:
        self.is_shannon_type()


def main(space: EntropicSpace):
    factory = ControllerFactory(space=space)
    # constraint_controller = factory.get_constraint_controller()
    # inequality_controller = factory.get_inequality_controller()
    # shannon = ShannonInequality(entropic_space=space)

    abstraction = Abstraction(
        prover=ClassicalProver(),
        inequality_control=factory.get_inequality_controller(),
        constraint_control=factory.get_constraint_controller(),
        shannon=ShannonInequality(space),
    )

    abstraction.one_round()


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
