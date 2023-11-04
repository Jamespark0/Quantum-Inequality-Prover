def is_float(value: str) -> bool:
    try:
        float(value)
    except ValueError:
        return False
    else:
        return True

class TwoRandomVariableCLI:
    def show_rules(self):
        print()
        print("=" * 70)
        print("This is a two-random-variable inequality prover!\n")
        print("In general, an information inequality can be expressed as follows:")
        print("a * H(1) + b * H(2) + c * H(1,2) >= 0\n")
        print("The input should be 3 numbers, a b c, separated by spaces.")
        print("=" * 70)
        print()

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
            elif all([is_float(element) for element in coefficients]):
                # return a list of floats
                return [float(element) for element in coefficients]
            else:
                print("Please only enter numbers.\n")
        

# To be deleted
if __name__ == "__main__":
    TwoRandomVariableCLI().show_rules()
    TwoRandomVariableCLI().show_shannon_type()
    TwoRandomVariableCLI().show_non_shannon_type()
    print(TwoRandomVariableCLI().get_inequality())