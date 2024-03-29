import re


class StringCalculator:
    def __init__(self) -> None:
        self.delimiter = ","
        self.expression = ""

    def get_delimiter(self) -> None:
        """
        Syntax: //[delimiter]\n[numbers...]
        """
        if self.expression.startswith("//"):
            idx = self.expression.find("\n")
            self.delimiter = self.expression[len("//") : idx]
            self.expression = self.expression[
                len("//") + len(self.delimiter) + len("\n") :
            ]

    def handle_new_lines(self, expression: str) -> str:
        return expression.replace("\n", self.delimiter)

    def add(self, numbers: str) -> int:
        self.expression = numbers
        self.get_delimiter()

        self.expression = self.handle_new_lines(self.expression)

        tokens = []
        for token in self.expression.split(self.delimiter):
            if re.match(r"^-?[0-9]+$", token):
                tokens.append(token)

        if not tokens:
            return 0

        sum = 0
        negatives = []
        for token in tokens:
            number = int(token)
            if number < 0:
                negatives.append(number)
            sum += number

        if negatives:
            raise Exception(f"negatives not allowed - {negatives}")

        return sum
