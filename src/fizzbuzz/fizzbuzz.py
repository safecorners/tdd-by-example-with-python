from typing import Iterable, Union


def fizzbuzz(n: int) -> Union[int, str]:
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return n


def fizzbuzz_list(from_: int, to_: int) -> Iterable[Union[int, str]]:
    result = []
    for n in range(from_, to_ + 1):
        result.append(fizzbuzz(n))
    return result


if __name__ == "__main__":
    list = fizzbuzz_list(1, 100)
    print(list)
