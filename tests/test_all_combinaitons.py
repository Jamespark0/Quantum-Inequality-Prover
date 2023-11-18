from classical import g_creator


def test_from_no_element() -> None:
    assert g_creator.all_combinations(n=0) == ()

def test_from_single_element() -> None:
    assert g_creator.all_combinations(n=1) == ({1},)

def test_from_two_element() -> None:
    assert g_creator.all_combinations(n=2) == ({1}, {2}, {1,2},)
    
def test_from_three_element() -> None:
    assert g_creator.all_combinations(n=3) == ({1},{2},{3},{1,2},{1,3},{2,3},{1,2,3},)

def test_from_four_element() -> None:
    all_pairings: tuple[set[int], ...] = g_creator.all_combinations(n = 4)
    assert len(all_pairings) == 2**4 - 1

def test_from_ten_element() -> None:
    all_pairings = g_creator.all_combinations(n = 10)
    assert len(all_pairings) == 2**10 - 1
