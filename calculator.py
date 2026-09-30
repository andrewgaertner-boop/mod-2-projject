class Calculation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        raise NotImplementedError


class Addition(Calculation):
    def execute(self):
        return self.a + self.b


class Subtraction(Calculation):
    def execute(self):
        return self.a - self.b


class Multiplication(Calculation):
    def execute(self):
        return self.a * self.b


class Division(Calculation):
    def execute(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero.")
        return self.a / self.b


class CalculationFactory:
    @staticmethod
    def create(operator, a, b):
        if operator == "+":
            return Addition(a, b)

        elif operator == "-":
            return Subtraction(a, b)

        elif operator == "*":
            return Multiplication(a, b)

        elif operator == "/":
            return Division(a, b)

        else:
            raise ValueError("Invalid operation.")


def show_help():
    print()
    print("Available commands:")
    print("  help     - Show this help message")
    print("  history  - Show previous calculations")
    print("  exit     - Exit the calculator")
    print("  +        - Addition")
    print("  -        - Subtraction")
    print("  *        - Multiplication")
    print("  /        - Division")
    print()


def show_history(history):
    if not history:
        print("No calculations yet.")
    else:
        print("\nCalculation History:")
        for calculation in history:
            print(calculation)

def main():
    history = []

    print("Simple Calculator")
    print("------------------")
    print("Type 'help', 'history', or 'exit' at the first prompt.")

    while True:

        # First number or special command
        first_input = input(
            "\nEnter first number (or command): "
        ).strip().lower()

        if first_input == "help":
            show_help()
            continue

        elif first_input == "history":
            show_history(history)
            continue

        elif first_input == "exit":
            print("Goodbye!")
            break

        # Convert first input to a number
        try:
            num1 = float(first_input)
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        # Operator
        operator = input(
            "Enter an operation (+, -, *, /): "
        ).strip()

        if operator not in ["+", "-", "*", "/"]:
            print("Error: Invalid operation.")
            continue

        # Second number
        try:
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        # Factory creates the calculation
        try:
            calculation = CalculationFactory.create(
                operator, num1, num2
            )

            result = calculation.execute()

            print("Result:", result)

            # Save calculation to history
            history.append(
                f"{num1} {operator} {num2} = {result}"
            )

        except ValueError as error:
            print("Error:", error)

if __name__ == "__main__":
    main()
