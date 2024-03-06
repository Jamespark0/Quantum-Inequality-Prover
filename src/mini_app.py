"""
This project only serves a quick preview on how things look like
"""

import os
import sys
from dataclasses import dataclass
from functools import partial
from typing import Callable

from src.controller import InequalityController, Prover
from src.model import EntropicSpace, Inequality, QuantumInequality
from src.view import ProverResultMessage, TerminalInput, TerminalMessage


@dataclass
class MiniApp:
    # Number of random variables
    n: int

    def __post_init__(self) -> None:
        space = EntropicSpace(n=self.n)
        self.controller = InequalityController(
            model=Inequality(dim=len(space.all_pairs)),
            inputView=TerminalInput(),
            messageView=TerminalMessage(tuple(space.to_index.keys())),
        )

        add_inequality = partial(
            self.controller.add_inequality_v2, mapping=space.to_index
        )
        add_inequality.__name__ = "add_inequality"

        add_constraint = partial(
            self.controller.add_single_constraint, mapping=space.to_index
        )
        add_constraint.__name__ = "add_one_constraint"

        # All possible actions for this app
        self.actions: dict[str, Callable[[], None]] = {
            "1": add_inequality,
            "2": add_constraint,
            "3": self.controller.clear_constraints,
            "4": self.check_shannon_type,
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

    def check_shannon_type(self) -> None:
        if self.controller.inequality.shape[0] == 0:
            print("Please add an inequality")

        elif self.prover.check_type(
            self.prover.calculate(
                inequality=self.controller.inequality,
                constraints=self.controller.constraints,
            )
        ):
            print("It's von-Neumann type!")
            print("\n")
            used_elemental, used_constraints = self.prover.shortest_proof_generator(
                inequality=self.controller.inequality,
                constraints=self.controller.constraints,
            )
            (
                elemental_msg,
                constraint_msg,
            ) = ProverResultMessage().generate_shortest_proof(
                used_elementals=used_elemental,
                used_constraints=used_constraints,
                elementals=self.prover.elemental,
                constraints=self.controller.constraints,
                index_order=self.controller.messageView.index_order,
            )

            if len(elemental_msg) > 0:
                print(elemental_msg[0])
                for _ in elemental_msg[1:]:
                    print(_ + " >= 0")
            print()
            if len(constraint_msg) > 0:
                print(constraint_msg[0])
                for _ in constraint_msg[1:]:
                    print(_ + " = 0")

        else:
            print("It's not provable by Quantum ITIP :(")
            print()
            used_elemental, used_constraints = self.prover.shortest_disprove_generator(
                n=self.n,
                inequality=self.controller.inequality,
                constraints=self.controller.constraints,
            )
            (
                elemental_msg,
                constraint_msg,
            ) = ProverResultMessage().generate_shortest_disprove(
                used_elementals=used_elemental,
                used_constraints=used_constraints,
                elementals=self.prover.elemental,
                constraints=self.controller.constraints,
                index_order=self.controller.messageView.index_order,
            )

            if len(elemental_msg) > 0:
                print(elemental_msg[0])
                for _ in elemental_msg[1:]:
                    print(_ + " = 0")
            print()
            if len(constraint_msg) > 0:
                print(constraint_msg[0])
                for _ in constraint_msg[1:]:
                    print(_ + " = 0")

        print("\n" * 5)
        input("Press anything to continue...")


if __name__ == "__main__":
    while True:
        n = input("Input the number of systems: ")
        if n.isdigit() and int(n) > 1:
            n = int(n)
            break
        else:
            print("Input an integer greater than 1")

    app = MiniApp(n)
    app.start()
