import os
import sys

sys.path.insert(0, ".")

from two_random_variable_prover import TwoRVInequalityProver

from src import TwoRandomVariableCLI


class InteractiveProver2RV:
    def __init__(self, cli: TwoRandomVariableCLI, prover: TwoRVInequalityProver):
        self.cli = cli
        self.prover = prover

    def _calculate_inequality(self):
        os.system("clear")

        self.cli.show_inequality_rules()
        self.prover.show_constraints()
        inequality = self.cli.get_inequality()

        if self.prover.is_shannon_type(inequality=inequality):
            self.cli.show_shannon_type()
        else:
            self.cli.show_non_shannon_type()
    
    def _get_constraints(self) -> None:
        os.system("clear")

        self.cli.show_constraint_rules()
        constraints = self.cli.get_constraints()

        if constraints is not False:
            self.prover.add_constraints(raw_constraints=constraints)

    def play(self) -> None:
        while True:
            action = input(
                f"Please enter '1' for calculating inequality or '2' for adding inequalities or 'q' for quiting the program \n > "
            )
            match action.isdecimal():
                case True:
                    if int(action) == 1:
                        self._calculate_inequality()
                    
                    if int(action) == 2:
                        self._get_constraints()

                case False:
                    if action.lower() == "q":
                        break
        print("Program ends !")


if __name__ == "__main__":
    prover = InteractiveProver2RV(
        cli=TwoRandomVariableCLI(), prover=TwoRVInequalityProver()
    )

    prover.play()
