from dataclasses import InitVar, dataclass, field

import numpy as np
from numpy.typing import NDArray

from src.model.model import BaseModel


@dataclass
class Inequality(BaseModel):
    n: InitVar[int]
    _expressions: NDArray = field(init=False)

    def __post_init__(self, n: int):
        self._expressions = np.empty((0, 2**n - 1))

    @property
    def expressions(self) -> NDArray:
        return self._expressions

    @expressions.setter
    def expressions(self, new_inequality: NDArray):
        self._expressions = new_inequality
