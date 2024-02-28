from typing import Iterable, Tuple, Union


def is_multiple_of(n: int, k: int) -> bool:
    return n % k == 0


def fizzbuzz(n: int, policies: Iterable[Tuple[int, str]]) -> Union[int, str]:
    words = []
    for k, word in policies:
        if is_multiple_of(n, k):
            words.append(word)
    if words:
        return "".join(words)
    return n


def fizzbuzz_sequence(
    from_: int, to_: int, policies: Iterable[Tuple[int, str]]
) -> Iterable[Union[int, str]]:
    return [fizzbuzz(n, policies) for n in range(from_, to_ + 1)]


if __name__ == "__main__":
    result = fizzbuzz_sequence(1, 100, [(3, "Fizz"), (5, "Buzz")])
    print(result)
