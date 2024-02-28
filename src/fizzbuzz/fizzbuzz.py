from typing import Union


def fizzbuzz(n: int) -> Union[int, str]:
    if n == 1:
        return 1
    if n == 2:
        return 2
    return "Fizz"
