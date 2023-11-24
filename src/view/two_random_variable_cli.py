def is_all_float(values: list):
    """
    Pass a sequence of values, and check if every element within the sequence can be converted to
    float

    Args:
        values (list): Elements to be converted to float

    Returns:
        If all the element can be converted to float, return the converted list

        Otherwise, return False
    """
    try:
        result = list(map(float, values))
    except ValueError:
        return False
    else:
        return result


class TwoRandomVariableCLI:
    def show_inequality_rules(self):
        print()
        print("=" * 70)
        print("This is a two-random-variable inequality prover!\n")
        print("In general, an information inequality can be expressed as follows:")
        print("a * H(1) + b * H(2) + c * H(1,2) >= 0\n")
        print("The input should be 3 numbers, a b c, separated by spaces.")
        print("=" * 70)
        print()

    def show_constraint_rules(self) -> None:
        print(
            "A single constraint takes the form of a * H(1) + b * H(2) + c * H(1, 2) = 0."
        )
        print("The input should be 3 numbers, a b c, separated by spaces.")
        print(
            "If more than one constraints are to be inserted, separate them with comma, ','"
        )

    def show_shannon_type(self) -> None:
        print("It's Shannon-type.\n")

    def show_non_shannon_type(self) -> None:
        print("It's not provable by ITIP algorithm!\n")

    def get_inequality(self) -> list[float]:
        while True:
            print("Input a,b, and c w.r.t a * H(1) + b * H(2) + c * H(1,2) >= 0")
            coefficients = input("$ ").split()

            if len(coefficients) != 3:
                print("Input three values!\n")

            else:
                inequality = is_all_float(coefficients)
                if inequality:
                    return inequality
                else:
                    print("Input only numerical values")

    def get_constraints(self):
        """
        Prompt the user to enter a series of constraints.

        If there is a single invalid input, return False.

        Otherwise, return the a list of inputed constraint

        """
        while True:
            print("Input a, b, and c w.r.t a * H(1) + b * H(2) + c * H(1,2) = 0")
            constraints: list = input("> > ").split(",")

            for i, raw in enumerate(constraints):
                constraint = raw.split()

                if len(constraint) != 3:
                    return False

                constraint = is_all_float(constraint)
                if constraint is not False:
                    constraints[i] = constraint
                else:
                    return False

            return constraints


# To be deleted
if __name__ == "__main__":
    TwoRandomVariableCLI().show_inequality_rules()
    TwoRandomVariableCLI().show_shannon_type()
    TwoRandomVariableCLI().show_non_shannon_type()
    print(TwoRandomVariableCLI().get_inequality())
