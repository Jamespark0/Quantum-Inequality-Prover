from src.shared import EntropicSpace


class ViewEntropicSpace:
    def __init__(self, space: EntropicSpace):
        self.space: EntropicSpace = space

    def display_inequality_rules(self):
        print(
            "In general, an information inequality can be expressed as the following:",
            end="\n\n",
        )
        print(
            f'{" + ".join(f"{self._map_set_to_joint_entropy(pair=x[0], index=x[1])}" for x in sorted(self.space.to_index.items(), key=lambda x: x[1]))}',
            end="\n\n",
        )
        print(
            f"The input should contain {len(self.space.all_pairs)} numbers, and in the order of: ",
            end="",
        )
        print(
            f'{", ".join(f"a({i})" for i in range(1, len(self.space.all_pairs) + 1))}'
        )

    def _map_set_to_joint_entropy(self, pair: set | frozenset, index: int):
        return f'a({index + 1}) * H({",".join(str(x) for x in tuple(pair))})'
