from src.controller_factory import ControllerFactory
from src.model import EntropicSpace


def main(space: EntropicSpace):
    factory = ControllerFactory(space=space)
    constraint_controller = factory.get_constraint_controller()
    inequality_controller = factory.get_inequality_controller()

    constraint_controller.add_constraints()
    constraint_controller.show_constraints()
    inequality_controller.set_inequality()
    inequality_controller.show_inequality()


if __name__ == "__main__":
    space = EntropicSpace(n=2)
    main(space)
