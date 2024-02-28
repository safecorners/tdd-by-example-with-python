class StringCalculator:
    def __init__(self) -> None:
        ...

    def add(self, numbers: str) -> int:
        queue = []

        for character in numbers.split(","):
            if character.isdigit():
                queue.append(int(character))

        if not queue:
            return 0

        sum = 0
        for element in queue:
            sum += int(element)

        return sum
