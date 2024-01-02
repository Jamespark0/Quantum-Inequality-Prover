from src.model.inequality import Inequality


def test_initialization() -> None:
    dim: int = 3

    canonical = Inequality(dim=dim)

    assert canonical.constraints.shape == (0, dim)
    assert canonical.expression.shape == (0, dim)
