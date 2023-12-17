from dataclasses import dataclass, field

# from numpy.typing import NDArray
# from src.model import EntropicSpace
# from src.util import to_joint_entropy
from src.view.view_tui import ViewTUI


@dataclass
class InequalityView(ViewTUI):
    _target: tuple = field(init=False, default=("inequality", " >= 0"))
    index_order: tuple
