from calculation import CalculationFactory


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

        try:
            num1 = float(first_input)
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        operator = input(
            "Enter an operation (+, -, *, /): "
        ).strip()

        if operator not in ["+", "-", "*", "/"]:
            print("Error: Invalid operation.")
            continue

        try:
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        try:
            calculation = CalculationFactory.create(
                operator, num1, num2
            )

            result = calculation.execute()

            print("Result:", result)

            history.append(
                f"{num1} {operator} {num2} = {result}"
            )

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()