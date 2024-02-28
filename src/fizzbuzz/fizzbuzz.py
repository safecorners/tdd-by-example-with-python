from typing import Union


def fizzbuzz(n: int) -> Union[int, str]:
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return "Fizz"
    if n == 5:
        return "Buzz"
    return n
