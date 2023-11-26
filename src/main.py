from src.shared import EntropicSpace
from src.view import EntropicSpaceView


def main(space: EntropicSpace):
    view = EntropicSpaceView(space=space)
    view.display_inequality_rules()


if __name__ == "__main__":
    space = EntropicSpace(n=3)
    main(space)
