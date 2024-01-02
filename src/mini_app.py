"""
This project only serves a quick preview on how things look like
"""

import os
import sys
from dataclasses import InitVar, dataclass
from typing import Callable

from src.controller import InequalityController, Prover
from src.model import EntropicSpace, Inequality, QuantumInequality
from src.view import TerminalInput, TerminalMessage


@dataclass
class MiniApp:
    n: InitVar[int]

    def __post_init__(self, n: int) -> None:
        space = EntropicSpace(n=n)
        self.controller = InequalityController(
            model=Inequality(dim=len(space.all_pairs)),
            inputView=TerminalInput(),
            messageView=TerminalMessage(tuple(space.to_index.keys())),
        )

        self.actions: dict[str, Callable[[], None]] = {
            "1": self.controller.add_inequality,
            "2": self.controller.add_constraints,
            "3": self.controller.clear_constraints,
            "4": self.check_shanno_type,
            "q": self.end_prover,
        }
        self.prover: Prover = Prover(elemental=QuantumInequality(space=space).ELEMENTAL)

    def homepage(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        # Print all possible actions
        for action in self.actions.items():
            print(f"{action[0]}: {' '.join(action[1].__name__.split('_'))}")
        self.controller.show_inequality()
        self.controller.show_constraints()
        print("\n" * 2)

    def single_round(self) -> None:
        self.homepage()

        choice = input("Pick an action: ")
        if choice not in self.actions.keys():
            print("Please choose a valid action!")
        elif choice.lower() == "q":
            self.actions["q"]()
        else:
            self.actions[choice]()

    def start(self) -> None:
        while True:
            self.single_round()

    def end_prover(self) -> None:
        print("Prover ends!")
        sys.exit()

    def check_shanno_type(self) -> None:
        if self.controller.inequality.shape[0] == 0:
            print("Please add an inequality")

        elif self.prover.check_type(
            self.prover.calculate(
                inequality=self.controller.inequality,
                constraints=self.controller.constraints,
            )
        ):
            print("It's Shannon_type!")
        else:
            print("It's not provable by ITIP :(")

        print("\n" * 5)
        input("Press anything to continue...")


if __name__ == "__main__":
    while True:
        n = input("Input the number of systems: ")
        if n.isdigit() and int(n) > 0:
            n = int(n)
            break
        else:
            print("Input a positive integer")

    app = MiniApp(n)
    app.start()
