import logging

import pytest
from fizzbuzz.fizzbuzz import fizzbuzz, fizzbuzz_list

logger = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 2),
        (3, "Fizz"),
        (4, 4),
        (5, "Buzz"),
        (6, "Fizz"),
        (15, "FizzBuzz"),
        (30, "FizzBuzz"),
    ],
)
def test_fizzbuzz_1(n: int, expected: int | str) -> None:
    assert fizzbuzz(n) == expected


def test_fizzbuzz_list() -> None:
    seq = fizzbuzz_list(1, 5)

    logger.info(seq)

    assert len(list(seq)) == 5
