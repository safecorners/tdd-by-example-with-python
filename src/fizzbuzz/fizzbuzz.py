from typing import Iterable, Tuple

Policy = Tuple[int, str]


def is_multiple_of(m: int, k: int) -> bool:
    return m % k == 0


def stringify(m: int, policies: Iterable[Policy]) -> str:
    words = []
    for k, word in policies:
        if is_multiple_of(m, k):
            words.append(word)
    if words:
        return "".join(words)

    return str(m)


def fizzbuzz(n: int, policies: Iterable[Policy]) -> Iterable[str]:
    return [stringify(m, policies) for m in range(1, n + 1)]
