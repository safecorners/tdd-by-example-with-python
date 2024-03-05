from typing import Iterable

import pytest
from fizzbuzz.fizzbuzz import Policy, fizzbuzz


@pytest.mark.parametrize("policies", [([(3, "Fizz"), (5, "Buzz")])])
@pytest.mark.parametrize(
    "n, expected",
    [
        (3, ["1", "2", "Fizz"]),
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (15, ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]) # noqa: E501
    ],
)  # fmt: skip
def test_fizzbuzz(
    policies: Iterable[Policy],
    n: int,
    expected: Iterable[str],
) -> None:
    assert fizzbuzz(n, policies) == expected
