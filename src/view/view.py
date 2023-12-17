from abc import ABC, abstractmethod

from numpy.typing import NDArray


class View(ABC):
    @abstractmethod
    def show_expressions(self, expressions: NDArray):
        raise NotImplementedError

    @abstractmethod
    def show_rules(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_input_message(self) -> str:
        raise NotImplementedError
