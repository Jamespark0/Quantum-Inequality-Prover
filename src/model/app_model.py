from dataclasses import dataclass, field

from numpy.typing import NDArray

from src.controller.constraint_controller import ConstraintController
from src.controller.inequality_controller import InequalityController


@dataclass
class AppModel:
    _constraint_controller: ConstraintController
    _inequality_controller: InequalityController
    _elemental_inequalities: NDArray

    actions: dict = field(init=False, default_factory=dict)

    @property
    def constraint_controller(self):
        return self._constraint_controller

    # @constraint_controller.setter
    # def constraint_controller(self, controller: ConstraintController):
    #     self._constraint_controller = controller

    @property
    def inequality_controller(self):
        return self._inequality_controller

    # @inequality_controller.setter
    # def inequality_controller(self, controller: InequalityController):
    #     self._inequality_controller = controller

    @property
    def elemental_inequalities(self):
        return self._elemental_inequalities

    # @elemental_inequalities.setter
    # def elemental_inequalities(self, elemental: NDArray):
    #     self.elemental_inequalities = elemental
