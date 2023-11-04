import os
import sys

sys.path.insert(0, ".")

from two_random_variable_prover import TwoRVInequalityProver

# from src.two_random_variable_cli import TwoRandomVariableCLI
from src import TwoRandomVariableCLI


class InteractiveProver2RV:
    def __init__(self, cli: TwoRandomVariableCLI, prover: TwoRVInequalityProver):
        self.cli = cli
        self.prover = prover
    
    def one_round(self):
        os.system("clear")
        
        self.cli.show_rules()

        inequality = self.cli.get_inequality()

        if self.prover.is_shannon_type(inequality=inequality):
            self.cli.show_shannon_type()
        else:
            self.cli.show_non_shannon_type()
    
    def play(self) -> None:
        while True:
            action = input(f"Please enter '1' for calculating inequality or 'q' for quiting the program > ")
            match action.isdecimal():
                case True:
                    if int(action) == 1:
                        self.one_round()
                
                case False:
                    if action.lower() == 'q':
                        break
        print("Program ends !")


if __name__ == "__main__":
    prover = InteractiveProver2RV(cli=TwoRandomVariableCLI(), prover=TwoRVInequalityProver())

    prover.play()