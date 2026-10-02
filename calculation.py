from operations import Operations


class Calculation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        raise NotImplementedError(
            "Subclasses must implement execute()."
        )


class Addition(Calculation):
    def execute(self):
        return Operations.add(self.a, self.b)


class Subtraction(Calculation):
    def execute(self):
        return Operations.subtract(self.a, self.b)


class Multiplication(Calculation):
    def execute(self):
        return Operations.multiply(self.a, self.b)


class Division(Calculation):
    def execute(self):
        return Operations.divide(self.a, self.b)


class CalculationFactory:

    @staticmethod
    def create(operator, a, b):
        calculations = {
            "+": Addition,
            "-": Subtraction,
            "*": Multiplication,
            "/": Division
        }

        if operator not in calculations:
            raise ValueError("Invalid operation.")

        return calculations[operator](a, b)