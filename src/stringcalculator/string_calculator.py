from typing import List


class StringCalculator:
    def __init__(self) -> None:
        ...

    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        tokens = []
        for character in numbers.split(","):
            tokens.append(character)

        queue = []
        for token in tokens:
            result = token.split("\n")
            for t in result:
                queue.append(t)

        if not queue:
            return 0

        sum = 0
        for element in queue:
            sum += int(element)

        return sum
