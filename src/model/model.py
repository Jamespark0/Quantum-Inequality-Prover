from abc import ABC, abstractmethod
from dataclasses import InitVar, dataclass

from numpy.typing import NDArray


@dataclass
class BaseModel(ABC):
    n: InitVar[int]
    _expressions: NDArray

    @property
    @abstractmethod
    def expressions(self):
        raise NotImplementedError
