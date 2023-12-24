from src.model.canonical import Canonical


def test_initialization() -> None:
    dim: int = 3

    canonical = Canonical(dim=dim)

    assert canonical.constraints.shape == (0, dim)
    assert canonical.inequality.shape == (0, dim)
