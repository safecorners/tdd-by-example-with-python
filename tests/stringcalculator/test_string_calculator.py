import pytest
from stringcalculator import StringCalculator


@pytest.fixture(scope="function")
def calc() -> StringCalculator:
    return StringCalculator()


def test_empty_string_should_be_0(calc: StringCalculator) -> None:
    assert calc.add("") == 0


def test_one_should_be_1(calc: StringCalculator) -> None:
    assert calc.add("1") == 1


def test_one_and_two_should_be_3(calc: StringCalculator) -> None:
    assert calc.add("1,2") == 3
