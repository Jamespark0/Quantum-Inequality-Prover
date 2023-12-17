from abc import ABC, abstractmethod

from numpy.typing import NDArray


class Controller(ABC):
    @abstractmethod
    def get_expressions(self) -> NDArray:
        raise NotImplementedError

    @abstractmethod
    def add_expressions(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def _validate_and_format_user_input(self, new_expressions: str) -> list:
        raise NotImplementedError

    @abstractmethod
    def show_expressions(self) -> None:
        raise NotImplementedError
