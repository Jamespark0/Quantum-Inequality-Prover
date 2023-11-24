from src.shared import EntropicSpace
from src.view import ViewEntropicSpace


def main(space: EntropicSpace):
    view = ViewEntropicSpace(space=space)
    view.display_inequality_rules()


if __name__ == "__main__":
    space = EntropicSpace(n=3)
    main(space)
