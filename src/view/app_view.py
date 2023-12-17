import os
from typing import Callable


class AppView:
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def greeting(self) -> None:
        print("Welcome to the Information Inequality Prover!")

    def get_num_random_variables(self) -> int:
        while True:
            n = input("Please enter the number of random variables in the system:\n# ")
            if n.isdigit() and int(n) > 1:
                print()
                return int(n)
            else:
                print(f"{n} is not an integer greater than 1!")

    def show_actions(self, actions: dict[str, tuple[Callable, ...]]) -> None:
        for key in actions.keys():
            print(f"{key} => {actions[key][0].__name__}")

    def get_action(self, actions: dict[str, tuple[str, Callable]]) -> str:
        while True:
            user_action = input("Please choose an action: ")

            if user_action not in set(actions.keys()):
                print("Please enter a valid operation!")

            else:
                return user_action

    def buffer(self):
        input("Press anything to continue ...")

    def show_shannon_type_message(self):
        print("It's Shannon-type!")

    def show_not_provable_message(self) -> None:
        print("It's not provable by ITIP!")
