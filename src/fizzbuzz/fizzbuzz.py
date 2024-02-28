from typing import Iterable, Union


def is_multiple_of_three(n: int) -> bool:
    return n % 3 == 0


def is_multiple_of_five(n: int) -> bool:
    return n % 5 == 0


def fizzbuzz(n: int) -> Union[int, str]:
    if is_multiple_of_three(n) and is_multiple_of_five(n):
        return "FizzBuzz"
    if is_multiple_of_three(n):
        return "Fizz"
    if is_multiple_of_five(n):
        return "Buzz"
    return n


def fizzbuzz_list(from_: int, to_: int) -> Iterable[Union[int, str]]:
    return [fizzbuzz(n) for n in range(from_, to_)]


if __name__ == "__main__":
    list = fizzbuzz_list(1, 100)
    print(list)
