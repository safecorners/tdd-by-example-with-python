from typing import List, Tuple

from fibonacci.iter08.fibonacci import fib


def test_fibonacci() -> None:
    cases: List[Tuple[int, int]] = [(0, 0), (1, 1), (2, 1), (3, 2)]
    for n, expected in cases:
        assert fib(n) == expected
