import logging
from typing import Iterable, Tuple, Union

import pytest
from fizzbuzz.fizzbuzz import fizzbuzz, fizzbuzz_sequence

logger = logging.getLogger(__name__)


@pytest.mark.parametrize("policies", [([(3, "Fizz"), (5, "Buzz")])])
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
def test_fizzbuzz(
    policies: Iterable[Tuple[int, str]], n: int, expected: Union[int, str]
) -> None:
    logger.info(policies)
    assert fizzbuzz(n, policies) == expected


def test_fizzbuzz_with_no_condition() -> None:
    result = [fizzbuzz(n, []) for n in range(1, 11)]
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_fizzbuzz_sequence() -> None:
    sequence = fizzbuzz_sequence(1, 15, [(3, "Fizz"), (5, "Buzz")])

    logger.info(sequence)

    assert len(list(sequence)) == 15
