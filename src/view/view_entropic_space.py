from src.shared import EntropicSpace
from src.util import to_joint_entropy


class EntropicSpaceView:
    def __init__(self, space: EntropicSpace):
        self.space: EntropicSpace = space

    def display_inequality_rules(self):
        print(
            "In general, an information inequality can be expressed as the following:",
            end="\n\n",
        )
        print(
            f'{" + ".join(f"a({x[1] + 1}) * {to_joint_entropy(pair=x[0])}" for x in sorted(self.space.to_index.items(), key=lambda x: x[1]))}',
            end="\n\n",
        )

    def get_inequality_input_msg(self):
        return (
            f"The input should contain {len(self.space.all_pairs)} numbers, and in the order of: "
            + f'{", ".join(f"a({i})" for i in range(1, len(self.space.all_pairs) + 1))}'
            + "\n# "
        )
