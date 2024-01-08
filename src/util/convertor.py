class InvalidPairError(IndexError):
    def __init__(self, message: str = ""):
        super().__init__(message)


def to_joint_entropy(pair: set | frozenset):
    return f'H({",".join(str(x) for x in tuple(pair))})'


def turn_str_to_pair(string: str) -> frozenset:
    pair = frozenset(
        [
            int(value) if value.isdigit() and int(value) > 0 else None
            for value in string.split()
        ]
    )

    if None in pair or pair == frozenset():
        raise InvalidPairError
    else:
        return pair
