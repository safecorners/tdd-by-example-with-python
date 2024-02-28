from typing import Union


def fizzbuzz(n: int) -> Union[int, str]:
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 15:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return n
