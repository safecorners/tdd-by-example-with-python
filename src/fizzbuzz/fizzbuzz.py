from typing import Iterable, Union


def is_multiple_of(n: int, k: int) -> bool:
    return n % k == 0


def fizzbuzz(n: int) -> Union[int, str]:
    if is_multiple_of(n, 3) and is_multiple_of(n, 5):
        return "FizzBuzz"
    if is_multiple_of(n, 3):
        return "Fizz"
    if is_multiple_of(n, 5):
        return "Buzz"
    return n


def fizzbuzz_list(from_: int, to_: int) -> Iterable[Union[int, str]]:
    return [fizzbuzz(n) for n in range(from_, to_ + 1)]


if __name__ == "__main__":
    list = fizzbuzz_list(1, 100)
    print(list)
