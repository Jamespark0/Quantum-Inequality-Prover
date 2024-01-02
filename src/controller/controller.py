from abc import ABC, abstractmethod


class BaseController(ABC):
    @abstractmethod
    def add_inequality(self) -> None:
        ...

    @abstractmethod
    def add_constraints(self) -> None:
        ...

    @abstractmethod
    def show_inequality(self) -> None:
        ...

    @abstractmethod
    def show_constraints(self) -> None:
        ...
