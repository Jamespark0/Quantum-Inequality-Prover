def to_joint_entropy(pair: set | frozenset):
    return f'H({",".join(str(x) for x in tuple(pair))})'
