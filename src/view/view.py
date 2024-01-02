from abc import ABC, abstractmethod

from numpy.typing import NDArray


class View(ABC):
    @abstractmethod
    def show_inequality(self, expressions: NDArray) -> None:
        raise NotImplementedError

    @abstractmethod
    def show_constraints(self, constraitns: NDArray) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_inequality_rules(self) -> str:
        raise NotImplementedError

    def get_constraints_rules(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_input_message(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_inequality(self) -> NDArray:
        raise NotImplementedError

    @abstractmethod
    def get_constraints(self) -> NDArray:
        raise NotImplementedError


class BaseInput(ABC):
    @abstractmethod
    def get_inequality(self) -> NDArray:
        ...

    @abstractmethod
    def get_constraints(self) -> NDArray:
        ...


class BaseMessage(ABC):
    @abstractmethod
    def get_inequality_rules(self) -> tuple[str, ...]:
        ...

    @abstractmethod
    def get_constraints_rules(self) -> tuple[str, ...]:
        ...

    @abstractmethod
    def get_input_message(self) -> str:
        ...

    @abstractmethod
    def show_inequality(self, inequalities: NDArray) -> tuple[str, ...]:
        ...

    @abstractmethod
    def show_constraints(self, constraitns: NDArray) -> tuple[str, ...]:
        ...
