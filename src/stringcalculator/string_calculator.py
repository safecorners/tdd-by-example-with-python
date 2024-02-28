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
            if token.isdigit():
                tokens.append(token)

        if not tokens:
            return 0

        sum = 0
        for token in tokens:
            sum += int(token)

        return sum
